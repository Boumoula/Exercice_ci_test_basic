import sys
import os

# Ajout du chemin racine du projet pour permettre les imports
# si le script est exécuté directement (python pipeline/trainer.py)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipeline.builder import VirusModelBuilder

def main():
    # Construction du système avec le Builder
    builder = VirusModelBuilder()
    
    system = (
        builder
        .set_data_path("data/patients_infectes.csv")
        .load_data()
        .train_model()
        .get_system()
    )

    print("✅ Modèle entraîné avec succès via le Builder !")
    print("Test de diagnostic pour un patient (38°C, 12 tension, toux=1)...")
    result = system.diagnose([38.0, 12.0, 1])
    print(f"Résultat du diagnostic : {result}")

if __name__ == "__main__":
    main()
