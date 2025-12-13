from sklearn.svm import SVC
from core.model import BaseModel

class SVMModel(BaseModel):
    def __init__(self):
        # probability=True est nécessaire pour predict_proba
        self.model = SVC(probability=True, kernel='linear')

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        proba_all = self.model.predict_proba(X)
        return proba_all[:, 1]
