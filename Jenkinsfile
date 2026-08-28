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
            echo ===== Starting Android Emulator =====

            adb start-server

            start "Android Emulator" /B emulator.exe ^
                -avd Pixel_8 ^
                -no-window ^
                -no-audio ^
                -no-boot-anim

            echo Emulator process started.
        '''

        timeout(time: 180, unit: 'SECONDS') {

            waitUntil {

                script {

                    def result = bat(
                        script: '''
                            adb devices | findstr "emulator-5554.*device"
                        ''',
                        returnStatus: true
                    )

                    if (result == 0) {
                        echo "Android emulator is connected."
                        return true
                    }

                    echo "Waiting for Android emulator..."
                    return false
                }
            }
        }

        timeout(time: 180, unit: 'SECONDS') {

            waitUntil {

                script {

                    def result = bat(
                        script: '''
                            adb shell getprop sys.boot_completed | findstr "1"
                        ''',
                        returnStatus: true
                    )

                    if (result == 0) {
                        echo "Android emulator boot completed."
                        return true
                    }

                    echo "Waiting for Android boot completion..."
                    return false
                }
            }
        }

        bat '''
            echo ===== Final Emulator Status =====
            adb devices
            adb shell getprop sys.boot_completed
        '''
    }
}

        stage('Install Dependencies') {

            steps {

                bat 'python -m pip install --upgrade pip'

                bat 'pip install -r requirements.txt'
            }
        }

        stage('Verify Android Device') {

    steps {

        bat '''
            echo ===== Verifying Android Device =====

            adb devices

            adb -s emulator-5554 get-state

            adb -s emulator-5554 shell getprop sys.boot_completed
        '''
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