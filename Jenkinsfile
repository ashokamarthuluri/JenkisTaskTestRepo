pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
        python -m pip install --user boto3
      }
      steps {
        sh 'python3 task2.py'
      }
    }
  }
}
