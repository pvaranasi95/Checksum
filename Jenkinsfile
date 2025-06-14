pipeline {
    agent any
stages {
        stage('Checking source folder existence') {
            steps {
              powershell'''
              $folderpath=C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Adressbook.zip
              if (test-path $folderpath) {
              Write-Host "Folder exists."
              } else {
              Write-Host "Folder does not exist."
              }
              '''
              }
            }
            }
        }            
