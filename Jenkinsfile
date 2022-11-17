pipeline {
    agent any
    stages {

        stage('Deploy'){
        	steps {
                sh "docker build ."
		sh "docker pull sonarqube"
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
		}
	}
}
