import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

#Data post processing
wd = pd.read_excel('Wheat_Data.xlsx')

feature_class = []
wd_arr = np.array(wd)
features = [i for i in wd_arr[0:96][:,:-1]]
feature_class = [i for i in wd_arr[:-4,7]] 
classOne = wd_arr[0:32]
classTwo = wd_arr[32:64]
classThree = wd_arr[64:96]
testData = [wd_arr[97:98][:,:-1], wd_arr[98:99][:,:-1], wd_arr[99:100][:,:-1] ]
predictions = []

#1-NN
knn1 = KNeighborsClassifier(1)
knn1.fit(features, feature_class)
knn1Pre = []
for x in range(0, len(testData)):
    knn1Pre.append("1NN Test "+ str(x+1) + " Result {}".format(knn1.predict(testData[x])))

knn1Pre.append(" Accuracy: {:.2f}".format(knn1.score(features, feature_class)))

predictions.append(knn1Pre)

#3-NN
knn3 = KNeighborsClassifier(3)
knn3.fit(features, feature_class)
knn3Pre = []
for x in range(0, len(testData)):
    knn3Pre.append("3NN Test "+ str(x+1) + " Result {}".format(knn3.predict(testData[x])))

knn3Pre.append("Accuracy: {:.2f}".format(knn3.score(features, feature_class)))

predictions.append(knn3Pre)

#5-NN
knn5 = KNeighborsClassifier(5)
knn5.fit(features, feature_class)
knn5Pre = []

for x in range(0, len(testData)):
    knn5Pre.append("5NN Test "+ str(x+1) + " Result {}".format(knn5.predict(testData[x])))

knn5Pre.append("Accuracy: {:.2f}".format(knn5.score(features, feature_class)))

predictions.append(knn5Pre)

nbc = GaussianNB()
nbc.fit(features, feature_class)
for x in range(0, len(testData)):
    #knn5Pre.append("5NN Test "+ str(x+1) + " Result {}".format(knn5.predict(testData[x])))
    print(nbc.predict(testData[x]))

print(nbc.score(features, feature_class))
