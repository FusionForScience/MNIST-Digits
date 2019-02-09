import random

# some notes
# a neuron should have no idea of what comes before it
# it just listens to its activations and does its thing

class Neuron:
    class Connection:
        def __init__(self , connection):
            self.connection = connection    # this is another neuron
            self.weight = random.random() * 2 - 1   # Between -1 and 1

        def print(self):
            # purposely not printing the connected neuron
            print("Weight: " + str(self.weight))



    def __init__(self):
        random.seed()
        self.bias = 0
        self.activation = 0
        self.connections = []
        
    
    def connect(self , neuron):
        self.connections.append(self.Connection(neuron))


    def print(self):
        print("Bias: " + str(self.bias))
        print("Connections: ")
        print(self.connections)
        

    def sigmoid(self , input):
        e = 2.71828
        return (e ** input) / ((e ** input) + 1)