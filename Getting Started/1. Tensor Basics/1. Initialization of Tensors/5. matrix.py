import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
X = tf.constant([[1,2,3],[4,5,6]], dtype=tf.float16)
print(X)