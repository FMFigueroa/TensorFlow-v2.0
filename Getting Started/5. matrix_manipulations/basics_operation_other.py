import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
# Create two random matrices
a = tf.Variable(tf.random.normal([4,5], stddev=2))
b = tf.Variable(tf.random.normal([4,5], stddev=2))
#Element Wise Multiplication
A = a * b
#Multiplication with a scalar 2
B = tf.scalar_mul(2, A)
# Element wise division, its result is
C = tf.divide(a,b)
#Element Wise remainder of division
D = tf.math.mod(a,b)
#print
print("a\n",a,"b\n",b, "a*b\n",A,"\n2*a*b\n",B,"\na/b\n",C, "\na%b\n",D)
