pipeline {
    agent none

    stages {
        stage('Test DEB on Ubuntu') {
            agent {
                docker { 
                    image 'ubuntu:latest' 
                    args '-u root'
                }
            }
            steps {
                sh 'apt-get update'
                
                sh 'apt-get install -y ./packages/*.deb'
                
                sh 'echo "Running file-counter on Ubuntu:"'
                sh 'file-counter'
            }
        }

        stage('Test RPM on Fedora') {
            agent {
                docker { 
                    image 'fedora:latest'
                    args '-u root'
                }
            }
            steps {
                sh 'dnf install -y ./packages/*.rpm'

                sh 'echo "Running file-counter on Fedora:"'
                sh 'file-counter'
            }
        }
    }
}
