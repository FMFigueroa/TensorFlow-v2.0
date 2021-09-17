import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
import numpy as np
X = tf.random.uniform((5,5), minval=0, maxval=5) # Standard Normal Distribution
Y = np.random.uniform(low=0, high=5, size=(5,5))  # With Numpy
print(X,Y)