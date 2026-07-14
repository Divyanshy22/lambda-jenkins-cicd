pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/opt/openjdk@21/bin:/opt/homebrew/bin:/usr/local/bin:${env.PATH}"
        FUNCTION_NAME = 'hello-world-jenkins'
        AWS_REGION = 'us-east-1'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Package') {
            steps {
                sh 'zip function.zip lambda_function.py'
            }
        }

        stage('Deploy to Lambda') {
            steps {
                withCredentials([
                    string(credentialsId: 'access-key-id', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'secret-access-key', variable: 'AWS_SECRET_ACCESS_KEY')
                ]) {
                    sh '''
                        aws lambda update-function-code \
                          --function-name $FUNCTION_NAME \
                          --zip-file fileb://function.zip \
                          --region $AWS_REGION
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Lambda function updated successfully via Jenkins.'
        }
        failure {
            echo 'Pipeline failed — check console output above.'
        }
    }
}
