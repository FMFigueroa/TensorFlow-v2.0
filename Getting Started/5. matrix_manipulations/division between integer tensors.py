import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
a = tf.random.uniform([5,5],1,100,dtype=tf.int32)
b = tf.random.uniform([5,5],1,11,dtype=tf.int32)
t_div = tf.truediv(a,b)
print(a,b,"change_int_to_float", t_div)