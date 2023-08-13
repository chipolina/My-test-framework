pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("tests:${env.BUILD_ID}", "-f Dockerfile .")
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def container = docker.image("tests:${env.BUILD_ID}")
                    container.inside("-v ${WORKSPACE}/allure-results:/app/allure-results") {
                        sh "/Users/denis/PycharmProjects/Otus_final/venv/bin/pytest -m api"  // Replace with the actual path to pytest
                    }
                }
            }
        }
    }
}
