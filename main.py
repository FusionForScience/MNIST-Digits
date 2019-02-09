from mnist import MNIST
from Layer import Layer

mndata = MNIST('Resources')

images, labels = mndata.load_training()

print(mndata.display(images[0]))
print(labels[0])

layer1 = Layer(2)
layer2 = Layer(2)

layer1.connect(layer2)

layer1.print()