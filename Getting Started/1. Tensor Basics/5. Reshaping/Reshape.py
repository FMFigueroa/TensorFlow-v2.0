import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.range(9)
print(X)
R_X = tf.reshape(X,(3,3))
print(R_X)
