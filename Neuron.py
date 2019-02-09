import random

# some notes
# a neuron should have no idea of what comes before it
# it just listens to its activations and does its thing

class Neuron:
    def __init__(self):
        random.seed()
        self.bias = 0
        self.activation = 0

        # This doesn't go here but save the code for later
        self.weight = random.random() * 2 - 1   # Between -1 and 1
        

    def print(self):
        print("Bias: " + str(self.bias))

        # Also doesn't go here
        print("Weight: " + str(self.weight))


    def sigmoid(self , input):
        e = 2.71828
        return (e ** input) / ((e ** input) + 1)