pipeline {
	agent any
	stages {
		stage('Git Checkout') {
			steps {
				checkout scm
			}
		}
		stage('Code Lint') {
			steps {
				sh 'python3 -m pip install flake8'
				sh 'flake8 .'
			}
		}
		stage('Terraform fmt & validate') {
			steps {
				dir('terraform') {
					sh 'terraform fmt -recursive -check'
					sh 'terraform validate'
				}
			}
		}
		stage('Terraform Apply') {
			steps {
				dir('terraform') {
					// Если первый запуск, нужно инициализировать
					sh 'terraform init -no-color'
					sh 'terraform apply -auto-approve -no-color'
				}
			}
		}
		stage('Python Healthcheck') {
			steps {
				dir('python') {
					sh 'python3 healthcheck.py > health.json'
					sh 'python3 report.py'
				}
			}
		}
	}
	post {
		always {
			echo 'Pipeline execution finished.'
		}
	}
}
