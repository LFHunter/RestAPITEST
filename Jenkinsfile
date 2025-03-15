pipeline {
    agent { label 'api-test-agent' }
    environment {
        VENV_PATH = "~/venv"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv ${VENV_PATH}
                source ${VENV_PATH}/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            parallel {
                stage('Unit Test') {
                    steps {
                        sh '''
                        source ${VENV_PATH}/bin/activate
                        pytest MarketstackAPITest_Proj/Testcases/test_historical_api.py \
                        --junitxml=report_unit.xml
                        '''
                    }
                }
                stage('Integration Test') {
                    steps {
                        sh '''
                        source ${VENV_PATH}/bin/activate
                        pytest MarketstackAPITest_Proj/Testcases/test_historical_api.py \
                        --junitxml=report_unit.xml
                        '''
                    }
                }
            }
        }


    }
    post {
        always {
            archiveArtifacts artifacts: '**/*.xml', fingerprint: true
            junit '**/*.xml'
        }
    }
}