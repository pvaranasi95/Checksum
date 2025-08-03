pipeline {
    agent any

    parameters {
        string(name: 'CheckSum1_Dir_Path', description: 'Path to the checksum file1')
        string(name: 'CheckSum2_Dir_Path', description: 'Path to the checksum file2')
    }

    environment {
        CHECKSUM1 = ''
        CHECKSUM2 = ''
    }

    stages {
        stage('Checking file1 existence') {
            steps {
                powershell """
                    \$folderpath1 = '${params.CheckSum1_Dir_Path}'
                    if (Test-Path \$folderpath1 -PathType Leaf) {
                        Write-Host "\$folderpath1 exists."
                    } else {
                        Write-Host "\$folderpath1 does not exist."
                        exit 1
                    }
                """
            }
        }
        stage('Checking file2 existence') {
            steps {
                powershell """
                    \$folderpath2 = '${params.CheckSum2_Dir_Path}'
                    if (Test-Path \$folderpath2 -PathType Leaf) {
                        Write-Host "\$folderpath2 exists."
                    } else {
                        Write-Host "\$folderpath2 does not exist."
                        exit 1
                    }
                """
            }
        } 
        stage('Checksum of file1') {
            steps {
                powershell """
                    \$hash = Get-FileHash -Path '${params.CheckSum1_Dir_Path}' -Algorithm SHA256
                    Write-Host "Checksum1: \$($hash.Hash)"
                    echo "CHECKSUM1=\$($hash.Hash)" | Out-File -Append -FilePath \$env:GITHUB_ENV
                """
            }
        }
        stage('Checksum of file2') {
            steps {
                powershell """
                    \$hash = Get-FileHash -Path '${params.CheckSum2_Dir_Path}' -Algorithm SHA256
                    Write-Host "Checksum2: \$($hash.Hash)"
                    echo "CHECKSUM2=\$($hash.Hash)" | Out-File -Append -FilePath \$env:GITHUB_ENV
                """
            }
        }
        stage('Compare checksums') {
            steps {
                script {
                    if (env.CHECKSUM1 == env.CHECKSUM2) {
                        echo "✅ Checksums match"
                    } else {
                        echo "❌ Checksums do NOT match"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
    }
}
