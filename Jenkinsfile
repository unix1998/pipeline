@Library('jenkins-pipeline-shared-lib-sample') _
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                SampleDSL()
                
            }
        }
    }
}
