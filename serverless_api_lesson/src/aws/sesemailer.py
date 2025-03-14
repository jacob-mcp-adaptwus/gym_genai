# pylint: disable=C0301,W0212,R0902,R0903
# Databricks notebook source
"""spot-emailer"""
# pylint: disable=C0301,W0212,R0902,R0201
import boto3
class Emailer:
    """Class to Email"""
    config_dict = None
    sender = "SPOT <SPoTAdmin@thermofisher.onmicrosoft.com>"
    charset = "UTF-8"
    body_text = "Horizon Notification"
    default_styles = """
    <style>
        table {
          font-family: Arial, Helvetica, sans-serif;
          border-collapse: collapse;
          width: 100%;
        }
        table td, table th {
          border: 1px solid #ddd;
          padding: 8px;
        }
        table tr:nth-child(even){background-color: #f2f2f2;}
        table tr:hover {background-color: #ddd;}
        table th {
          padding-top: 12px;
          padding-bottom: 12px;
          text-align: left;
          background-color: #919191;
          color: white;
        }
    </style>"""

    def __init__(self):
        """intitalizing class take a dict"""
        self.client = boto3.client('ses')
            ###
    def send_email(self, recipients, subject, body_html):
        """send email function"""
        for recipient in recipients:
            response = self.client.send_email(
                Destination={
                    'ToAddresses': [recipient, ], },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.charset,
                            'Data': self.default_styles + body_html,
                        },
                        'Text': {
                            'Charset': self.charset,
                            'Data': self.body_text,
                        },
                    },
                    'Subject': {
                        'Charset': self.charset,
                        'Data': subject,
                    },
                },
                Source=self.sender,
            )
            print(response)
