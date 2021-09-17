import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
rand_t = tf.random.uniform([5,5],0,10,seed=0)
t_a = tf.Variable(rand_t)
t_b = tf.Variable(rand_t)
print(t_a,t_b)