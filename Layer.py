from Neuron import Neuron

class Layer:
    def __init__(self , size):
        self.size = size
        self.neurons = []

        for i in range(size):
            self.neurons.append(Neuron())
        
    
    def print(self):
        for i in self.neurons:
            i.print()
    