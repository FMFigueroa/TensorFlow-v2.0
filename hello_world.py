#import os
#os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
message = tf.constant("Bienvenido al Gran Mundo de Deep Neural Networks")
print(message.numpy().decode())