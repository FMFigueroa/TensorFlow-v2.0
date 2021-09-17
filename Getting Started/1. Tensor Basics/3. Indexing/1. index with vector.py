import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.constant([0,1,1,2,3,1,2,3])
print(X[:])
print(X[:4])
print(X[4:])
print(X[4:5])
print(X[::2])
print(X[::-1])

indices = tf.constant([0,3])
X_ind = tf.gather(X,indices)
print(X_ind)