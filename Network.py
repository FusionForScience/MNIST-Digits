from Layer import Layer

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
    
    