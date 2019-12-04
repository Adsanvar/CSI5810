import numpy as np
import pandas as pd
from numpy import linalg as LA
import matplotlib.pyplot as plt

#U^t F V = delta^1/2
#U and V are Orhogonal matrices of size m x m and n x n.
#delta^1/2 is a mxn diagonal matrix
#F = U delta^1/2 V^t
#Columns of U are eigenvectors of the FF^t
#Columns of V are eigenvectors of the F^tF

matrix = np.array([[1,0,1,0,0,0], [0,1,0,0,0,0], [1,1,0,0,0,0], [1,0,0,1,1,0], [0,0,0,1,0,1]])
test = np.array([[6,6], [0,1], [4,0], [0,6]])
#print("F:\n" + str(matrix))

#VT
Ff = np.matmul(matrix.T, matrix)
#print("F'F:\n" + str(Ff))
w, v = LA.eig(Ff)
print("F'F: Eigen Values:\n" + str(np.round(w, 3)) + "\nEigenvectors:\n" + str(np.round(v.T, 3)))
#U
fF = np.matmul(matrix,matrix.T)
#print("FF':\n" + str(fF))
w, v = LA.eig(fF)
print("FF': Eigen Values:\n" + str(w) + "\nEigenvectors:\n" + str(v))

#SVD
print("\nOther")
U, s, VT = LA.svd(matrix)
print("U:\n" + str(U))
print("s:\n" + str(s))
print("VT:\n" + str(VT))

# print("S(1):\n" + str(np.round(s[0], 3)))
# print("U(1)\n" + str(np.round(U[0], 3)))
# print("V(1)T\n" + str(np.round(VT[0], 3)))

# print("S(2):\n" + str(np.round(s[1], 3)))
# print("U(2)T\n" + str(np.round(U[1], 3)))
# print("V(2)T\n" + str(np.round(VT[1], 3)))

# print("S(3):\n" + str(np.round(s[2], 3)))
# print("U(3)\n" + str(np.round(U[2], 3)))
# print("V(3)T\n" + str(np.round(VT[2], 3)))

# print("S(4):\n" + str(np.round(s[3], 3)))
# print("U(4)\n" + str(np.round(U[3],3)))
# print("V(4)T\n" + str(np.round(VT[3], 3)))

# print("S(5):\n" + str(np.round(s[4], 3)))
# print("U(5)\n" + str(np.round(U[4],3)))
# print("V(5)T\n" + str(np.round(VT[4],3)))

#Reconstruction

# Sigma = np.zeros((matrix.shape[0], matrix.shape[1]))
# print(Sigma.shape)
# print(U.shape)
# print(VT.shape)
# # populate Sigma with n x n diagonal matrix
# print(np.diag(s).shape)
# Sigma[:matrix.shape[0], :matrix.shape[0]] = np.diag(s)
# # reconstruct matrix
# B = U.dot(Sigma.dot(VT))
# print(B)

# Sigma = np.zeros((2, 2))
# print(Sigma.shape)
# print(U[:2].shape)
# print(VT[:2].shape)
# # populate Sigma with n x n diagonal matrix
# print(np.diag(s[:2]).shape)
# Sigma[:2, :2] = np.diag(s[:2])
# # reconstruct matrix
# B = U[:2].T.dot(Sigma.dot(VT[:2]))
# print(B)

# print("S(1):\n" + str(np.round(s[0], 3)))
# print("U(1)\n" + str(np.round(U[0], 3)))
# print("V(1)T\n" + str(np.round(VT[0], 3)))

k = s[0] * np.matmul(np.reshape(U[0], (5,1)),np.reshape(VT[0], (1,6)))
k = k + s[1] * np.matmul(np.reshape(U[1], (5,1)),np.reshape(VT[1], (1,6)))
print(np.round(k, 3))
# print("S(2):\n" + str(np.round(s[1], 3)))
# print("U(2)T\n" + str(np.round(U[1], 3)))
# print("V(2)T\n" + str(np.round(VT[1], 3)))
from sklearn.metrics.pairwise import cosine_similarity

print(cosine_similarity(matrix, matrix))

plt.plot(cosine_similarity(matrix, matrix))
plt.show()