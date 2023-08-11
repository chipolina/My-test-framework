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

        stage('Pull browser') {
            steps {
                catchError {
                    script {
                        docker.image('selenoid/chrome:114.0')
                    }
                }
            }
        }

        stage('Start selenoid') {
            steps {
                catchError {
                    sh "/Users/denis/Desktop/drivers/cm selenoid start"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def container = docker.image("tests:${env.BUILD_ID}")
                    container.inside("-v ${WORKSPACE}/allure-results:/app/allure-results") {
                        sh "pytest -m api"
                    }
                }
            }
        }

        /*
        stage('Reports') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
        */

        stage('Stop selenoid') {
            steps {
                catchError {
                    sh "/Users/denis/Desktop/drivers/cm selenoid stop"
                }
            }
        }
    }
}
