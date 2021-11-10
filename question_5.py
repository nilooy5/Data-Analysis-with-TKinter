import matplotlib.pyplot as plt
from sklearn import datasets

while True:
    print("input 2 numbers from between 0 to 3.")
    try:
        a = int(input("a: "))
        b = int(input("b: "))
    except ValueError:
        print("input error.")
        continue

    if a < 0 or a > 3 or b < 0 or b > 3:
        print("input error.")
        continue

    iris = datasets.load_iris()  # returns np-array (150 rows and 4 columns)

    # print(iris['feature_names'])

    # Each row is a 4D sample
    # Column: Sepal Length, Sepal Width, Petal Length and Petal Width.
    X = iris.data[:, [a, b]]  # take the first two columns.
    y = iris.target
    # print("X =", X)
    # print("X-0 =", X[:, 0])
    # print("X-1 =", X[:, 1])
    # Target names: Setosa, Versicolour, and Virginica
    labels = iris.target_names
    # Plot the data
    plt.scatter(X[:, 0], X[:, 1], label='iris', c='r', marker='o', s=30)
    plt.xlabel(iris['feature_names'][a])
    plt.ylabel(iris['feature_names'][b])
    plt.title('Iris dataset')
    plt.legend()
    plt.show()
