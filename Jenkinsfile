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
                    sh 'pwd'
                    sh 'ls -l'
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run API Tests in Parallel') {
            parallel {
                stage('Test Env 1') {
                    steps {
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
    def HOST_WORKSPACE = sh(script: "docker inspect jenkins | grep Source | awk -F'\"' '{print \$4}'", returnStdout: true).trim() + "/workspace/${JOB_NAME}"
    sh """
        echo "Running tests in ${envName}..."
        echo "HOST_WORKSPACE:${HOST_WORKSPACE},WORKSPACE:${WORKSPACE}"
        mkdir -p ${WORKSPACE}/${CONTAINER_REPORTS}/${envName}
        pwd
        ls -l
        chmod -R 777 ${WORKSPACE}
        docker run --rm \
            -v ${HOST_WORKSPACE}:/app \
            -v ${HOST_WORKSPACE}/${CONTAINER_REPORTS}/${envName}:/app/reports \
            ${IMAGE_NAME}

        echo "Tests in ${envName} completed."
    """
}
