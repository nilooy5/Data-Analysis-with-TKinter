import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris() # returns np-array (150 rows and 4 columns)
print(iris.data)
# Each row is a 4D sample
# Column: Sepal Length, Sepal Width, Petal Length and Petal Width.
X = iris.data[:, :2] #take the first two columns.
y = iris.target
# Target names: Setosa, Versicolour, and Virginica
labels = iris.target_names
# Plot the data
plt.scatter(X[:, 0], X[:, 1], label='iris', c='r', marker='o', s=30)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
