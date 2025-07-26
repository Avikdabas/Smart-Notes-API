import boto3
import json
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SmartNotes')

def lambda_handler(event, context):
    note_id = event['pathParameters']['note_id']
    data = json.loads(event['body'])
    response = table.update_item(
        Key={'note_id': note_id},
        UpdateExpression='SET title = :t, content = :c, timestamp = :ts',
        ExpressionAttributeValues={
            ':t': data['title'],
            ':c': data['content'],
            ':ts': datetime.utcnow().isoformat()
        },
        ReturnValues='ALL_NEW'
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Note updated', 'item': response['Attributes']})
    }