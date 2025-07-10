import unittest
import linear_algebra
import numpy as np




class testLinearAlgebra(unittest.TestCase):
   a = np.array([1, 2, 3])
   b = np.array([4, 5, 6])
   a1 = np.array([[1, 2], [3, 4]])
   b1 = np.array([[5, 6], [7, 8]])


   def test_add_matrices(self):
       self.assertEqual(list(linear_algebra.add_matrices(self.a, self.b)), [5, 7, 9])
       self.assertEqual(
           list(linear_algebra.add_matrices(np.array([1, 2, 3]), np.array([4, 5, 6]))),
           [5, 7, 9],
       )
       self.assertEqual(
           linear_algebra.add_matrices(self.a1, self.b1).all(),
           np.array([[6, 8], [10, 12]]).all(),
       )
       self.assertRaises(ValueError, linear_algebra.add_matrices, self.a, self.b1)


   def test_subtract_matrices(self):
       self.assertEqual(
           list(linear_algebra.subtract_matrices(self.a, self.b)), [-3, -3, -3]
       )
       self.assertEqual(
           linear_algebra.subtract_matrices(self.a1, self.b1).all(),
           np.array([[-4, -4], [-4, -4]]).all(),
       )
       self.assertRaises(ValueError, linear_algebra.add_matrices, self.a, self.b1)


   def test_dot_product(self):
       self.assertEqual(linear_algebra.dot_product(self.a, self.b), 32)
       self.assertNotEqual(linear_algebra.dot_product(self.a1, self.b1).all(), 52)


   def test_multiply_matrix(self):
       self.assertEqual(
           linear_algebra.multiply_matrix(
               np.array([[1, 2, 3], [4, 5, 6]]),
               np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]),
           ).all(),
           np.array([[74, 80, 86, 92], [173, 188, 203, 218]]).all(),
       )
       self.assertRaises(
           ValueError,
           linear_algebra.multiply_matrix,
           np.array([[1, 2, 3], [4, 5, 6]]),
           np.array([[1, 2, 3], [4, 5, 6]]),
       )


   def test_magnitude(self):
       self.assertEqual(
           linear_algebra.magnitude(np.array([1, 1, 2])), 2.449489742783178
       )
       self.assertNotEqual(linear_algebra.magnitude(np.array([1, 1, 2])), 2.45)


   def test_transpose_matrix(self):
       self.assertEqual(
           linear_algebra.transpose_matrix(self.a1).all(),
           np.array([[1, 3], [2, 4]]).all(),
       )
       self.assertEqual(
           linear_algebra.transpose_matrix(self.b1).all(),
           np.array([[5, 7], [6, 8]]).all(),
       )