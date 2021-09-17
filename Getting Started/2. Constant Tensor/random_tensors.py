import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
#tf.random.normal
t_random1 = tf.random.normal([2,3],mean=2.0,stddev=4,seed=12)
#tf.random.truncated_normal
t_random2 = tf.random.truncated_normal([1,5],stddev=2,seed=12)
#tf.random.uniform
t_random3 = tf.random.uniform([2,3],maxval=4,seed=12)
#tf.image.random_crop
t_random4 = tf.image.random_crop(t_random3,[2,3],seed=12)
#tf.random.shuffle
t_random5 = tf.random.shuffle(t_random4)
# tf.random.set_seed
tf.random.set_seed(24)
print(t_random1,t_random2,t_random3,t_random4,t_random5)
