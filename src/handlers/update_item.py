import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
    item_id = event["pathParameters"]["id"]
    body = json.loads(event["body"])

    table.update_item(
        Key={"id": item_id},
        UpdateExpression="SET #t = :t, #d = :d",
        ExpressionAttributeNames={
            "#t": "title",
            "#d": "done"
        },
        ExpressionAttributeValues={
            ":t": body.get("title", ""),
            ":d": body.get("done", False)
        }
    )

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"id": item_id, "title": body.get("title", ""), "done": body.get("done", False)})
    }