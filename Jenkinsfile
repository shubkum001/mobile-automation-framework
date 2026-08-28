pipeline {

    agent any

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

    environment {

        PATH = "C:\\Program Files\\nodejs;C:\\Users\\shubh\\AppData\\Roaming\\npm;C:\\Users\\shubh\\AppData\\Local\\Android\\Sdk\\platform-tools;C:\\Users\\shubh\\AppData\\Local\\Android\\Sdk\\emulator;${env.PATH}"

        ANDROID_HOME = "C:\\Users\\shubh\\AppData\\Local\\Android\\Sdk"

        ANDROID_SDK_ROOT = "C:\\Users\\shubh\\AppData\\Local\\Android\\Sdk"

        ANDROID_AVD_HOME = "C:\\Users\\shubh\\.android\\avd"

        AVD_NAME = "Pixel_8"
    }

    stages {

        stage('Checkout') {

            steps {

                checkout scm
            }
        }

        stage('Check Android Environment') {

            steps {

                bat '''
                    echo ===== Android Environment =====
                    echo ANDROID_HOME=%ANDROID_HOME%
                    echo ANDROID_SDK_ROOT=%ANDROID_SDK_ROOT%
                    echo ANDROID_AVD_HOME=%ANDROID_AVD_HOME%

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

        stage('Start Android Emulator') {

            steps {

                bat '''
                    echo ===== Starting Android Emulator =====

                    adb start-server

                    if not exist "%ANDROID_AVD_HOME%\\%AVD_NAME%.avd" (
                        echo ERROR: AVD not found:
                        echo %ANDROID_AVD_HOME%\\%AVD_NAME%.avd
                        exit /b 1
                    )

                    start "Android Emulator" /B emulator.exe ^
                        -avd %AVD_NAME% ^
                        -no-window ^
                        -no-audio ^
                        -no-boot-anim

                    echo Emulator process started.
                '''

                timeout(time: 3, unit: 'MINUTES') {

                    waitUntil {

                        script {

                            def result = bat(
                                script: '''
                                    adb devices | findstr /R /C:"emulator-5554.*device"
                                ''',
                                returnStatus: true
                            )

                            if (result == 0) {

                                echo "Android emulator is connected."

                                return true
                            }

                            echo "Waiting for Android emulator..."

                            sleep 5

                            return false
                        }
                    }
                }
            }
        }

        stage('Verify Android Device') {

            steps {

                bat '''
                    echo ===== Android Device =====

                    adb devices

                    echo.
                    echo ===== Device State =====

                    adb -s emulator-5554 get-state

                    echo.
                    echo ===== Boot Completed =====

                    adb -s emulator-5554 shell getprop sys.boot_completed
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
                    echo ===== Starting Appium =====

                    start "Appium Server" /B appium.cmd
                '''

                timeout(time: 30, unit: 'SECONDS') {

                    waitUntil {

                        script {

                            def result = bat(
                                script: 'curl.exe -s http://127.0.0.1:4723/status',
                                returnStatus: true
                            )

                            if (result == 0) {

                                echo "Appium server is ready."

                                return true
                            }

                            echo "Waiting for Appium server..."

                            sleep 2

                            return false
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