import numpy as np

class Perceptron:
    def __init__(self, imput_size, learning_rate=0.01, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(imput_size + 1)
    
    def predict(self, x):
        x = np.insert(x, 0, 1) # Insert 1 at the beginning of the array (bias)
        activation = np.dot(self.weights, x) # product of weights and inputs (w_i * x_i)
        return 1 if activation >= 0 else 0 # Activation function
    
    def train(self, X, y):
        for _ in range(self.epochs): # Train for a number of epochs
            for i in range(y.shape[0]): # Iterate over all samples in the dataset (X)
                prediction = self.predict(X[i]) # Predict the output for the current sample (X[i])
                self.weights += self.learning_rate * (y[i] - prediction) * np.insert(X[i], 0, 1) # Update weights based on the prediction error and the learning rate (w_i = w_i + learning_rate * (y - prediction) * x_i)
    
    def loss(self, X, y):
        loss = 0 # Initialize loss to 0
        for i in range(y.shape[0]): # Iterate over all samples in the dataset (X) to calculate the loss
            loss += (y[i] - self.predict(X[i])) ** 2 # Add the squared difference between the true output and the predicted output to the loss (L = (y - prediction)^2)
        return loss
    
    def accuracy(self, X, y):
        correct = 0 # Initialize correct predictions to 0
        for i in range(y.shape[0]): # Iterate over all samples in the dataset (X) to calculate the accuracy
            correct += self.predict(X[i]) == y[i] # Add 1 to correct predictions if the predicted output is equal to the true output (y)
        return correct / y.shape[0] # Return the ratio of correct predictions to the total number of samples in the dataset

if __name__ == "__main__":
    # XOR Dataset
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])
    
    # Train Perceptron
    perceptron = Perceptron(imput_size=2)
    perceptron.train(X, y)
    
    # Predict and evaluate
    print(f'Loss: {perceptron.loss(X, y)}')
    print(f'Accuracy: {perceptron.accuracy(X, y)}')
    print('Predictions:')
    for i in range(y.shape[0]):
        print(f'X: {X[i]}, y: {y[i]}, Prediction: {perceptron.predict(X[i])}')
        
    # Or Dataset
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 1])
    
    # Train Perceptron
    perceptron = Perceptron(imput_size=2)
    perceptron.train(X, y)
    
    # Predict and evaluate
    print(f'Loss: {perceptron.loss(X, y)}')
    print(f'Accuracy: {perceptron.accuracy(X, y)}')
    print('Predictions:')
    for i in range(y.shape[0]):
        print(f'X: {X[i]}, y: {y[i]}, Prediction: {perceptron.predict(X[i])}')
    
