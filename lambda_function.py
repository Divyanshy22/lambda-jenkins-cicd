def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello World deployed via Jenkins CI/CD pipeline!'
    }
