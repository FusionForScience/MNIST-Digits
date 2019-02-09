from Layer import Layer
from Neuron import Neuron

class Network:
    def __init__(self , layerSizes):
        self.layers = []

        # Create layers
        for i in layerSizes:
            self.layers.append(Layer(i))

        # And then connect them
        for i in range(len(self.layers)):
            if i > 0:
                self.layers[i - 1].connect(self.layers[i])
    

    def print(self):
        for i in range(len(self.layers)):
            print("Layer " + str(i) + ": ")
            self.layers[i].print()
    

    def setInput(self , input):
        for i in range(len(self.layers[0].neurons)):
            self.layers[0].neurons[i].rawInput(input[i])
            