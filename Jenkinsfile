pipeline {
    agent any
    stages {

        stage('Deploy'){
        	steps {
		sh "apt-get update"
		sh "apt-get install docker-compose-plugin"
                sh "docker build ."
        	}
        }      
        stage('OWASP DependencyCheck') {
			steps {
				script {
				docker.image("3x03/web").withRun("","sleep infinity"){c->
					sh "docker exec -t ${c.id} pip freeze > requirements.txt"
				}
			}
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
