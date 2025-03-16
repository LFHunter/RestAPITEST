pipeline {
    agent any

    environment {
        REPO_URL = "https://github.com/LFHunter/RestAPITEST.git"
        IMAGE_NAME = "api-test-env"
        CONTAINER_REPORTS = "allure-reports"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                script {
                    deleteDir()
                }
            }
        }

        stage('Checkout Code') {
            steps {
                script {
                    git branch: 'main', url: REPO_URL
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run API Tests in Parallel') {
            parallel {
                stage('Test Env 1') {
                    steps {
                        sh 'pwd'
                        script {
                            runDockerTest("env1")
                        }
                    }
                }
                stage('Test Env 2') {
                    steps {
                        script {
                            runDockerTest("env2")
                        }
                    }
                }
                stage('Test Env 3') {
                    steps {
                        script {
                            runDockerTest("env3")
                        }
                    }
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    sh "allure generate ${CONTAINER_REPORTS} -o allure-report --clean"
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-report']]
            }
        }
    }
}

def runDockerTest(envName) {
    sh """
        echo "Running tests in ${envName}..."
        mkdir -p ${CONTAINER_REPORTS}/${envName}
        docker run --rm \
            -v ${pwd}:/app \
            -v ${pwd}/${CONTAINER_REPORTS}/${envName}:/app/reports \
            ${IMAGE_NAME}

        echo "Tests in ${envName} completed."
    """
}
