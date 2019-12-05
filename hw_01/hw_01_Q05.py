import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from matplotlib.lines import Line2D
from sklearn.manifold import TSNE

plt.style.use('dark_background')
data = pd.read_csv("wdbc.data", header= None)
#removes id and diagnosis for standardization
num_data = data.drop([data.columns[0], data.columns[1]], axis=1)
num_data = num_data.values
#Standardize x -> Removes mean from all attributes of x
standata = StandardScaler().fit_transform(num_data)

tsne = TSNE(n_components=2, verbose=1, perplexity=10, n_iter=2000)
results = tsne.fit_transform(standata)
comp_1 = results[:,0]
comp_2 = results[:,1]
target = data[data.columns[1]]
labels = {'M': 'Malignent', 'B': 'Benign'}
colors = {'M': 'deeppink', 'B': 'yellow'}
marker={'M':'^', 'B': 'o'}
alpha={'M': .3, 'B': .5 }
uniquevals = np.unique(target)
uniquevals = uniquevals[::-1]
fig, ax = plt.subplots(figsize=(5, 5))
for i in uniquevals:
    index = np.where(target == i)
    ax.scatter(comp_1[index], comp_2[index], s=40, label=labels[i], c= colors[i], marker = marker[i], alpha = alpha[i])
plt.legend()
ax.set(title="TSNE Breast Cancer\n*Perplexity 10", xlabel='First Component', ylabel='Second Component')
fig.savefig("Q05_per10.png",format='png')