from sklearn.neural_network import MLPClassifier
from core.model import BaseModel

class NeuralNetworkModel(BaseModel):
    def __init__(self):
        # Configuration simple d'un MLP
        self.model = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=500, random_state=42)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        proba_all = self.model.predict_proba(X)
        return proba_all[:, 1]
