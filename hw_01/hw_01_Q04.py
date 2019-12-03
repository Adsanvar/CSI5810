import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib.lines import Line2D


plt.style.use('dark_background')
headers = ['ID number', 'Diagnosis','radius', 'texture', 'perimeter','area','smoothness','compactness',
'concavity', 'concave points', 'symmetry','fractal dimension']

data = pd.read_csv("wdbc.data", header= None)
#removes id and diagnosis for standardization
num_data = data.drop([data.columns[0], data.columns[1]], axis=1)
num_data = num_data.values
#print(str(data))
#Standardize x -> Removes mean from all attributes of x
standata = StandardScaler().fit_transform(num_data)
#covariance
c = np.cov(standata.T)
#eigen values / vectors from data
w, v = np.linalg.eig(c)
eigenvals = "Eigen Values: " + str(w)+ "\nEigen Vectors: " + str(v)

pca = PCA(n_components=2)
components = pca.fit_transform(standata)
comp_1 = components[:,0]
comp_2 = components[:,1]
target = data[data.columns[1]]
labels = {'M': 'Malignent', 'B': 'Benign'}
colors = {'M': 'lawngreen', 'B': 'deepskyblue'}
marker={'M':'^', 'B': 'o'}
alpha={'M': .3, 'B': .5 }
uniquevals = np.unique(target)
uniquevals = uniquevals[::-1]
fig, ax = plt.subplots(figsize=(7, 5))
for i in uniquevals:
    index = np.where(target == i)
    ax.scatter(comp_1[index], comp_2[index], s=40, label=labels[i], c= colors[i], marker = marker[i], alpha = alpha[i])
plt.legend()
ax.set(title="PCA Breast Cancer", xlabel='First Component', ylabel='Second Component')
fig.savefig("Q04.png",format='png')

