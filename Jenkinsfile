pipeline {
  agent any
  stages {
    stage('Print var from lib') {
      steps {
        script {
          sayHello('Alain')
          println("Commit : ${getCommit()}")
          println("BRANCH_NAME : ${BRANCH_NAME}")
          println("GIT_TAG_NAME : ${gitTagName( getCommit() )}")
        }
      }
    }
    stage('Call Groovy code'){
      steps {
        script {
          println "not doing anything"
        }
      }
    }
  }
}
