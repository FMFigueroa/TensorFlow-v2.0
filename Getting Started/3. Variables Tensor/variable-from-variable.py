import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
weights = tf.Variable(tf.random.normal([3,3],stddev=2))
# Create another variable with the same value as 'weights'.
weight2 = tf.Variable(weights.read_value(),name="weight2")
# Create another variable with twice the value of 'weights'
w_twice = tf.Variable(weights.read_value() * 2.0, name="w_twice")
print(weight2,w_twice)
