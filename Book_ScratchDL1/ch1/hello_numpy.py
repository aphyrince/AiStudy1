import numpy as np

X = np.array([[1,2],[3,4],[5,6]])

X = X.flatten()
print(X)

print(X[np.array([0,2,4])])

print(X>3)

print(X[X>2])

