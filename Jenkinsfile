pipeline {

    agent any

     environment {
       PATH = "C:\\Program Files\\nodejs;C:\\Users\\shubh\\AppData\\Roaming\\npm;${env.PATH}"

        ANDROID_HOME = "C:\\Users\\shubh\\AppData\\Local\\Android\\Sdk"
        ANDROID_SDK_ROOT = "C:\\Users\\shubh\\AppData\\Local\\Android\\Sdk"
        ANDROID_AVD_HOME = "C:\\Users\\shubh\\.android\\avd"
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

stage('Start Android Emulator') {

    steps {

        bat '''
            echo ===== Android Environment =====

            set ANDROID_HOME=C:\\Users\\shubh\\AppData\\Local\\Android\\Sdk
            set ANDROID_SDK_ROOT=C:\\Users\\shubh\\AppData\\Local\\Android\\Sdk
            set ANDROID_AVD_HOME=C:\\Users\\shubh\\.android\\avd
            set ANDROID_USER_HOME=C:\\Users\\shubh\\.android

            echo ANDROID_HOME=%ANDROID_HOME%
            echo ANDROID_SDK_ROOT=%ANDROID_SDK_ROOT%
            echo ANDROID_AVD_HOME=%ANDROID_AVD_HOME%
            echo ANDROID_USER_HOME=%ANDROID_USER_HOME%

            echo.
            echo ===== Starting ADB =====

            adb start-server

            echo.
            echo ===== Starting Android Emulator =====

            start "Android Emulator" /B emulator.exe ^
                -avd Pixel_8 ^
                -no-window ^
                -no-audio ^
                -no-boot-anim

            echo Emulator process started.

            timeout /t 10 /nobreak

            echo.
            echo ===== Emulator Processes =====

            tasklist | findstr /I "emulator"

            echo.
            echo ===== ADB Devices =====

            adb devices

            echo.
            echo ===== ADB State =====

            adb get-state
        '''
    }
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