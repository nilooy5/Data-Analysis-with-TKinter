import io_q9 as io
import matplotlib.pyplot as plt
import numpy as np

dataset_name = 'blue_2d'
# dataset_name = 'red_2d'
# dataset_name = 'unknown_2d'

selected_file = 'Files_Assignment3/' + dataset_name + '.txt'

dataset = io.read_multi_dim_data(selected_file)
print(dataset)
arr = np.array(dataset)

"""make a scatter plot from dataset"""
plt.scatter(arr[:, 0], arr[:, 1], s=10, c='r')
plt.show()
