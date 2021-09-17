import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.constant([9,8,7])
Y = tf.constant([1,2,3])
Z = tf.tensordot(X,Y, axes=1) # in this case only has a axes or dimensions.

A = tf.constant([[9,8,7],[1,2,3]])
B = tf.constant([[1,2,3],[9,8,7]])
C = tf.tensordot(A,B, axes=2) # in this case has two axes or dimensions.
print(Z,C)