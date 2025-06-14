pipeline {
    agent any

    parameters {
        string(name: 'CheckSum1_Dir_Path', description: 'Path to the checksum file1')
        string(name: 'CheckSum2_Dir_Path', description: 'Path to the checksum file2')
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
                    }
                """
            }
        } 
      stage('Checksum of folderpath1') {
          steps {
              powershell'''
              \$hash1 = Get-FileHash -Path "\$folderpath1" -Algorithm SHA256
              '''
          }
      }
          stage('Checksum of folderpath2') {
          steps {
              powershell'''
              \$hash2 = Get-FileHash -Path "\$folderpath2" -Algorithm SHA256
              '''
          }
      }

      stage('Compare checksums') {
          steps {
        powershell """
            Write-Host "Hash1: \$hash1"
            Write-Host "Hash2: \$hash2"

            if (\$hash1 -eq \$hash2) {
                Write-Host "✅ Checksums match"
            } else {
                Write-Host "❌ Checksums do NOT match"
            }
        """
    }
}

    }
}
