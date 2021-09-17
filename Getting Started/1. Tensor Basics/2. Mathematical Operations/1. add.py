import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.constant([1,2,3])
Y = tf.constant([9,8,7])
Z = tf.add(X,Y)
A = X + Y
print(Z,A)
