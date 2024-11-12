
class Layer:
	def __init__(self, weights):
		self.neurons = [Neuron(w) for w in weights]
 
	def forward(self, inputs):
		return [neuron.forward(inputs) for neuron in self.neurons]
 
				# Example usage
layer = Layer([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
layer_output = layer.forward([1.0, 2.0])
print("Layer outputs:", layer_output)