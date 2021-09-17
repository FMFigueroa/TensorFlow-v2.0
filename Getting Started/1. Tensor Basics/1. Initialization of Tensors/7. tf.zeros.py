import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.zeros((2,3), dtype=tf.int16)
print(X)