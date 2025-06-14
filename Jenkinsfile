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
                    \$folderpath = '${params.CheckSum1_Dir_Path}'
                    if (Test-Path \$folderpath -PathType Leaf) {
                        Write-Host "\$folderpath exists."
                    } else {
                        Write-Host "\$folderpath does not exist."
                    }
                """
            }
        }
        stage('Checking file2 existence') {
            steps {
                powershell """
                    \$folderpath = '${params.CheckSum2_Dir_Path}'
                    if (Test-Path \$folderpath -PathType Leaf) {
                        Write-Host "\$folderpath exists."
                    } else {
                        Write-Host "\$folderpath does not exist."
                    }
                """
            }
        } 
      stage('Compare checksums') {
          steps {
        powershell """
            \$file1 = '${params.CheckSum1_Dir_Path}'
            \$file2 = '${params.CheckSum2_Dir_Path}'

            \$hash1 = (Get-FileHash -Path \$file1 -Algorithm SHA256).Hash
            \$hash2 = (Get-FileHash -Path \$file2 -Algorithm SHA256).Hash

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
