# Just disables the warning, doesn't take advantage of AVX/FMA to run faster
# import os
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
import tensorrt

print(tensorrt.__version__)
assert tensorrt.Builder(tensorrt.Logger())
# print(tf.reduce_sum(tf.random.normal([1000, 1000])))
# print(tf.config.list_physical_devices("GPU"))
