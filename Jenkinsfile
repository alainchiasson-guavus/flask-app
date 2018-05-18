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
          def gitUtil = new com.guavus.jenkins.GitUtil()

          gitUtil.guavusCopyright();
        }
      }
    }
  }
}
