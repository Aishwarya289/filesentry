pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "filesentry:latest"
    }

    stages {
        stage('Build') {
            steps {
                echo ' Building Docker image...'
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Test') {
            steps {
                echo ' Running unit tests with pytest...'
                sh 'docker run --rm $DOCKER_IMAGE pytest tests/ > test_results.txt'
                archiveArtifacts artifacts: 'test_results.txt', allowEmptyArchive: true
            }
        }

        stage('Code Quality') {
            steps {
                echo ' (Placeholder) Running SonarCloud or code quality tool...'
                // Replace with actual SonarCloud CLI command if configured
                sh 'echo "SonarCloud scan would run here."'
            }
        }

        stage('Security Scan') {
            steps {
                echo ' Running Bandit security scan...'
                sh 'pip install bandit'
                sh 'bandit -r filesentry > bandit_report.txt'
                archiveArtifacts artifacts: 'bandit_report.txt', allowEmptyArchive: true
            }
        }

        stage('Deploy') {
            steps {
                echo ' Running container for snapshot creation...'
                sh 'mkdir -p sample_dir && echo "test" > sample_dir/test.txt'
                sh 'docker run --rm -v "$PWD/sample_dir:/app/sample_dir" $DOCKER_IMAGE python main.py sample_dir'
            }
        }
    }
}
