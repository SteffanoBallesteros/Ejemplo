pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SteffanoBallesteros/Ejemplo.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat '"C:/Users/Usuario/AppData/Local/Programs/Python/Python312/python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Pruebas') {
            steps {
                bat '"C:/Users/Usuario/AppData/Local/Programs/Python/Python312/python.exe" -m pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Despliegue') {
            steps {
                echo "🚀 Iniciando despliegue de la app Flask..."
                bat '"C:/Users/Usuario/AppData/Local/Programs/Python/Python312/python.exe" app.py'
            }
        }
    }
}
