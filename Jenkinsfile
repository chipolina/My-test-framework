pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = "tests:${env.BUILD_ID}"
                    def dockerFile = "Dockerfile"

                    sh "docker build -t ${dockerImage} -f ${dockerFile} ."
                }
            }
        }

        stage('Install Requirements') {
            steps {
                script {
                    def dockerImage = "tests:${env.BUILD_ID}"

                    sh "docker run --rm -v ${WORKSPACE}:/app ${dockerImage} pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def dockerImage = "tests:${env.BUILD_ID}"

                    sh "docker run --rm -v ${WORKSPACE}:/app ${dockerImage} pytest -m api"
                }
            }
        }
    }
}
