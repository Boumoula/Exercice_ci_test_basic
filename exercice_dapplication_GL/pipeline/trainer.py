import sys
import os

# Ajout du chemin racine du projet pour permettre les imports
# si le script est exécuté directement (python pipeline/trainer.py)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipeline.builder import VirusModelBuilder

from core.logistic_regression import LogisticRegressionModel
from core.svm import SVMModel
from core.neural_network import NeuralNetworkModel

def train_and_evaluate(builder, strategy_name, strategy_instance):
    print(f"\n--- Entraînement avec la stratégie : {strategy_name} ---")
    
    # On réutilise le même builder, mais on change la stratégie
    # Note: Dans une application réelle, on pourrait vouloir recharger les données une seule fois
    # Mais ici le builder recharge à chaque 'load_data'. 
    # Pour optimiser, on pourrait charger les données hors du builder ou adapter le builder.
    
    system = (
        builder
        .set_data_path("data/patients_infectes.csv")
        .set_model_strategy(strategy_instance)
        .load_data()
        .train_model()
        .get_system()
    )

    print(f"✅ Modèle ({strategy_name}) entraîné avec succès !")
    
    # Test simple
    patient_test = [38.0, 12.0, 1]
    result = system.diagnose(patient_test)
    print(f"Diagnostic pour patient standard {patient_test} : {result}")


def main():
    builder = VirusModelBuilder()

    strategies = [
        ("Régression Logistique", LogisticRegressionModel()),
        ("SVM", SVMModel()),
        ("Réseau de Neurones", NeuralNetworkModel())
    ]

    for name, strategy in strategies:
        train_and_evaluate(builder, name, strategy)

if __name__ == "__main__":
    main()
