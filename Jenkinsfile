pipeline {
    agent {
        label 'api-test-agent'
    }
    environment {
        VENV_PATH = "venv"
    }
    stages {
        stage('Run API Tests in Parallel') {
            steps {
                script {
                    parallel(
                        "Test Env 1" : {
                            node {
                                docker.image('python:3.12').inside {
                                    stage('Setup & Run Test Env 1') {
                                        echo 'Pull Repository'
                                        checkout scm
                                        echo 'Install python library'
                                        sh '''
                                            python3 -m venv "${env.VENV_PATH}"
                                            source "${env.VENV_PATH}/bin/activate"
                                            pip install -r requirements.txt
                                        '''
                                        echo 'Run Test'
                                        sh '''
                                            mkdir -p reports/allure_results
                                            source "${env.VENV_PATH}/bin/activate"
                                            pytest MarketstackAPITest_Proj/Testcases/test_historical_api.py \
                                            --alluredir=reports/allure_results
                                        '''
                                    }
                                }
                            }
                        },
                        "Test Env 2" : {
                            node {
                                docker.image('python:3.12').inside {
                                    stage('Setup & Run Test Env 2') {
                                        echo 'Pull Repository'
                                        checkout scm
                                        echo 'Install python library'
                                        sh '''
                                            python3 -m venv "${env.VENV_PATH}"
                                            source "${env.VENV_PATH}/bin/activate"
                                            pip install -r requirements.txt
                                        '''
                                        echo 'Run Test'
                                        sh '''
                                            mkdir -p reports/allure_results
                                            source "${env.VENV_PATH}/bin/activate"
                                            pytest MarketstackAPITest_Proj/Testcases/test_historical_api.py \
                                            --alluredir=reports/allure_results
                                        '''
                                    }
                                }
                            }
                        }
                    )
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
            echo 'Cleaning up virtual environment'
            sh 'rm -rf "${env.VENV_PATH}"'
        }
    }
}
