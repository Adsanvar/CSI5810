import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import distance
from matplotlib.lines import Line2D

plt.style.use('dark_background')

mean = [1, 2, 1]
cov = [ [5, 0.8, -0.3], [0.8, 3, 0.6], [-0.3, 0.6, 4]]

#Generate 100 3D vectors
x, y, z = np.random.multivariate_normal(mean, cov, 100).T
titles = ['X Vs. Y', 'X Vs. Z', 'Y Vs. Z']
c = 0

fig, ax = plt.subplots(1, 3, figsize=(8, 5))

ax[0].scatter(x, y)
ax[0].set(xlabel='X', ylabel='Y')
ax[1].scatter(x, z)
ax[1].set(xlabel='X', ylabel='Z')
ax[2].scatter(y, z)
ax[2].set(xlabel='Y', ylabel='Z')

for a in ax:
    a.set_title(titles[c])
    c += 1


fig.savefig("Q02_AB.png", format='png', bbox_inches='tight')

#-------------------Part C--------------#

a = []
b = []
pat = []
colors = ['red', 'blue', 'green', 'yellow', 'white']
#first chart
fig2 = plt.figure(figsize=plt.figaspect(0.5))
ax2 = fig2.add_subplot(1,2,1, projection='3d')
ax2.scatter(x, y, z) 
ax2.set(xlabel='X', ylabel='Y', zlabel='Z')
#second chart, keep same axes
ax3 = fig2.add_subplot(1,2,2, projection='3d')
ax3.set(xlabel='X', ylabel='Y', zlabel='Z', xlim=(ax2.get_xlim()), ylim=(ax2.get_ylim()), zlim=(ax2.get_zlim()))

#chooses 5 pairs of 2. first 5.
for i in range(0, 10, 2):
    a = np.array((x[i], y[i], z[i]))
    b = np.array((x[i+1], y[i+1], z[i+1]))
    j = int(i/2)
    ax3.scatter(x[i], y[i], z[i], c=colors[j], marker='x')
    ax3.scatter(x[i+1], y[i+1], z[i+1], c=colors[j], marker='x')
    pat.append(Line2D([0], [0], marker='X', color='black', label="Euclidian, Mahalanobis : " +str(round(distance.euclidean(a,b), 1)) + ", " 
    + str(round(distance.mahalanobis(a,b, np.linalg.inv(cov)), 1)) , markerfacecolor= colors[j], markersize=15))

#Legend
lg = ax3.legend(handles = pat, loc = "best", bbox_to_anchor=(1, 1))
#Save, note must have (lg,) inorder to keep the chart in picture.
fig2.savefig("Q02_C.png", format='png', bbox_extra_artists=(lg,), bbox_inches='tight')

#plt.show()

