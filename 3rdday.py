# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:06:23 2023

@author: Pradip
"""
from numpy import array
#define matrix
A=array([[1,2],[3,4],[5,6]])
print(A)
#calculate transpose
C=A.T 
print(C)

########################################################

#invert matrix
from numpy import array
from numpy.linalg import inv
#define matrix
A=array([[1.0,2.0],[3.0,4.0]])
print(A)
#invert matrix
B=inv(A) 
print(B)


#multiple A and B
I=A.dot(B)
print(I)

########################################################

#sparse matrix--more no of zeros matrix
from numpy import array
from scipy.sparse import csr_matrix
#create dense matrix
A=array([[1,0,0,1,0,0],[0,0,2,0,0,1],[0,0,0,2,0,0]])
print(A)
#convert to sparse matrix (CSR Technique)
S=csr_matrix(A)
print(S)
#reconstruct dense matrix
B=S.todense()
print(B)

########################################################

#write a numpy to get the numpy version and show the numpy
import numpy as np
print(np.__version__)
print(np.show_config())
#write a numpy program to get help with the add function
import numpy as np
print(np.info(np.add))
#write a numpy program to test whether none of the elements of a given array is zero:.
import numpy as np
x=np.array([1,2,3,4])
print("original array:")
print(x)
print("Test if none of the elements of the said array is zero")
print(np.all(x))
x=np.array([0,1,2,3])
print("Original array")
print(x)
print("test if none of the elements of the said array is zero")
print(np.all(x))

#--------------------------------------------------------------

#write a numpy program to test if any of the elements of a given
#array is non-zero
import numpy as np
x=np.array([1,0,0,0])
print("original array:")
print(x)
print("Test if none of the elements of the said array is zero")
print(np.any(x))
x=np.array([0,0,0,0])
print("Original array")
print(x)
print("test if none of the elements of the said array is zero")
print(np.any(x))

#-------------------------------------------------------------

#write a numpy program to test a given array
#elements-wise for finiteness (not infinity or not a number)
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("original array:")
print(a)
print("Test given array elements-wise finiteness:")
print(np.isfinite(a))

#--------------------------------------------------------

#write a numpy program to test element wise for nan of the given array
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("original array:")
print(a)
print("Test element-wise for nan:")
print(np.isnan(a))

#--------------------------------------------------------

#write a numpy program to test element wise for
#complex number , real number in a given array 
#also test if a given number is not scalar type of not.
import numpy as np
a=np.array([1+1j,1+0j,4.5,3,2,2j])
print("original array:")
print(a)
print("Checking for complex numbers:")
print(np.iscomplex(a))
print("Checking for real numbers:")
print(np.isreal(a))
print("Checking for scalar type:")
print(np.isscalar(3.1))
print(np.isscalar([3.1]))

#--------------------------------------------------------

#write a numpy program to compare to compute multiplication
#of two given strings
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original matrix:")
print(p)
print(q)
result=np.dot(p,q)
print("dot product of the said to two vectors:")
print(result)

#--------------------------------------------------------

#for outer product
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original matrix:")
print(p)
print(q)
result=np.outer(p,q)
print("outer product of the said to two vectors:")
print(result)

#--------------------------------------------------------

import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original matrix:")
print(p)
print(q)
result1=np.cross(p,q)
result2=np.cross(q,p)
print("cross product of the said to two vectors(p,q):")
print(result1)
print("cross product of the said to two vectors(q,p):")
print(result2)

########################################################

#write a python program to draw a line with suitable label
import matplotlib.pyplot as plt
X=range(1,50)
Y=[value*3 for value in X]
print("value of X:")
print(*range(1,50))

'''
this is equivalent to -
i in range(1,50):
    print(i,end="")
'''
print("Value of Y (thrice of X):")
print(Y)
#plot lines and/or markers to the Axes
plt.plot(X,Y)
#set the x axis label of the current axis.
plt.xlabel('X-axis')
#set the y axis label of the current axis
plt.ylabel('Y-axis')
#set a title
plt.title('Draw a line.')
#display the figure
plt.show()

###############################################################



