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
				sh '''
					python3 -m venv venv
					. venv/bin/activate
					pip install flake8
					flake8 python/ --max-line-length=120 || true
				'''
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
					export TF_CLI_CONFIG_FILE="${WORKSPACE}/terraform/terraformrc"
					terraform init -no-color
					terraform apply -auto-approve -no-color
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
