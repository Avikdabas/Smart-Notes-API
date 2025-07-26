import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SmartNotes')

def lambda_handler(event, context):
    note_id = event['pathParameters']['note_id']
    table.delete_item(Key={'note_id': note_id})
    return {'statusCode': 200, 'body': json.dumps({'message': 'Note deleted'})}