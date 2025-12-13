from core.dataset import PatientDataset
from core.system import VirusDiagnosisSystem

class VirusModelBuilder:
    def __init__(self):
        self.data_path = None
        self.dataset = None
        self.model = None

    def set_data_path(self, path):
        self.data_path = path
        return self

    def set_model_strategy(self, model_strategy):
        """
        Définit la stratégie de modèle à utiliser (Strategy Pattern).
        :param model_strategy: Instance d'une classe héritant de BaseModel
        """
        self.model = model_strategy
        return self

    def load_data(self):
        if not self.data_path:
            raise ValueError("Data path not set.")
        self.dataset = PatientDataset(self.data_path)
        self.dataset.load()
        return self

    def train_model(self):
        if not self.dataset:
            raise ValueError("Dataset not loaded.")
        if not self.model:
            raise ValueError("Model strategy not set.")
        
        X, y = self.dataset.get_features_and_labels()
        self.model.train(X, y)
        return self

    def get_system(self):
        return VirusDiagnosisSystem(self.model)
