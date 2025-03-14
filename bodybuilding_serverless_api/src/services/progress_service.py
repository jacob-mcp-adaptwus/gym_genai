from typing import Dict, Any, List, Optional
from datetime import datetime
import json

class ProgressService:
    def __init__(self, dynamodb_client, plan_service):
        self.dynamodb_client = dynamodb_client
        self.plan_service = plan_service
        self.progress_table = "bodybuilding-progress"

    async def log_progress(self, user_id: str, plan_id: str, progress_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Log a new progress entry for a user's workout plan.
        """
        timestamp = datetime.utcnow().isoformat()
        progress_id = f"{plan_id}-{timestamp}"

        progress_entry = {
            "progress_id": progress_id,
            "plan_id": plan_id,
            "user_id": user_id,
            "timestamp": timestamp,
            "measurements": progress_data.get("measurements", {}),
            "workout_data": progress_data.get("workout_data", {}),
            "nutrition_data": progress_data.get("nutrition_data", {}),
            "notes": progress_data.get("notes", "")
        }

        # Save progress entry
        await self._save_progress(progress_entry)

        # Update the plan's progress tracking
        plan = await self.plan_service.get_plan(plan_id, user_id)
        if plan:
            plan_updates = {
                "progress_tracking": {
                    "measurements": progress_entry["measurements"],
                    "workout_logs": plan["progress_tracking"]["workout_logs"] + [progress_entry["workout_data"]],
                    "nutrition_logs": plan["progress_tracking"]["nutrition_logs"] + [progress_entry["nutrition_data"]]
                }
            }
            await self.plan_service.update_plan(plan_id, user_id, plan_updates)

        return progress_entry

    async def get_progress_history(self, user_id: str, plan_id: str, 
                                 start_date: Optional[str] = None, 
                                 end_date: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve progress history for a specific plan within a date range.
        """
        query_params = {
            "TableName": self.progress_table,
            "KeyConditionExpression": "plan_id = :pid",
            "ExpressionAttributeValues": {":pid": {"S": plan_id}}
        }

        if start_date and end_date:
            query_params["KeyConditionExpression"] += " AND #ts BETWEEN :start AND :end"
            query_params["ExpressionAttributeValues"].update({
                ":start": {"S": start_date},
                ":end": {"S": end_date}
            })
            query_params["ExpressionAttributeNames"] = {"#ts": "timestamp"}

        response = await self.dynamodb_client.query(**query_params)
        return response.get("Items", [])

    async def analyze_progress(self, user_id: str, plan_id: str) -> Dict[str, Any]:
        """
        Analyze user's progress and provide insights.
        """
        # Get all progress entries
        progress_history = await self.get_progress_history(user_id, plan_id)
        
        if not progress_history:
            return {
                "status": "no_data",
                "message": "No progress data available for analysis"
            }

        # Calculate progress metrics
        initial_measurements = progress_history[0]["measurements"]
        latest_measurements = progress_history[-1]["measurements"]
        
        changes = {
            metric: {
                "initial": initial_measurements.get(metric, 0),
                "current": latest_measurements.get(metric, 0),
                "change": latest_measurements.get(metric, 0) - initial_measurements.get(metric, 0)
            }
            for metric in initial_measurements.keys()
        }

        # Analyze workout consistency
        workout_logs = [entry["workout_data"] for entry in progress_history]
        total_workouts = len(workout_logs)
        
        return {
            "status": "success",
            "measurement_changes": changes,
            "workout_statistics": {
                "total_workouts": total_workouts,
                "average_workouts_per_week": total_workouts / max(1, len(progress_history) // 7)
            },
            "trends": self._calculate_trends(progress_history),
            "recommendations": self._generate_recommendations(changes, workout_logs)
        }

    def _calculate_trends(self, progress_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate trends in user's progress data.
        """
        # Implementation would include trend analysis for various metrics
        # This is a simplified version
        return {
            "strength_trend": "increasing",  # Would be calculated based on workout data
            "weight_trend": "stable",        # Would be calculated based on measurements
            "consistency_trend": "good"      # Would be calculated based on workout frequency
        }

    def _generate_recommendations(self, changes: Dict[str, Any], 
                                workout_logs: List[Dict[str, Any]]) -> List[str]:
        """
        Generate recommendations based on progress analysis.
        """
        recommendations = []
        
        # Example recommendations based on simple analysis
        # In a real implementation, this would be more sophisticated
        if workout_logs and len(workout_logs) < 3:
            recommendations.append("Increase workout frequency to at least 3 times per week")
            
        for metric, data in changes.items():
            if data["change"] == 0:
                recommendations.append(f"Consider adjusting your routine to improve {metric}")
            elif data["change"] < 0 and metric != "body_fat":
                recommendations.append(f"Focus on increasing {metric} through progressive overload")

        return recommendations

    async def _save_progress(self, progress_entry: Dict[str, Any]) -> None:
        """
        Save a progress entry to DynamoDB.
        """
        await self.dynamodb_client.put_item(
            TableName=self.progress_table,
            Item=progress_entry
        ) 