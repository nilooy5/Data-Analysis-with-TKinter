import numpy as np
import io_data_module as io


def load_iris_dataset(filename):
    dataset = io.read_multi_dim_data("Files_Assignment3/" + str(filename))

    labels_dict = {}
    for item in dataset:
        item = list(item)
        if item[-1] not in labels_dict:
            labels_dict[item[-1]] = [item[:-1]]
        else:
            labels_dict[item[-1]].append(list(item[:-1]))

    class_labels = list(labels_dict.keys())

    i = 0

    X = []
    y = []

    for item in dataset:
        item = list(item)
        if i % 2 == 1:
            temp = []
            for j in item[:-1]:
                temp.append(float(j))
            X.append(temp)
            temp = []
            if item[-1] == 'Iris-setosa':
                y.append(0)
            elif item[-1] == 'Iris-versicolor':
                y.append(1)
            elif item[-1] == 'Iris-virginica':
                y.append(2)

        i = i + 1

    return [X, y, class_labels]


X, y, class_labels = load_iris_dataset('iris.data')

print('X =', X)
print('y =', y)
print('class labels =', class_labels)

