pipeline {
    agent any

    stages {
        stage('Checking source file existence') {
            steps {
                powershell '''
                    $folderpath = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Adressbook.zip"
                    if (Test-Path $folderpath -PathType Leaf) {
                        Write-Host "File exists."
                    } else {
                        Write-Host "File does not exist."
                    }
                '''
            }
        }
    }
}
