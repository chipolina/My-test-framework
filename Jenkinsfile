pipeline {
  agent {
    dockerfile true
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
                sh "/Users/denis/Desktop/drivers/cm selenoid start"
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
     stage('Stop selenoid') {
        steps {
            catchError {
                sh "/Users/denis/Desktop/drivers/cm selenoid stop"
        }
        }
     }
     }
}
