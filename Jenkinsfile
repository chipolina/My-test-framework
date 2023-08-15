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
                    sh "docker run --name test_run --network=${network} tests"
             }
             }
             }
        stage('Take report results') {
            steps {
                catchError {
                    sh "docker cp test_run:app/allure-results ."
             }
             }
             }
        stage('Serve Allure Report') {
            steps {
                catchError {
                    sh "python3 -m http.server -d allure-results"
                }
            }
        }
        stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   properties: [],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: 'Users/denis/.jenkins/workspace/final_pipeline/allure-report']]
    	   ])
  	        }
         }
     stage('Stop selenoid') {
        steps {
            catchError {
                sh "/Users/denis/PycharmProjects/Otus_final/drivers/cm selenoid stop"
                sh "docker rm test_run"
        }
        }
     }
     }
}
