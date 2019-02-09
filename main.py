from mnist import MNIST
from Layer import Layer

mndata = MNIST('Resources')

images, labels = mndata.load_training()

print(mndata.display(images[0]))
print(labels[0])

layer = Layer(12)

layer.print()