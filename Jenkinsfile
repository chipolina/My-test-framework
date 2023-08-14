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
        stage('Run tests') {
            steps {
                catchError {
                    sh "docker volume create allure-results" // Create a Docker volume for Allure results
                    sh "docker run --rm --network=${network} -v allure-results:/app/allure-results tests sh -c '/usr/local/bin/pytest -n 4 -m api --alluredir=/app/allure-results'"
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                catchError {
                    script {
                        def allureResultsDir = "/app/allure-results"
                        def allureReportDir = "/app/allure-report"

                        docker.image('your-allure-image').inside("-v ${allureResultsDir}:${allureResultsDir}", "-v ${allureReportDir}:${allureReportDir}") {
                            sh "/opt/homebrew/bin/allure generate ${allureResultsDir} -o ${allureReportDir}"
                        }
                    }
                }
            }
        }


        stage('Reports') {
            steps {
                sh 'mv /tmp/allure-report /app/' // Move the generated report back to /app directory
                archiveArtifacts artifacts: '/app/allure-report/**', allowEmptyArchive: true
            }
        }
    }
}
