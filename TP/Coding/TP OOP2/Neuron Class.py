import numpy as np 
class Neuron:
    def __init__(seft, weights):
        seft.weights = np.array(weights)
    
    def forward (seft, inputs):
        z = np.dot(seft.weights , inputs)
        return seft.sigmoid(z)
    def sigmoid(seft, x):
        return 1/(1+np.exp(-x))
    
# Example usage
neuron = Neuron([0.5, -0.6])
output = neuron.forward([1.0, 2.0])
print("Neuron output:", output)