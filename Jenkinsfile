pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['dev', 'staging', 'prod'],
            description: 'Which environment to deploy to'
        )
    }

    environment {
        PATH = "/opt/homebrew/opt/openjdk@21/bin:/opt/homebrew/bin:/usr/local/bin:${env.PATH}"
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

        stage('Determine Function Name') {
            steps {
                script {
                    if (params.ENVIRONMENT == 'prod') {
                        env.FUNCTION_NAME = 'hello-world-jenkins'
                    } else {
                        env.FUNCTION_NAME = "hello-world-jenkins-${params.ENVIRONMENT}"
                    }
                    echo "Deploying to function: ${env.FUNCTION_NAME}"
                }
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
            echo "Lambda function ${env.FUNCTION_NAME} updated successfully via Jenkins."
        }
        failure {
            echo 'Pipeline failed — check console output above.'
        }
    }
}
