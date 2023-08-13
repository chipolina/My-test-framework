pipeline {
    agent any
    environment {
        DOCKER_PATH = '/Applications/Docker.app/Contents/Resources/bin'
        PATH = "${DOCKER_PATH}:${PATH}"
    }
    stages {
        stage("Build image") {
            steps {
                catchError {
                    script {
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
        stage('Start selenoid') {
            steps {
                catchError {
                    sh "/Users/denis/PycharmProjects/Otus_final/drivers/cm selenoid start"
                            }
            }
        }
        stage('Run tests') {
            steps {
                catchError {
                    sh "docker run --rm --network=${network} tests sh -c '/usr/local/bin/pytest -n 4 -m api --alluredir=/app/allure-results'"
                    }
                    sh "/usr/local/bin/allure generate /app/allure-results -o /app/allure-report"
            }
        }
        stage('Reports') {
        steps {
            archiveArtifacts artifacts: '**/allure-report/**', allowEmptyArchive: true
         }
    }
}
}