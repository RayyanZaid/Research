import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
print(tf.__version__)

# physical_devices = tf.config.list_physical_devices('GPU')

# if physical_devices:
#     # Enable memory growth for the first GPU
#     tf.config.experimental.set_memory_growth(physical_devices[0], True)
# else:
#     print("No GPUs found, memory growth setting is not needed.")





# # Initialization of Tensors

# x = tf.constant(4)  
# print(x)  

# x = tf.constant([[1,2,3] , [4,5,6]])
# print(x)
#   # shape represent the r x c matrix. so shape = (2,3) is a 2x3 matrix



# # Mathematical Operations

# x = tf.constant([1,2,3])  # cols in first matrix ==
# y = tf.constant([9,8,7])  # rows in second matrix

# z = tf.tensordot(x,y,axes=1)
# print(z)



# x = tf.constant([[1, 2],
#                  [1, 2],
#                  [1, 2]])  # 3 x 2 matrix

# y = tf.constant([[2, 2, 3],
#                  [1, 1, 1]])  # 2 x 3 matrix

# z = tf.tensordot(x, y, axes=2)
# print(z)

# z = tf.matmul(x,y)
# z = x @ y

# print(z == z)


# Indexing

# x = tf.constant([0,1,1,2,3,1,2,3])
# print(x[:])
# print(x[1:]) # excludes the first element

# indices = tf.constant([0,3])
# x_ind = tf.gather(x,indices)
# print(x_ind)


# x = tf.constant([[1,2],
#                  [3,4],
#                  [5,6]])

# print(x[0])

# print(x[0:2]) # prints out the first 2 rows


# Reshaping


x = tf.range(9)
print(x)

x = tf.reshape(x,(3,3))
print(x)


# Transposing (switching rows and cols)

x = tf.transpose(x, perm=[1,0]) # swaps the axis
print(x)