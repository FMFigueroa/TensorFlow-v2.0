import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.eye(3, dtype=tf.int16) # I for the identity matrix (eye)
print(X)