// nodes which handles the workflow
def node_list = []
def docker_node_list = []
def yesBuild = true
def customImage = null
def imageNames = []
def reponame = null

// retrieve build causes
println("INFO: build cause is " +causes.type)

pipeline {
  agent none
  options {
    disableConcurrentBuilds()
    timeout(time: 10, unit: 'MINUTES')
    timestamps()
  }
  stages {
    // only branch_event master branch merge from PR 
    stage('bpkg publish'){
      steps{
        python3.10 -m pytest test_*
        }
      }
    }
  }
}
