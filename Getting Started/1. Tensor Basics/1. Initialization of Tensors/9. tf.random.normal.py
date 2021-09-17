import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.random.normal((3,3), mean=0, stddev=1) # Standard Normal Distribution
print(X)