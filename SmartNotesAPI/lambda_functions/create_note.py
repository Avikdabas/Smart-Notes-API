import boto3
import uuid
import json
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SmartNotes')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    note_id = str(uuid.uuid4())
    item = {
        'note_id': note_id,
        'title': data['title'],
        'content': data['content'],
        'timestamp': datetime.utcnow().isoformat()
    }
    table.put_item(Item=item)
    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Note created', 'note_id': note_id})
    }