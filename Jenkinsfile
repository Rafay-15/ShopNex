pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "rafay15/assignment3:latest"
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

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry([ credentialsId: 'dockerhub-credentials-id', url: '' ]) {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }
    }
}
