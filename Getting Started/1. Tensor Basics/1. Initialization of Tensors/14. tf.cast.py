import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
# tf.cast change different dtypes: tf.float (16,32,64) // tf.int(8,16,32,64) // tf.bool
X = tf.range(start=1, limit=11, delta=2)
Y = tf.cast(X, dtype=tf.float64)
C = tf.cast(Y, dtype=tf.bool)
print(X,Y,C)