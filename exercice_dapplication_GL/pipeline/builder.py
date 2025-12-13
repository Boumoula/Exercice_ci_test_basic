from core.dataset import PatientDataset
from core.logistic_regression import LogisticRegressionModel
from core.system import VirusDiagnosisSystem

class VirusModelBuilder:
    def __init__(self):
        self.data_path = None
        self.dataset = None
        self.model = LogisticRegressionModel()

    def set_data_path(self, path):
        self.data_path = path
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
        
        X, y = self.dataset.get_features_and_labels()
        self.model.train(X, y)
        return self

    def get_system(self):
        return VirusDiagnosisSystem(self.model)
