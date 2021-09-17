import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.constant([[1,2,3,4],
                 [3,4,5,6],
                 [5,6,7,8],
                 [7,8,9,10],
                 [9,10,11,12],
                 [11,12,13,14]])
print(X[0,:])
print(X[1:3,0:2])
print(X[3:,2:3])
print(X[:2,3])