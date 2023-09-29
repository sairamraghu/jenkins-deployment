import json

def Jenkins-Lambda(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Middleware!')
    }
