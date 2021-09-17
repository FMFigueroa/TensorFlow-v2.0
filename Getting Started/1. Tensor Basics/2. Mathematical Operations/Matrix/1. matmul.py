import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

X = tf.constant([[5,3,-4,-2],[8,-1,0,-3]]) # (2x4)
Y = tf.constant([[1,4,0],[-5,3,7],[0,-9,5],[5,1,4]]) # (4x3)
Z = tf.matmul(X,Y) # (2x3)
print(X)
print(Y)
print(Z)
Z = X @ Y
print(Z)