import cv2
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img_arr = []
imgs= []
img_class = []
no_bueno = []
# im = cv2.imread('/Users/adriansandoval/Documents/CSI5810/EC/train/ASENSIO_1.jpg')
# plt.imshow(im)
# plt.show()
for file in os.listdir():
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        imgs.append(file)
        #img = cv2.imread(path +'/' +str(os.path.basename(os.path.abspath(img))))
        img = cv2.imread(file)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(img_gray, 1.1, 3)
    
        trip = 0
        for (x,y,w,h) in faces:
            #cv2.rectangle(asen,(x,y),(x+w,y+h),(255, 0, 0), 2)
            img = cv2.resize(img_gray[y:y+h, x:x+w], (100,100))
            img_arr.append(img.flatten())
            trip += 1
            if len(faces) >1:
                
                #print("Index: " + str(len(img_arr)) + " trip: "+ str(trip)+" Image: "+ str(faces))
                if len(img_arr) == 24 or len(img_arr) == 29 or len(img_arr) == 45 or len(img_arr) == 56 or len(img_arr) == 84 or len(img_arr) == 97 or len(img_arr) == 98:
                    no_bueno.append(len(img_arr)-1)
                #     if trip == 1:
                #         no_bueno.append(faces[0])
                #     if trip == 2:
                #         no_bueno.append(faces[1])
                # print(len(img_arr))
                # plt.imshow(img)
                # plt.show()

x = 0
for i in no_bueno: 
    if i  == 23:
        img_arr.pop(i)
        x +=1
    else:
        i = (i-x)
        #print("popping i: " + str(i))
        img_arr.pop(i)
        #print(len(img_arr))
        x +=1

df = pd.DataFrame(img_arr)
#dfx = (df - df.mean())/df.std()

for i in imgs:
    if 'ASENSIO' in i:
        img_class.append(1)
    if 'BALE' in i:
        img_class.append(2)
    if 'BENZEMA' in i:
        img_class.append(3)
    if 'CARVAJAL' in i:
        img_class.append(4)
    if 'COURTOIS' in i:
        img_class.append(5)
    if 'HAZARD' in i:
        img_class.append(6)
    if 'ISCO' in i:
        img_class.append(7)
    if 'KROOS' in i:
        img_class.append(8)
    if 'MARCELO' in i:
        img_class.append(9)
    if 'RAMOS' in i:
        img_class.append(10)

print(df)
print(img_class)
xtrain, xtest, ytrain, ytest = train_test_split(df, img_class, test_size = .1, random_state =12)
pca = PCA(n_components = 10)
X = pca.fit_transform(xtrain)
Xtest = pca.fit_transform(xtest)

knn = KNeighborsClassifier(4)
knn.fit(X,ytrain)

print(knn.score(Xtest,ytest))



# print(img_arr.shape)
# x = 0
# for file in os.listdir('train'):
#     #print(os.path.basename(os.path.abspath(file)))
#     x +=1
#     if x == 1:
#         asen = cv2.imread(os.path.basename(os.path.abspath(file)))
#         # asen = cv2.cvtColor(asen, cv2.COLOR_BGR2RGB)
#         #asen_gray = cv2.cvtColor(asen, cv2.COLOR_BGR2GRAY)
#         # plt.imshow(asen_gray, cmap='gray')
#         # plt.show()
#         plt.imshow(asen)
#         plt.show()
#         #cv2.waitKey(0)
#     else:
#         break



