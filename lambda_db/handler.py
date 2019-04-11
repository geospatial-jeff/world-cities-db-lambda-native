import json
from db import Database

def spatial_query(event, context):

    data = json.loads(event['body'])

    with Database.load(read_only=True, deployed=True) as db:
        response = db.spatial_query(data['geoj'])
        return {
            'statusCode': 200,
            'body': json.dumps(response),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            }
        }