import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.constant([10,25,40])
Y = tf.constant([2,5,8])
Z = tf.divide(X,Y)
A = X // Y
print(Z,A)