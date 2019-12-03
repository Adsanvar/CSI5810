import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data = pd.read_excel("CrimeRate.xlsx")
data = data.drop(columns=data.columns[7:])

X = data[['X3', 'X4', 'X5', 'X6', 'X7']]
y = data[['X1']]

Y= data.iloc[:, 0]
X3 = data.iloc[:, 2]

lm = LinearRegression()

model = lm.fit(X, y)
# plt.title('Crime Rate Data')
# plt.scatter(X['X3'], y, label="X3")
# plt.scatter(X['X4'], y,label="X4")
# plt.scatter(X['X5'], y,label="X5")
# plt.scatter(X['X6'], y,label="X6")
# plt.legend()
# plt.xlabel('VARS')
# plt.ylabel('X1')
# plt.savefig('Data.png', format='png')

#print('Betas {}'.format(model.coef_))

#print(model.score(X, y))

#finding best fit line

N = 32
alpha = 1.3
beta = np.array([.5, 1.9])

w = np.random.randn(3)

l_rate = .0001
result = []
loss = 0

for t in range(200):
    y_pred = X3.dot(w)
    loss = np.square(y_pred - Y)
    if t % 10 == 0:
        print(t, loss)
        result.append(loss)
    grad_y_pred = 2.0 * (y_pred - Y)
    grad_w = X3.T.dot(grad_y_pred)
    w -= l_rate * grad_w

print(w)