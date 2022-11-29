pipeline {
  agent any
  stages {
    stage('Install boto3') {
      steps {
        sh 'python3 -m pip install --user boto3'
      }
    }
    stage('Run Py Script') {
      steps {
        sh 'python3 task2.py'
      }
    }
  }
}
