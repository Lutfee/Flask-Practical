pipeline {
    agent any
    stages {

        stage('Deploy'){
        	steps {
		sh "apt-get update"
		sh "apt-get install docker-compose-plugin"
		sh "docker compose up"
                sh "docker build ."
		sh "docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest"	
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
			sh "docker stop sonarqube"
		}
	}
}
