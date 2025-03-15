pipeline {
    agent any
    environment {
        PYTHON_VERSION = '3.12'
        VENV_PATH = 'venv'
    }

    stages {
        stage('Checkout Repository') {
            steps {
                echo '===== Pulling Repository ====='
                checkout([$class: 'GitSCM',
                ranches: [[name: '*/main']],
                userRemoteConfigs: [[url: 'https://github.com/LFHunter/RestAPITEST.git']]])
            }
        }
        stage('Setup and Run Tests') {
            parallel {
                stage('Test 1') {
                    agent { docker { image "python:${env.PYTHON_VERSION }"
                    } }
                    steps {
                        // sh 'apt-get update && apt-get install -y git'
                        // echo '=====Pull Repository====='
                        // echo "${env.WORKSPACE}"
                        // dir("${env.WORKSPACE}") {
                        // git branch: 'main', url: 'https://github.com/LFHunter/RestAPITEST.git'
                        // }
                        script {
                            setupPyEnv(${ env.VENV_PATH })
                            runPytest()
                        }
                    }
                }
                stage('Test 2') {
                    agent { docker { image "python:${env.PYTHON_VERSION }"
                    args '--entrypoint /bin/sh'} }
                    steps {
                        // sh 'apt-get update && apt-get install -y git'
                        // echo '=====Pull Repository====='
                        // echo "${env.WORKSPACE}"
                        // dir("${env.WORKSPACE}") {
                        // git branch: 'main', url: 'https://github.com/LFHunter/RestAPITEST.git'
                        // }
                        script {
                            setupPyEnv(${ env.VENV_PATH })
                            runPytest()
                        }
                    }
                }
                stage('Test 3') {
                    agent { docker { image "python:${env.PYTHON_VERSION }"
                    args '--entrypoint /bin/sh'} }
                    steps {
                        // sh 'apt-get update && apt-get install -y git'
                        // echo '=====Pull Repository====='
                        // echo "${env.WORKSPACE}"
                        // dir("${env.WORKSPACE}") {
                        // git branch: 'main', url: 'https://github.com/LFHunter/RestAPITEST.git'
                        // }
                        script {
                            setupPyEnv(${ env.VENV_PATH })
                            runPytest()
                        }
                    }
                }
            }
        }
        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'reports/allure_results']]
            }
        }
    }

    post {
        always {
            echo 'All tests completed.'
        }
    }
}

def setupPyEnv(venvpath) {
    sh """
      echo ====Setting up Env =====
      python3 -m venv ${venvpath}
      source ${venvpath}/bin/activate
      mkdir -p reports/allure_results
      pip3 install -r requirements.txt
    """
}
def runPytest() {
    sh '''
           mkdir -p reports/allure_results
           pytest MarketstackAPITest_Proj/Testcases/test_historical_api.py \
           --alluredir=reports/allure_results
    '''
}
