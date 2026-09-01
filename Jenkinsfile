pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install Playwright') {
            steps {
                sh '''
                    . .venv/bin/activate
                    playwright install chromium
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest
                '''
            }
        }
    }

    post {
        always {
            junit 'reports/junit.xml'

            archiveArtifacts artifacts: 'reports/**',
                allowEmptyArchive: true

            archiveArtifacts artifacts: 'allure-results/**',
                allowEmptyArchive: true
        }
    }
}