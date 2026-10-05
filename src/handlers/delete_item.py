import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
    item_id = event["pathParameters"]["id"]

    table.delete_item(Key={"id": item_id})

    return {
        "statusCode": 204,
        "headers": {"Content-Type": "application/json"},
        "body": ""
    }