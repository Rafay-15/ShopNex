pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "rafay15/assignment3:latest"
        IMAGE_NAME = "myapp"
        DOCKER_REGISTRY = "docker.io" 
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: '4c34f89c-2bb0-4964-a6b4-7c7023fd8d3f', url: 'https://github.com/Rafay-15/ShopNex.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withDockerRegistry([ credentialsId: 'dockerhub-credentials-id', url: '' ]) {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Run Tests in Docker') {
            steps {
                script {
                  
                    sh '''
                    docker run -d --name myapp-container -p 3000:3000 $DOCKER_IMAGE

                    sleep 10

                    docker exec myapp-container python /app/src/test_script.py

                    TEST_RESULT=$?

                    docker stop myapp-container
                    docker rm myapp-container

                    exit $TEST_RESULT
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    sh 'docker system prune -f'
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
        success {
            echo 'Tests passed and pipeline completed successfully!'
        }
        failure {
            echo 'Tests failed. Please check the logs for details.'
        }
    }
}
