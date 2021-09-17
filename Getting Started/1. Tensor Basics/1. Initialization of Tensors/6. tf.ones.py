import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.ones((3,3), dtype=tf.int8)
print(X)