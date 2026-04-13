pipeline {
    agent any
    stages {
        stage('Nettoyage et Build') {
            steps {
                sh '''
                # On supprime TOUT ce qui concerne l'ancien environnement
                rm -rf venv
                
                # On crée le venv proprement
                python3 -m venv venv
                
                # On répare les permissions immédiatement
                chmod -R +x venv/bin/
                
                # On n'essaye PAS de mettre à jour pip (c'est souvent ce qui casse tout)
                # On installe directement les outils nécessaires
                ./venv/bin/pip install pytest bandit safety
                
                # Installation des dépendances si elles existent
                if [ -f requirements.txt ]; then
                    ./venv/bin/pip install -r requirements.txt
                fi
                '''
            }
        }
        stage('Tests et Sécurité') {
            steps {
                sh '''
                # On s'assure que Python trouve le code source
                export PYTHONPATH=$PYTHONPATH:.
                
                # Exécution des tests (on ne bloque pas le pipeline ici pour voir la suite)
                ./venv/bin/pytest tests/ || echo "Tests en échec, mais on continue pour la sécurité"
                
                # Bandit (Sécurité du code)
                ./venv/bin/bandit -r . -ll || true
                
                # Safety (Sécurité des librairies)
                ./venv/bin/safety check || true
                '''
            }
        }
    }
    post {
        always {
            sh 'rm -rf venv'
        }
    }
}
