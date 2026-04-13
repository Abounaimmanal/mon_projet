import sys
import os
# Cette ligne permet à Python de trouver votre code dans le dossier parent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# On importe 'addition' depuis votre fichier principal (ex: app.py ou main.py)
# Si votre fichier s'appelle 'app.py', écrivez : from app import addition
try:
    from main import addition 
except ImportError:
    # Si le fichier est à la racine et s'appelle autrement, adaptez ici
    def addition(a, b): return a + b 

def test_addition():
    assert addition(2, 3) == 5
