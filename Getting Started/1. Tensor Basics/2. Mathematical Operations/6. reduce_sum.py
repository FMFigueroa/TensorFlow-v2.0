import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.constant([9,8,7])
Y = tf.constant([1,2,3])
Z = tf.reduce_sum(X*Y,axis=0)
print(Z)