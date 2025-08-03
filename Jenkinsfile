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

        stage('Calculate checksums') {
            steps {
                script {
                    def hash1 = powershell(
                        script: "Get-FileHash -Path '${params.CheckSum1_Dir_Path}' -Algorithm SHA256 | Select-Object -ExpandProperty Hash",
                        returnStdout: true
                    ).trim()

                    def hash2 = powershell(
                        script: "Get-FileHash -Path '${params.CheckSum2_Dir_Path}' -Algorithm SHA256 | Select-Object -ExpandProperty Hash",
                        returnStdout: true
                    ).trim()

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
    }
}
