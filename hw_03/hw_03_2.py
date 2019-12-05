import numpy as np

#class vectors
c1 = np.array([[2,10], [2,5], [1,2], [4,9]])
c2 = np.array([[8,4], [5,8], [7,5], [6,4]])
test = [3,3]
#means
c1_mean = np.mean(c1, 0)
c2_mean = np.mean(c2, 0)

#matrix
c1_mat = 3 * np.cov(c1.T)
c2_mat = 3 * np.cov(c2.T)

mat = c1_mat + c2_mat

mat_inv = np.linalg.inv(mat)

#weight vector

weight_vec = np.matmul(mat_inv, (c1_mean - c2_mean))

#mat mult to get classification
c1_pro = np.matmul(weight_vec.T, c1_mean)
c2_pro = np.matmul(weight_vec.T, c2_mean)

#cut in half
z = .5 * (c1_pro + c2_pro)

print("C1 Projection: {}".format(c1_pro))
print("C2 Projection: {}".format(c2_pro))
var = np.matmul(weight_vec.T, test)
print("Determination of [3,3] Class Label: {}".format(var))
print("Z-cut: {}".format(z) )
print("So the predicted value is: Class One.")
