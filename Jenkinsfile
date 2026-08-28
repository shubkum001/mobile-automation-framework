pipeline {

    agent any

     environment {
        PATH = "C:\\Program Files\\nodejs;C:\\Users\\shubh\\AppData\\Roaming\\npm;${env.PATH}"
    }

    parameters {



        choice(
            name: 'ENVIRONMENT',
            choices: ['qa', 'staging', 'prod'],
            description: 'Environment to execute tests against'
        )

        choice(
            name: 'PLATFORM',
            choices: ['android'],
            description: 'Platform to execute tests against'
        )

        choice(
            name: 'TEST_SUITE',
            choices: ['all', 'smoke', 'regression'],
            description: 'Test suite to execute'
        )
    }

    stages {

        stage('Checkout') {

            steps {
                checkout scm
            }
        }

        stage('Check Android Emulator') {

    steps {

        bat '''
            echo ===== Android Environment =====
            echo ANDROID_HOME=%ANDROID_HOME%
            echo ANDROID_SDK_ROOT=%ANDROID_SDK_ROOT%

            echo.
            echo ===== ADB =====
            where adb
            adb version

            echo.
            echo ===== Emulator =====
            where emulator
            emulator -list-avds

            echo.
            echo ===== Connected Devices =====
            adb devices
        '''
    }
}

        stage('Install Dependencies') {

            steps {

                bat 'python -m pip install --upgrade pip'

                bat 'pip install -r requirements.txt'
            }
        }

        stage('Start Appium') {

            steps {

                bat '''
                    start "Appium Server" /B appium.cmd
                '''

                timeout(time: 30, unit: 'SECONDS') {

                    waitUntil {

                        script {

                            def result = bat(
                                script: 'curl.exe -s http://127.0.0.1:4723/status',
                                returnStatus: true
                            )

                            return result == 0
                        }
                    }
                }
            }
        }

        stage('Run Tests') {

            steps {

                script {

                    def testCommand =
                        "pytest -v tests/ " +
                        "--env=${params.ENVIRONMENT} " +
                        "--platform=${params.PLATFORM} " +
                        "--alluredir=artifacts/allure-results"

                    if (params.TEST_SUITE == 'smoke') {

                        testCommand =
                            "pytest -v -m smoke tests/ " +
                            "--env=${params.ENVIRONMENT} " +
                            "--platform=${params.PLATFORM} " +
                            "--alluredir=artifacts/allure-results"

                    } else if (params.TEST_SUITE == 'regression') {

                        testCommand =
                            "pytest -v -m regression tests/ " +
                            "--env=${params.ENVIRONMENT} " +
                            "--platform=${params.PLATFORM} " +
                            "--alluredir=artifacts/allure-results"
                    }

                    bat testCommand
                }
            }
        }
    }

    post {

        always {

            archiveArtifacts(
                artifacts: 'artifacts/**/*',
                allowEmptyArchive: true
            )
        }

        success {

            echo 'Mobile automation execution completed successfully.'
        }

        failure {

            echo 'Mobile automation execution failed.'
        }
    }
}