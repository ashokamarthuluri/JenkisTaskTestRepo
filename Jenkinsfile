pipeline {
  agent any
  stages {
    stage('Install boto3') {
      steps {
        sh 'python -m pip install --user boto3'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 task2.py'
      }
    }
  }
}
