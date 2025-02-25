import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

C = np.eye(150) - 1/150 * np.ones((150, 150))

iris = load_iris()['data']
target = load_iris()['target']
target_names = load_iris()['target_names']
colors = ['red', 'blue', 'green']
X_prime = iris.T
X = X_prime @ C

training_data = X.T @ X
eigvals = np.linalg.eig(training_data)[0]
eigvecs = np.linalg.eig(training_data)[1]
print(np.shape(eigvecs))

idx = np.argsort(eigvals)[::-1]
sorted_eigvals = eigvals[idx]
sorted_eigvecs = eigvecs[:, idx]
V = sorted_eigvecs.T[0:2]
Sigma = np.diag(np.sqrt(sorted_eigvals[0:2]))

print(np.shape(Sigma))
print(np.shape(V.T))


