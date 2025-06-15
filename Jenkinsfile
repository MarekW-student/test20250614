pipeline {
	agent any
	
	triggers {
		cron('H/2 * * * *')
	}
	stages {
		stage('Say hello') {
			steps {
				echo 'hello TAS4'
			}
		}
	}
}
