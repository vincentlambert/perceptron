import numpy as np


class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=1000):
        self.weights = np.zeros(input_size + 1)  # +1 pour le biais
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        z = self.weights.T.dot(np.insert(x, 0, 1))  # Ajouter le biais
        return self.activation_function(z)

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                prediction = self.predict(xi)
                update = self.learning_rate * (target - prediction)
                self.weights[1:] += update * xi
                self.weights[0] += update  # Mise à jour du biais


# Exemple d'utilisation
if __name__ == "__main__":
    # Données d'entraînement (ET logique)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])

    # Données d'entraînement (OR logique)
    # X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # y = np.array([0, 1, 1, 1])

    # Données d'entraînement (XOR logique)
    # X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # y = np.array([0, 1, 1, 0])

    perceptron = Perceptron(input_size=2)

    print("Entraînement du perceptron...")
    perceptron.train(X, y)

    # Prédictions
    print("Prédictions...")
    for xi in X:
        print(f"Entrée: {xi}, Prédiction: {perceptron.predict(xi)}")
