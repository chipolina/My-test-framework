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
                sh "docker run -v /Users/denis/.jenkins/workspace/final_pipeline/allure-results:/app/allure-results tests"
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
      	   results: [[path: '/Users/denis/.jenkins/workspace/final_pipeline/allure-results']]
    	   ])
  	        }
         }
    }
}
