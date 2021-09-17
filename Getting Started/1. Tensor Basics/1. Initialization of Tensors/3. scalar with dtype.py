import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.constant(4, dtype=tf.float32)
print(X)