pipeline {
    agent any

    stages {

        stage('Verify Environment') {
            steps {
                echo 'Checking Python and Docker environment...'
                bat 'python --version'
                bat 'docker --version'
            }
        }

        stage('Python Syntax Check') {
            steps {
                echo 'Checking Python source code...'
                bat 'python -m py_compile ci\\ai_triage.py'
                bat 'python -m py_compile web\\app.py'
            }
        }

        stage('Bandit Security Scan') {
            steps {
                echo 'Running Bandit security scan...'
                bat 'python -m bandit -r ci web -ll'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t devsecops-ai-web:%BUILD_NUMBER% web'
            }
        }

        stage('Docker Compose Validation') {
            steps {
                echo 'Validating docker-compose configuration...'
                bat 'docker-compose config'
            }
        }
    }

    post {
        success {
            echo 'DevSecOps pipeline completed successfully.'
        }

        failure {
            echo 'DevSecOps pipeline failed. Check the stage logs.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
