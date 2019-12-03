import numpy as np
import pandas as pd
from numpy import linalg as LA

#U^t F V = delta^1/2
#U and V are Orhogonal matrices of size m x m and n x n.
#delta^1/2 is a mxn diagonal matrix
#F = U delta^1/2 V^t
#Columns of U are eigenvectors of the FF^t
#Columns of V are eigenvectors of the F^tF

matrix = np.array([[1,0,1,0,0,0], [0,1,0,0,0,0], [1,1,0,0,0,0], [1,0,0,1,1,0], [0,0,0,1,0,1]])
test = np.array([[6,6], [0,1], [4,0], [0,6]])
print("F:\n" + str(matrix))

Ff = np.matmul(matrix.T, matrix)
print("F'F:\n" + str(Ff))
w, v = LA.eig(Ff)
print("F'F: Eigen Values:\n" + str(w) + "\nEigenvectors:\n" + str(v))
fF = np.matmul(matrix,matrix.T)
print("FF':\n" + str(fF))
w, v = LA.eig(fF)
print("FF': Eigen Values:\n" + str(w) + "\nEigenvectors:\n" + str(v))

#SVD
print("\nOther")
U, s, VT = LA.svd(matrix)
print("U:\n" + str(U))
print("s:\n" + str(s))
print("VT:\n" + str(VT))

print("S(1):\n" + str(np.round(s[0], 3)))
print("U(1)\n" + str(np.round(U[:,0], 3)))
print("V(1)T\n" + str(np.round(VT[0], 3)))

print("S(2):\n" + str(np.round(s[1], 3)))
print("U(2)T\n" + str(np.round(U[:,1], 3)))
print("V(2)T\n" + str(np.round(VT[1], 3)))

print("S(3):\n" + str(np.round(s[2], 3)))
print("U(3)\n" + str(np.round(U[:,2], 3)))
print("V(3)T\n" + str(np.round(VT[2], 3)))

print("S(4):\n" + str(np.round(s[3], 3)))
print("U(4)\n" + str(np.round(U[:,3],3)))
print("V(4)T\n" + str(np.round(VT[3], 3)))

print("S(5):\n" + str(np.round(s[4], 3)))
print("U(5)\n" + str(np.round(U[:,4],3)))
print("V(5)T\n" + str(np.round(VT[4],3)))

#Reconstruction
#y =np.matmul(U[:,0].T , VT[0])

# 1.594 *
# [-0.296 -0.331 -0.511  0.351  0.647]^t *
# [-0.286 -0.528 -0.186  0.626  0.22   0.406]