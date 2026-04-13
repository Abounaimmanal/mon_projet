pipeline {
    agent any

    stages {
        stage('Build + Tests + Sécurité') {
            steps {
                sh '''
                # 1. Création de l'environnement virtuel
                python3 -m venv venv
                
                # 2. Correction des permissions (Crucial pour éviter l'erreur 126)
                chmod -R +x venv/bin/
                
                # 3. Installation/Mise à jour des outils de base
                ./venv/bin/python -m pip install --upgrade pip
                
                # 4. Installation des dépendances du projet
                if [ -f requirements.txt ]; then
                    ./venv/bin/pip install -r requirements.txt
                fi
                
                # 5. Installation des outils de test et sécurité
                ./venv/bin/pip install pytest bandit safety
                
                # 6. Exécution des tests (vérifiez que votre dossier s'appelle bien 'tests')
                if [ -d tests ]; then
                    ./venv/bin/pytest tests/
                else
                    echo "Dossier tests non trouvé, passage à l'étape suivante."
                fi
                
                # 7. Analyse de sécurité statique (SAST) avec Bandit
                # On scanne '.' pour tout le projet, ou 'src/' si votre code est là
                ./venv/bin/bandit -r . -ll
                
                # 8. Vérification des vulnérabilités des dépendances avec Safety
                ./venv/bin/safety check
                '''
            }
        }

        stage('Nettoyage') {
            steps {
                echo "Suppression de l'environnement virtuel..."
                sh 'rm -rf venv'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline exécuté avec succès."
        }
        failure {
            echo "❌ Pipeline échoué. Vérifiez les logs ci-dessus pour les erreurs de tests ou de sécurité."
        }
    }
}
