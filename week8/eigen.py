from numpy import linalg as LA
import numpy
#x=numpy.array([[1,2,3] ,[4,5,7], [6,9,7]])
x=numpy.array([[1,-2,] , [2,-3]])
w,v=LA.eig(x)
print w
print v

