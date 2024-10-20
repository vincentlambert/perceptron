import numpy as np
from keras.layers import Dense, Input
from keras.models import Sequential


class MLPerceptron:
    def __init__(self, input_size, learning_rate=0.05, epochs=2000):
        self.input_size = input_size
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.model = Sequential()
        self.model.add(Input((input_size,)))
        # self.model.add(Dense(4, activation="tanh"))  # Couche cachée avec 4 neurones
        self.model.add(Dense(2, activation="tanh"))  # Deuxième couche cachée
        self.model.add(Dense(1, activation="sigmoid"))  # Couche de sortie
        self.model.compile(
            loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"]
        )

    def train(self, X, y):
        self.model.fit(X, y, epochs=self.epochs, verbose=1)

    def predict(self, x):
        prediction = self.model.predict(np.array([x]))
        return 1 if prediction >= 0.5 else 0


# Exemple d'utilisation
if __name__ == "__main__":
    # Données d'entraînement (XOR logique)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])

    ml_perceptron = MLPerceptron(input_size=2)
    ml_perceptron.train(X, y)

    # # Prédictions
    for xi in X:
        print(f"Entrée: {xi}, Prédiction: {ml_perceptron.predict(xi)}")
