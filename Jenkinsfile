pipeline {
    agent any
    environment {
        DOCKER_PATH = '/Applications/Docker.app/Contents/Resources/bin'
    }
    stages {
        stage("Build image") {
            steps {
                catchError {
                    script {
                        sh "export PATH=$PATH:${DOCKER_PATH}"
                        docker.build("tests", "-f Dockerfile .")
                    }
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
        stage('Run tests') {
            steps {
                catchError {
                    sh "docker run --rm --network=${network} tests"
                }
            }
        }
    }
}
