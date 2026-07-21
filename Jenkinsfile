@Library('shared-library') _

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
        PATH = "/opt/homebrew/bin:/usr/local/bin:${env.PATH}"
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
                    env.FUNCTION_NAME = (params.ENVIRONMENT == 'prod')
                        ? 'hello-world-jenkins'
                        : "hello-world-jenkins-${params.ENVIRONMENT}"
                    echo "Deploying to function: ${env.FUNCTION_NAME}"
                }
            }
        }

        stage('Deploy to Lambda') {
            steps {
                deployToLambda(
                    functionName: env.FUNCTION_NAME,
                    region: env.AWS_REGION,
                    zipFile: 'function.zip'
                )
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
