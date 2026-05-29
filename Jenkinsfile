pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/piyuusha/VehicleDamageDetection-awdl.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Testing Vehicle Damage Detection Application'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Docker image build stage'
            }
        }
    }
}