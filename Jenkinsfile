pipeline {
    agent any
    stages {

        stage('Deploy'){
        	steps {
		sh "apt-get update"
		sh "apt-get install docker-compose-plugin"
                sh "docker build -t flask-app ."
		sh "docker run  --name flask-app --publish 8000:8000 flask-app"
			
	
        	}
        }      
        stage('OWASP DependencyCheck') {
			steps {
				
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
			}
		}
    }   
    post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		
		}
	}
}
