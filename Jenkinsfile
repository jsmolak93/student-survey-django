// Group: SWE645-Django
// File: Jenkinsfile
// Description: CI/CD pipeline for Django Docker image build/push and Kubernetes deployment

pipeline {
    agent any

    environment {
        DOCKERHUB_PASS  = credentials('docker_credentials')
        BUILD_TIMESTAMP = new Date().format("yyyyMMdd-HHmmss", TimeZone.getTimeZone("UTC"))
        KUBE_NAMESPACE  = 'swe645'
    }

    stages {
        stage('Install dependencies & run tests') {
        steps {
            checkout scm
            sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
            python3 manage.py test
            '''
        }
        }

        stage('Build Docker image') {
        steps {
            sh """
            echo "${DOCKERHUB_PASS_PSW}" | \
                docker login -u "${DOCKERHUB_PASS_USR}" --password-stdin
            """
            sh """
            docker build \
                -t jsmolak93/swe645:latest-${BUILD_TIMESTAMP} .
            """
        }
        }

        stage('Push image to Docker Hub') {
        steps {
            sh "docker push jsmolak93/swe645:latest-${BUILD_TIMESTAMP}"
        }
        }

        stage('Run Database Migrations') {
            steps {
                withCredentials([file(credentialsId: KUBECONFIG_FILE,
                                        variable: 'KUBECONFIG')]) {
                    sh """
                        # Launch one-off Job to run migrations; ignore errors so deploy always runs
                        kubectl create job django-migrate-${BUILD_TIMESTAMP} \
                            --image=jsmolak93/swe645:latest-${BUILD_TIMESTAMP} \
                            --namespace=${KUBE_NAMESPACE} \
                            -- python3 manage.py migrate 
                        """
                }
            }
        }

        stage('Deploy to Kubernetes') {
        steps {
            withCredentials([file(credentialsId: 'kubeConfig', variable: 'KUBECONFIG')]) {
            sh """
                kubectl set image deployment/deployment-student-survey \
                survey=jsmolak93/swe645:latest-${BUILD_TIMESTAMP} \
                -n ${KUBE_NAMESPACE} 
                kubectl rollout status deployment/deployment-student-survey -n ${KUBE_NAMESPACE}
            """
            }
        }
        }
    }
}
