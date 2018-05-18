def gitUtil = new com.guavus.jenkins.GitUtil()

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
          gitUtil.guavusCopyright();
        }
      }
    }
  }
}
