pipeline {
    agent {
        node{label 'Windows1'}
    }
    tools {
        jdk 'JDK11'  //JDK17
        maven 'Maven'
    }

    stages {
        stage('Git checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/pvaranasi95/Python-test.git']])
            }
        }
        // stage('Sonar scan') {
        //     steps{
        //         script{
        //         bat 'cd C:\\Users\\pavan\\OneDrive\\Desktop\\sonarqube-10.4.1.88267\\sonar-scanner-6.1.0.4477-windows-x64\\bin'
        //        bat 'C:\\Users\\pavan\\OneDrive\\Desktop\\sonarqube-10.4.1.88267\\sonar-scanner-6.1.0.4477-windows-x64\\bin\\sonar-scanner.bat -D"sonar.projectKey=Jenkins-Sonarqube-Docker" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_3a7c14cc0030612ec004f1f554f6fa17fd9298a3"'
        //          }
        //     }
        // }
         stage('Docker Image') {
             steps{
                bat 'docker build -t pvaranasi/Py-Num-Guess:%BUILD_NUMBER% .'
             }
         }
         stage('Docker Push') {
             steps{
                 bat 'docker push pvaranasi/Py-Num-Guess:%BUILD_NUMBER%'
             }
         }
         stage('Container') {
             steps{
                 bat 'docker run -d -p 8088:80 --name Py-Num-Guess:%BUILD_NUMBER% Py-Num-Guess:%BUILD_NUMBER%'
    //         }
    //     }
    // }
    post{
        failure{
            emailext subject: "Build Failed for:%JOB_NAME% with %BUILD_NUMBER%",
                body: "Hi Your jenkins Build is failed for %JOB_NAME% with %BUILD_NUMBER%",
                to: "pavanvaranasi95@gmail.com",
                from: "pavanvaranasi95@gmail.com"
        }
        success{
            emailext subject: "Build success for %JOB_NAME% with %BUILD_NUMBER%",
                body: "Hi Your jenkins Build is success for %JOB_NAME% with %BUILD_NUMBER%",
                to: "pavanvaranasi95@gmail.com",
                from: "pavanvaranasi95@gmail.com"
        }
    }
}
}
