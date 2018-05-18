pipeline {
  agent any
  stages {
    stage('Print var from lib') {
      steps {
        script {
          sayHello('Alain')
        }
      }
    }
    stage('Call Groovy code'){
      steps {
        script {
          com.guavus.jenkins.gitUtil.guavusCopyright();
        }
      }
    }
  }
}
