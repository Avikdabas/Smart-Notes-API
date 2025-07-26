import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SmartNotes')

def lambda_handler(event, context):
    note_id = event['pathParameters']['note_id']
    response = table.get_item(Key={'note_id': note_id})
    item = response.get('Item')
    if not item:
        return {'statusCode': 404, 'body': json.dumps({'error': 'Note not found'})}
    return {'statusCode': 200, 'body': json.dumps(item)}