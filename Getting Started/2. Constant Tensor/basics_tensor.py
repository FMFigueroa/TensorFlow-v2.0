import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
#Scalar
t_1 = tf.constant(4)
# Vector of shape [1,3]
t_2 = tf.constant([4,3,2])
# Tensor with all elements zero
zero_t = tf.zeros([2,3],tf.int32) # Results in an 2×3 array of zeros: [[0 0 0], [0 0 0]]
# Tensor with all elements ones
ones_t = tf.ones([2,3],tf.int32) # Results in an 2×3 array of ones:[[1 1 1], [1 1 1]]
#tf.ones_like
t_like = tf.ones_like(t_2)
# sequence of evenly spaced vectors tf.linspace(start,stop,num)
#The corresponding values differ by (stop-start)/(num-1).
space_t = tf.linspace(2.0,5.0,5) # We get: [ 2. 2.75 3.5 4.25 5. ]
# sequence of numbers starting from the start (default=0), incremented
# by delta (default =1), until, but not including, the limit.
# tf.range(start,limit,delta)
range_t = tf.range(10) # Result: [0 1 2 3 4 5 6 7 8 9]
print(t_1,t_2,zero_t,ones_t,t_like,space_t,range_t)