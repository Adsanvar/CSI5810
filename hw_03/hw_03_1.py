import numpy as np
import matplotlib as plt


data = np.array([[2,2,-1], [3,5,-1], [1,3,-1], [-1, -0.5, -1]]) #Given Class 1 and Class 2
classes = np.array([1,1,2,2]) #Classes  
aug_vec = np.array([1,1,1]) #weights
d = 4 #how deep the summation will go

#Perceptron that takes in the two classes data and the classes map

print(aug_vec)
def perceptron(input, class_label, to_d):
    global aug_vec
    if to_d == 0:
        print('OUTPUT: ')
        print(aug_vec)
    else:
        cal_weight(input, class_label)
        to_d -= 1
        perceptron(input, class_label, to_d)  

#Calculates the weight
def cal_weight(dt, labels):
    global aug_vec
    if dt.size == 0:
        print(aug_vec)
    else:
        if ((np.dot(dt[0], aug_vec))* labels[0]) <= 0:
            aug_vec = aug_vec + (dt[0] * labels[0])
        cal_weight(dt[1:], labels[1:])

#calls the perceptron with overloaded parameters
perceptron(data, classes, d)

