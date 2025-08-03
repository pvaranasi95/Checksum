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

        stage('Generate checksums and save to file') {
            steps {
                powershell """
                    \$hash1 = (Get-FileHash -Path '${params.CheckSum1_Dir_Path}' -Algorithm SHA256).Hash
                    \$hash2 = (Get-FileHash -Path '${params.CheckSum2_Dir_Path}' -Algorithm SHA256).Hash

                    'hash1=' + \$hash1 | Out-File -FilePath 'checksums.txt' -Encoding utf8
                    'hash2=' + \$hash2 | Out-File -FilePath 'checksums.txt' -Append -Encoding utf8
                """
            }
        }

        stage('Compare checksums') {
            steps {
                script {
                    def content = readFile('checksums.txt').readLines()
                    def h1 = content.find { it.startsWith('hash1=') }?.split('=')[1]?.trim()
                    def h2 = content.find { it.startsWith('hash2=') }?.split('=')[1]?.trim()

                    echo "Hash1: ${h1}"
                    echo "Hash2: ${h2}"

                    if (h1 && h2 && h1 == h2) {
                        echo "✅ Checksums match"
                    } else {
                        echo "❌ Checksums do NOT match"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Archive checksum file') {
            steps {
                archiveArtifacts artifacts: 'checksums.txt', onlyIfSuccessful: false
            }
        }
    }
}
