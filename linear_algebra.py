import numpy as np


"""adds matrices unless shape is not equal"""




def add_matrices(a, b):
   if a.shape != b.shape:
       raise ValueError("not valid")
   return np.add(a, b)




"""subtracts matrices unless shape is not equal"""




def subtract_matrices(a, b):
   if a.shape != b.shape:
       raise ValueError("not valid")
   return np.subtract(a, b)




def dot_product(a, b):
   return np.dot(a, b)




"""number of columns in matrix a must be equal to number of rows in matrix b to multiply"""




def multiply_matrix(a, b):
   if len(a[0]) != len(b):
       raise ValueError("not valid")
   return np.matmul(a, b)




def magnitude(a):
   return np.linalg.norm(a)




def transpose_matrix(a):
   return np.transpose(a)