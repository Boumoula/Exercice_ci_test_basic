class VirusDiagnosisSystem:
    def __init__(self, model):
        self.model = model

    def diagnose(self, patient_features):
        """
        Diagnostique un patient à partir de ses caractéristiques.
        :param patient_features: Liste ou array [temperature, tension, toux]
        :return: 0 ou 1 (résultat de la prédiction)
        """
        return self.model.predict([patient_features])[0]
