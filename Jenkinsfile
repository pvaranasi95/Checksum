pipeline {
    agent any

    parameters {
        string(name: 'CheckSum1_Dir_Path', description: 'Path to the first file')
        string(name: 'CheckSum2_Dir_Path', description: 'Path to the second file')
    }

    stages {
        stage('Check file existence') {
            steps {
                powershell """
                    if (-Not (Test-Path '${params.CheckSum1_Dir_Path}' -PathType Leaf)) {
                        Write-Host 'File1 not found'
                        exit 1
                    }
                    if (-Not (Test-Path '${params.CheckSum2_Dir_Path}' -PathType Leaf)) {
                        Write-Host 'File2 not found'
                        exit 1
                    }
                """
            }
        }

        stage('Generate checksum file') {
            steps {
                powershell """
                    \$hash1 = Get-FileHash -Path '${params.CheckSum1_Dir_Path}' -Algorithm SHA256
                    \$hash2 = Get-FileHash -Path '${params.CheckSum2_Dir_Path}' -Algorithm SHA256

                    "\$('${params.CheckSum1_Dir_Path}')=\$($hash1.Hash)" | Out-File -FilePath "checksums.txt" -Encoding utf8
                    "\$('${params.CheckSum2_Dir_Path}')=\$($hash2.Hash)" | Out-File -FilePath "checksums.txt" -Append -Encoding utf8
                """
            }
        }

        stage('Compare checksums') {
            steps {
                script {
                    def lines = readFile('checksums.txt').readLines()
                    def hash1 = lines[0].split('=')[1].trim()
                    def hash2 = lines[1].split('=')[1].trim()

                    echo "Checksum1: ${hash1}"
                    echo "Checksum2: ${hash2}"

                    if (hash1 == hash2) {
                        echo "✅ Checksums match"
                    } else {
                        echo "❌ Checksums do NOT match"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Archive checksums file') {
            steps {
                archiveArtifacts artifacts: 'checksums.txt', onlyIfSuccessful: false
            }
        }
    }
}
