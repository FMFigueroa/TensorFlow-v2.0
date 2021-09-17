import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
x = tf.placeholder("float")
y = 2 * x
data = tf.random.uniform([4,5],2)
with tf.Session() as sess:
    x_data = sess.run(data)
    print(sess.run(y,feed_dict={x:x_data}))
sess.close()
