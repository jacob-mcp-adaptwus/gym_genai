"""Email manager for the bodybuilding app using AWS SES"""
from typing import List, Optional, Dict, Any
import boto3
from botocore.exceptions import ClientError

class EmailManager:
    """Handles all email operations for the bodybuilding app"""

    def __init__(self, logger, sender_email: str):
        """Initialize email manager with logger and sender email"""
        self.logger = logger
        self.sender = f"BodyBuildr AI Coach <{sender_email}>"
        self.charset = "UTF-8"
        self.client = boto3.client('ses')
        
        # Modern, responsive email styles
        self.default_styles = """
        <style>
            /* Reset styles */
            body {
                margin: 0;
                padding: 0;
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
            }
            
            /* Container */
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }
            
            /* Header */
            .header {
                background: #2c3e50;
                color: white;
                padding: 20px;
                text-align: center;
                border-radius: 8px 8px 0 0;
            }
            
            /* Content */
            .content {
                background: #ffffff;
                padding: 20px;
                border-radius: 0 0 8px 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            
            /* Tables */
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                background: #fff;
                border-radius: 8px;
                overflow: hidden;
            }
            
            th {
                background: #34495e;
                color: white;
                padding: 12px;
                text-align: left;
            }
            
            td {
                padding: 12px;
                border-bottom: 1px solid #eee;
            }
            
            tr:nth-child(even) {
                background: #f9f9f9;
            }
            
            /* Buttons */
            .button {
                display: inline-block;
                padding: 12px 24px;
                background: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 4px;
                margin: 10px 0;
            }
            
            /* Progress Bars */
            .progress-bar {
                background: #eee;
                height: 20px;
                border-radius: 10px;
                overflow: hidden;
            }
            
            .progress-fill {
                height: 100%;
                background: #2ecc71;
                transition: width 0.3s ease;
            }
            
            /* Responsive */
            @media (max-width: 600px) {
                .container {
                    width: 100%;
                    padding: 10px;
                }
                
                table {
                    font-size: 14px;
                }
            }
        </style>
        """

    def send_email(
        self, 
        recipients: List[str], 
        subject: str, 
        body_html: str,
        template_data: Optional[Dict[str, Any]] = None
    ) -> bool:
        """Send an email to one or more recipients"""
        try:
            # Apply template data if provided
            if template_data:
                body_html = self._apply_template(body_html, template_data)
            
            # Add container and styling
            formatted_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                {self.default_styles}
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>{subject}</h1>
                    </div>
                    <div class="content">
                        {body_html}
                    </div>
                </div>
            </body>
            </html>
            """
            
            for recipient in recipients:
                self.logger.info(f"Sending email to {recipient}")
                response = self.client.send_email(
                    Destination={'ToAddresses': [recipient]},
                    Message={
                        'Subject': {
                            'Charset': self.charset,
                            'Data': subject
                        },
                        'Body': {
                            'Html': {
                                'Charset': self.charset,
                                'Data': formatted_html
                            }
                        }
                    },
                    Source=self.sender
                )
                self.logger.info(f"Email sent successfully: {response['MessageId']}")
            
            return True
            
        except ClientError as e:
            self.logger.error(f"Failed to send email: {str(e)}")
            raise

    def send_workout_plan(
        self, 
        recipient: str, 
        plan_data: Dict[str, Any],
        start_date: str
    ) -> bool:
        """Send a workout plan email"""
        subject = f"Your New Workout Plan - Starting {start_date}"
        
        # Create workout plan HTML
        exercises_html = ""
        for day, workouts in plan_data['schedule'].items():
            exercises_html += f"<h3>{day}</h3><table>"
            exercises_html += "<tr><th>Exercise</th><th>Sets</th><th>Reps</th><th>Rest</th></tr>"
            for exercise in workouts:
                exercises_html += f"""
                <tr>
                    <td>{exercise['name']}</td>
                    <td>{exercise['sets']}</td>
                    <td>{exercise['reps']}</td>
                    <td>{exercise['rest']}s</td>
                </tr>
                """
            exercises_html += "</table>"
        
        body_html = f"""
        <h2>Your Personalized Workout Plan</h2>
        <p>Here's your customized workout plan designed to help you reach your fitness goals.</p>
        
        <h3>Goals</h3>
        <ul>
            {''.join(f'<li>{goal}</li>' for goal in plan_data['goals'])}
        </ul>
        
        <h3>Weekly Schedule</h3>
        {exercises_html}
        
        <h3>Notes</h3>
        <ul>
            {''.join(f'<li>{note}</li>' for note in plan_data['notes'])}
        </ul>
        
        <p>
            <a href="#" class="button">View Full Plan</a>
        </p>
        """
        
        return self.send_email([recipient], subject, body_html)

    def send_progress_update(
        self, 
        recipient: str, 
        progress_data: Dict[str, Any]
    ) -> bool:
        """Send a progress update email"""
        subject = "Your Fitness Progress Update"
        
        # Calculate progress percentages
        goal_progress = progress_data.get('goal_progress', {})
        progress_html = ""
        for goal, percentage in goal_progress.items():
            progress_html += f"""
            <div style="margin: 10px 0;">
                <strong>{goal}</strong>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {percentage}%"></div>
                </div>
                <span>{percentage}% Complete</span>
            </div>
            """
        
        body_html = f"""
        <h2>Progress Update</h2>
        
        <h3>Goal Progress</h3>
        {progress_html}
        
        <h3>Recent Achievements</h3>
        <ul>
            {''.join(f'<li>{achievement}</li>' for achievement in progress_data.get('achievements', []))}
        </ul>
        
        <h3>Recommendations</h3>
        <ul>
            {''.join(f'<li>{rec}</li>' for rec in progress_data.get('recommendations', []))}
        </ul>
        
        <p>
            <a href="#" class="button">View Detailed Progress</a>
        </p>
        """
        
        return self.send_email([recipient], subject, body_html)

    def _apply_template(self, template: str, data: Dict[str, Any]) -> str:
        """Apply template data to HTML template"""
        for key, value in data.items():
            template = template.replace(f"{{{{ {key} }}}}", str(value))
        return template 