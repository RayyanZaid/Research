from keras.datasets import mnist
from keras import layers
from tensorflow import keras
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# keras - higher level API for tensorflow
# easier to make neural networks and APIs


# Loading Data

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(-1, 28*28).astype("float32") / 255
print(x_train.shape)

x_test = x_test.reshape(-1, 28*28).astype("float32") / 255
print(x_test.shape)


# Creating a model


