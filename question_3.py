import numpy as np
import io_data_module as io

dataset = io.read_multi_dim_data("Files_Assignment3/iris.data")

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
        print(item[0], item[1], item[2], item[3], item[4])
        X.append(item[:-2])
        if item[-1] == 'Iris-setosa':
            y.append(0)
        elif item[-1] == 'Iris-versicolor':
            y.append(1)
        elif item[-1] == 'Iris-virginica':
            y.append(2)

    i = i + 1

print(X)
print(y)
# print(labels_dict)
print(class_labels)
# print(class_labels.index('Iris-setosa'))

