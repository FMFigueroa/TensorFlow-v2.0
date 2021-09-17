import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
bias = tf.Variable(tf.zeros([2,2]))
print(bias.initializer)

