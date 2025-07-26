# Smart Notes API

A simple cloud-native notes API using AWS Lambda, DynamoDB, and API Gateway.

## Features
- Create, Read, Update, Delete (CRUD) notes
- Python-based AWS Lambda functions
- DynamoDB for storage
- API Gateway for routing

## Setup Instructions
1. Create a DynamoDB table named `SmartNotes` with `note_id` as the primary key.
2. Deploy the Python Lambda functions using AWS Console or SAM CLI.
3. Use the OpenAPI spec to configure API Gateway.
4. Connect each endpoint to its respective Lambda function.

## Endpoints
- POST `/notes` → create_note.py
- GET `/notes/{note_id}` → read_note.py
- PUT `/notes/{note_id}` → update_note.py
- DELETE `/notes/{note_id}` → delete_note.py
