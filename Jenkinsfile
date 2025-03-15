pipeline {
    agent { label 'api-test-agent' }
    environment {
        VENV_PATH = "venv"
    }
    stages {
        stage('Run API Tests in Parallel') {
            parallel {
                stage('Test Env 1') {
                    agent { docker { image 'python:3.12' } }
                    steps {
                        echo 'Pull Repository'
                        checkout scm
                        echo 'Install python library'
                        sh '''
                            python3 -m venv ${VENV_PATH}
                            source ${VENV_PATH}/bin/activate
                            pip install -r requirements.txt
                           '''
                        echo 'Run Test'
                        sh '''
                        source ${VENV_PATH}/bin/activate
                        pytest MarketstackAPITest_Proj/Testcases/test_historical_api.py \
                        --alluredir=reports/allure_results
                        '''
                    }
                }
                stage('Test Env 2') {
                    agent { docker { image 'python:3.12' } }
                    steps {
                        echo 'Pull Repository'
                        checkout scm
                        echo 'Install python library'
                        sh '''
                            python3 -m venv ${VENV_PATH}
                            source ${VENV_PATH}/bin/activate
                            pip install -r requirements.txt
                           '''
                        echo 'Run Test'
                        sh '''
                        source ${VENV_PATH}/bin/activate
                        pytest MarketstackAPITest_Proj/Testcases/test_historical_api.py \
                        --alluredir=reports/allure_results
                        '''
                    }
                }

            }
        }
    },
    stage('Publish Allure Report') {
        steps {
        allure includeProperties: false, jdk: '', results: [[path: 'reports/allure_results']]
    }
}

}









