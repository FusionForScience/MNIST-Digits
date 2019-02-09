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
    

    def connect(self , layer):
        self.connection = layer

        for i in self.neurons:
            for j in layer.neurons:
                i.connect(j)
    

    # MAKE SURE YOU CALL CONNECT FIRST
    def propagate(self):
        for i in self.neurons:
            i.propagate()
