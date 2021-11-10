import numpy
from sklearn import datasets, neighbors, metrics, svm
from sklearn.model_selection import train_test_split
import pandas as pd

dataset = datasets.load_iris()
# print(dataset)

X = dataset.data
# print('Array of data samples:')
# print(X)
# print()
n_samples, n_features = X.shape

# print('Number of data samples: ', n_samples)
# print('Dimensionality (Number of features): ', n_features)
# print()
y = dataset.target
# print('True class index of data samples:')
# print(y)
# print()
class_names = dataset.target_names
# print('Array of class names:', class_names)
# print('Number of classes:', len(class_names))
# print()

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
# print(X_train)
# print()
# print(X_test)
# print()
# print(y_train)
# print()
# print(y_test)
# print()

# Load classifier containing classification technique and model
classifier = neighbors.KNeighborsClassifier(n_neighbors=3)

# Training
classifier.fit(X_train, y_train)
# Testing
y_pred = classifier.predict(X_test)


def get_confusion_matrix(true_list, predicted_list, class_labels):
    c_matrix = pd.crosstab(true_list, predicted_list)
    c_matrix = c_matrix.set_axis(class_labels, axis=0, inplace=False)
    c_matrix = c_matrix.set_axis(class_labels, axis=1, inplace=False)
    return c_matrix


label_names = numpy.array(['Setosa', 'Versicolour', 'Virginica'])
confusion_matrix = get_confusion_matrix(y_pred, y_test, label_names)
print(confusion_matrix)

