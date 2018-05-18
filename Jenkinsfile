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
          println com.guavus.jenkins.GitUtil.guavusCopyright()
        }
      }
    }
  }
}
