import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
plt.style.use('dark_background')

x = np.array([[5700, 12.8, 2500, 270, 25000], 
              [1000, 10.9, 600, 10, 10000],
              [3400, 8.8, 1000, 10, 9000],
              [3800, 13.6, 1700, 140, 25000],
              [4000, 12.8, 1600, 140, 25000],
              [8200, 8.3, 2600, 60, 12000],
              [1200, 11.4, 400, 10, 16000],
              [9100, 11.5, 3300, 60, 14000],
              [9900, 12.5, 3400, 180, 18000],
              [9600, 13.7, 3600, 390, 25000],
              [9600, 9.6, 3300, 80, 12000],
              [9400, 11.4, 4000, 100, 13000]])

''' Manually -> Look at his blog https://iksinc.online/2018/08/21/principal-component-analysis-pca-explained-with-examples/
#mean
xmean = np.mean(x, 0)
print("xmean: " + str(xmean))
#standardized 
x = x - xmean
print(str(x))
#covariance
c = np.cov(x.T)
#eigen values / vectors from data
w, v = np.linalg.eig(c)
print("Eigen Values: " + str(w)+ "\nEigen Vectors: " + str(v))

#transform matrix
x_transform = np.array([v[:,2], v[:,1]])
#New transformation to get 2-D
y = np.matmul(x_transform, (x - xmean).T)
#Recover original data
xhat = np.matmul(x_transform.T, y).T + xmean
mse = np.sum((x-xhat)**2)/ len(xhat)
print("Mean Square Error: " + str(mse))'''

#Standardize x -> Removes mean from all attributes of x
x = StandardScaler().fit_transform(x)
#covariance
c = np.cov(x.T)
#eigen values / vectors from data
w, v = np.linalg.eig(c)
#print("Eigen Values: " + str(w)+ "\nEigen Vectors: " + str(v))

pca = PCA(n_components=2)
components = pca.fit_transform(x)
xhat = pca.inverse_transform(components)
mse = np.sum((x - xhat) **2)/len(xhat)

print("MSE: " + str(mse))

#----------First Part---------
colors = ['red', 'blue']
labels = ['Component 1', 'Component 2']

fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(components[:,0], components[:,1], 'o')
ax.set(xlabel=labels[0], ylabel=labels[1])
ax.set(title="Reduction Representation")
wv = ""
for i  in range(len(v)):
    wv += str(v[i]) +"\n"
vecs = fig.suptitle("Eigen Values: " + str(w) + "\nEigen Vectors:\n" + wv, fontsize= 12, y = -.01)

fig.savefig("Q03.png",format='png', bbox_extra_artists=(vecs,), bbox_inches='tight')
#---------End First Part---------
#---------Second Part----------
fig2 = plt.figure(figsize=(12,6))
bw = 0.10
r1 = np.arange(len(xhat))
r2 = [x + bw for x in r1]
r3 = [x + bw for x in r2]
r4 = [x + bw for x in r3]
r5 = [x + bw for x in r4]
r6 = [x + bw for x in r5]
colors = ['blue', 'red']

plt.bar(r1, x[:,0], bw, alpha=0.5, color=colors[0], label='Original')
plt.bar(r2, xhat[:,0], bw, alpha=0.5, color=colors[1], label='Rescontructed')
plt.bar(r3, x[:,1], bw, alpha=0.5, color=colors[0])
plt.bar(r4, xhat[:,1], bw, alpha=0.5, color=colors[1])
plt.bar(r5, x[:,2], bw, alpha=0.5, color=colors[0])
plt.bar(r6, xhat[:,2], bw, alpha=0.5, color=colors[1])

plt.xticks([r + bw for r in range(len(xhat))], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L'])

plt.legend()
fig2.savefig("Q03_Reconstruction.png",format='png')

#---------End Second Part----------

#plt.show()




