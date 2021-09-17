import os
os.environ["TF_CPP_MIN_LOG_LEVEL)"] = "2"
import tensorflow as tf
#Define a 5x5 Identity matrix
I_matrix = tf.eye(5)
print(I_matrix)
#Define a Variable initialized to a 10x10 identity matrix
X = tf.Variable(tf.eye(10))
print(X)
# Evaluate the Variable and print the result
#Create a random 5x10 matrix
A = tf.Variable(tf.random.normal([5,10]))
#Multiply two matrices
product = tf.matmul(A, X)
print(product)
#create a random matrix of 1s and 0s, size 5x10
b = tf.Variable(tf.random.uniform([5,10], 0, 2, dtype=tf.int32))
print(b)
#Cast to float32 data typ
b_new = tf.cast(b, dtype=tf.float32)
print(b_new)
# Add the two matrices
t_sum = tf.add(product, b_new)
t_sub = product - b_new
print("A*X + b_new", t_sum)
print("A*X - b_new", t_sub)