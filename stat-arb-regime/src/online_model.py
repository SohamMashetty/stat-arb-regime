from sklearn.linear_model import PassiveAggressiveRegressor

class OnlineSpreadModel:
    def __init__(self):
        self.model = PassiveAggressiveRegressor(max_iter=1000, random_state=42, tol=1e-3)

    def partial_fit(self, X, y):
        self.model.partial_fit(X, y)

    def predict(self, X):
        return self.model.predict(X)