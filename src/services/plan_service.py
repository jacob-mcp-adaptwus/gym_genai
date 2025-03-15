from typing import Dict, List, Any, Optional
from datetime import datetime
import json
import uuid
import os
from boto3.dynamodb.conditions import Key

class PlanService:
    def __init__(self, dynamodb_client, bedrock_manager):
        self.dynamodb_client = dynamodb_client
        self.bedrock_manager = bedrock_manager
        self.table_name = "bodybuilding-plans"
        self.versions_table_name = os.environ.get('PLAN_VERSIONS_TABLE', 'bodybuildr-planversions')

    async def create_plan(self, user_id: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new workout plan based on user requirements and preferences.
        """
        plan_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()

        # Initialize the base plan structure
        plan = {
            "plan_id": plan_id,
            "user_id": user_id,
            "created_at": timestamp,
            "updated_at": timestamp,
            "status": "draft",
            "version": 1,
            "goals": request_data["goals"],
            "experience_level": request_data["experience_level"],
            "available_days": request_data["available_days"],
            "preferences": request_data.get("preferences", {}),
            "limitations": request_data.get("limitations", []),
            "workout_plan": {},  # Will be populated by the AI
            "nutrition_plan": {},  # Will be populated by the AI
            "progress_tracking": {
                "measurements": {},
                "workout_logs": [],
                "nutrition_logs": []
            }
        }

        # Save the initial plan
        await self._save_plan(plan)
        
        # Save initial version
        await self._save_plan_version(plan_id, user_id, plan)
        
        return plan

    async def get_plan(self, plan_id: str, user_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves a specific workout plan.
        """
        response = await self.dynamodb_client.get_item(
            TableName=self.table_name,
            Key={
                "plan_id": {"S": plan_id},
                "user_id": {"S": user_id}
            }
        )
        return response.get("Item")

    async def update_plan(self, plan_id: str, user_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing workout plan with new information.
        """
        existing_plan = await self.get_plan(plan_id, user_id)
        if not existing_plan:
            raise ValueError(f"Plan {plan_id} not found")

        # Update the plan with new data
        updated_plan = {**existing_plan}
        updated_plan.update(updates)
        updated_plan["updated_at"] = datetime.utcnow().isoformat()
        updated_plan["version"] += 1

        # Save the updated plan to the main table
        await self._save_plan(updated_plan)
        
        # Save a new version to the versions table
        await self._save_plan_version(plan_id, user_id, updated_plan)
        
        return updated_plan

    async def delete_plan(self, user_id: str, plan_id: str) -> bool:
        """
        Deletes a plan and all its versions
        """
        try:
            # First verify the plan exists and user has access
            existing_plan = await self.get_plan(plan_id, user_id)
            if not existing_plan:
                raise ValueError(f"Plan {plan_id} not found")
                
            # Get all versions
            versions = await self.get_plan_versions(user_id, plan_id)
            
            # Delete all versions from versions table
            for version in versions:
                await self.dynamodb_client.delete_item(
                    TableName=self.versions_table_name,
                    Key={
                        "planId": {"S": plan_id},
                        "version": {"N": str(version.get('version', 1))}
                    }
                )
                
            # Delete main plan record
            await self.dynamodb_client.delete_item(
                TableName=self.table_name,
                Key={
                    "plan_id": {"S": plan_id},
                    "user_id": {"S": user_id}
                }
            )
            
            return True
            
        except Exception as err:
            print(f"Error deleting plan: {str(err)}")
            raise

    async def list_plans(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Lists all workout plans for a user.
        """
        response = await self.dynamodb_client.query(
            TableName=self.table_name,
            KeyConditionExpression="user_id = :uid",
            ExpressionAttributeValues={":uid": {"S": user_id}}
        )
        return response.get("Items", [])

    async def _save_plan(self, plan: Dict[str, Any]) -> None:
        """
        Internal method to save a plan to DynamoDB.
        """
        await self.dynamodb_client.put_item(
            TableName=self.table_name,
            Item=plan
        )
        
    async def _save_plan_version(self, plan_id: str, user_id: str, plan_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Save a version of a plan to the versions table
        """
        try:
            # Get current version number
            version_number = plan_data.get("version", 1)
            timestamp = datetime.utcnow().isoformat()
            
            # Create version item
            version_item = {
                'planId': plan_id,
                'userId': user_id,
                'version': version_number,
                'timestamp': timestamp,
                'goals': plan_data.get('goals', {}),
                'workout_plan': plan_data.get('workout_plan', {}),
                'nutrition_plan': plan_data.get('nutrition_plan', {}),
                'status': plan_data.get('status', 'draft'),
                'experience_level': plan_data.get('experience_level', 'beginner'),
                'available_days': plan_data.get('available_days', []),
                'preferences': plan_data.get('preferences', {}),
                'limitations': plan_data.get('limitations', [])
            }
            
            # Save version to versions table
            await self.dynamodb_client.put_item(
                TableName=self.versions_table_name,
                Item=version_item
            )
            
            return version_item
            
        except Exception as err:
            print(f"Error saving plan version: {str(err)}")
            raise
            
    async def get_plan_versions(self, user_id: str, plan_id: str) -> List[Dict[str, Any]]:
        """
        Get all versions of a plan after verifying access
        """
        try:
            # Verify access by checking if the plan exists for this user
            existing_plan = await self.get_plan(plan_id, user_id)
            if not existing_plan:
                return []
                
            # Query the versions table
            response = await self.dynamodb_client.query(
                TableName=self.versions_table_name,
                KeyConditionExpression="planId = :pid",
                ExpressionAttributeValues={":pid": {"S": plan_id}}
            )
            
            versions = response.get('Items', [])
            
            # Sort by version number
            return sorted(versions, key=lambda x: x.get('version', 0))
            
        except Exception as err:
            print(f"Error retrieving plan versions: {str(err)}")
            raise
            
    async def get_latest_version(self, user_id: str, plan_id: str) -> Optional[Dict[str, Any]]:
        """
        Get the latest version of a plan
        """
        try:
            versions = await self.get_plan_versions(user_id, plan_id)
            return versions[-1] if versions else None
        except Exception as err:
            print(f"Error retrieving latest version: {str(err)}")
            raise 