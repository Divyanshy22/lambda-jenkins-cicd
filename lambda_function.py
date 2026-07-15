def lambda_handlerX(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello World deployed via Jenkins CI/CD pipeline!'
    }
