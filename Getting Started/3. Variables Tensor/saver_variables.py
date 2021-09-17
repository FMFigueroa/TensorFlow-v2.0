import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
t_a = tf.Variable(tf.random.uniform([5,5],0,10,seed=0))
