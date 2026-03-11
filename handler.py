import json

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print(f"New file uploaded: {key} in bucket {bucket}")
    return {
        'statusCode': 200,
        'body': json.dumps('S3 event processed successfully!')
    }