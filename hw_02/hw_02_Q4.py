import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs

#X, y = make_blobs(n_samples= 10, centers= 2, cluster_std= 4.0, random_state=10)
from matplotlib.colors import ListedColormap
cmap_light = ListedColormap(["#AAFFAA", "#AAAAFF"])

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
X = np.array([[1,0],  [0, 1], [0, -1], [0, 0], [0, 2], [0, -2], [-2, 0]])
elements = [0, 0, 0, 1, 1, 1, 1]
class_one = np.array([[1,0],  [0, 1], [0, -1]])
class_two = np.array([[0, 0], [0, 2], [0, -2], [-2, 0]])
#i
k_value = 1
knn = KNeighborsClassifier(k_value)
knn.fit(X, elements)
x_min, x_max = X[:, 0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
fig = plt.figure(figsize=(12,6))
plt.pcolor(xx, yy, Z, cmap=cmap_light)
# plt.scatter(class_one[:,0], class_one[:,1], c="r", label='Class One')
# plt.scatter(class_two[:,0], class_two[:,1], c="b", label='Class Two')
plt.xlabel("first feature")
plt.ylabel("second feature")
#print("accuracy: {:.2f}".format(knn.score(X, elements)))
plt.legend()
plt.show()
#fig.savefig("Q4_i.png", format='png')

#ii
# print(X[:,0])
# classOne_vector = [class_one[:, 0].mean(), class_one[:, 1].mean()]
# classTwo_vector = [class_two[:, 0].mean(), class_two[:, 1].mean()]
# dis = (classOne_vector[0] + classTwo_vector[0])/2
# middle = [dis, 0]
# print(dis)
# print(classOne_vector)
# print(classTwo_vector)
# fig = plt.figure(figsize=(12,6))
# plt.scatter(class_one[:,0], class_one[:,1], c="r", label='Class One')
# plt.scatter(class_two[:,0], class_two[:,1], c="b", label='Class Two')
# plt.scatter(middle[0], middle[1], color='m')
# plt.text(middle[0]-.175, middle[1]-.175, "Middle of Means", color='m')
# plt.scatter(classOne_vector[0], classOne_vector[1], c='g' )
# plt.plot([classOne_vector[0], middle[0]], [0, 0],'g--')
# plt.text(classOne_vector[0]-.125, classOne_vector[1]+.125, "Class1 Mean Vector", color='g')
# plt.scatter(classTwo_vector[0], classTwo_vector[1], c='c')
# plt.text(classTwo_vector[0]-.125, classTwo_vector[1]+.125, "Class2 Mean Vector", color='c')
# plt.plot([classTwo_vector[0], middle[0]], [0, 0],'c--')
# plt.plot([middle[0], middle[0]], [-2.1, 2.1],'m-')
# plt.axvspan(middle[0], 1.1, color ='r', alpha=.1)
# plt.axvspan(middle[0], -2.1, color ='b', alpha=.1)
# plt.xlabel("first feature")
# plt.ylabel("second feature")
# plt.legend()
# plt.show()
# fig.savefig("Q4_ii.png", format='png')