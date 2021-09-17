import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
weights = tf.Variable(tf.random.normal([3,3],stddev=2))
bias = tf.Variable(tf.ones([3,3]),name="biases")
print(weights,bias)