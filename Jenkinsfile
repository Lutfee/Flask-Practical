pipeline {
    agent any
    stages {

        stage('Deploy'){
        	steps {
                sh "docker build flask ."
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
