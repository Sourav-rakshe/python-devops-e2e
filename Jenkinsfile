pipeline {
    agent any
    environment {
        DOCKER_USER = "sourav-rakshe"
        IMAGE_NAME  = "${DOCKER_USER}/python-devops-app"
        BUILD_TAG   = "${BUILD_NUMBER}"
    }
    stages {
        stage('1. Checkout SCM') {
            steps { checkout scm }
        }
        stage('2. Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_TAG} ."
                sh "docker tag ${IMAGE_NAME}:${BUILD_TAG} ${IMAGE_NAME}:latest"
            }
        }
        stage('3. Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo "$PASS" | docker login -u "$USER" --password-stdin'
                    sh "docker push ${IMAGE_NAME}:${BUILD_TAG}"
                    sh "docker push ${IMAGE_NAME}:latest"
                }
            }
        }
        stage('4. Deploy to Kubernetes') {
            steps {
                sh "kubectl apply -f k8s/"
                sh "kubectl set image deployment/python-app-deployment python-container=${IMAGE_NAME}:${BUILD_TAG}"
            }
        }
        stage('5. Verify Rollout') {
            steps {
                sh "kubectl rollout status deployment/python-app-deployment --timeout=90s"
            }
        }
    }
}
