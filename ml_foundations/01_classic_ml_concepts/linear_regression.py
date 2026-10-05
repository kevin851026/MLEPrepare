import numpy as np
from sklearn.linear_model import LinearRegression

# X: house size, y: house price
X = np.array([[50], [70], [90], [110], [130]])
y = np.array([150, 190, 230, 270, 310])

model = LinearRegression()
model.fit(X, y)

print("intercept:", model.intercept_)
print("coefficient:", model.coef_[0])
print("prediction for size=100:", model.predict([[100]])[0])
