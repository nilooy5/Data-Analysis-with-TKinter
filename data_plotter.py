import io_q9 as io
import matplotlib.pyplot as plt
import numpy as np

# dataset_name = 'blue_2d'
# dataset_name = 'red_2d'
# dataset_name = 'unknown_2d'
# dataset_name = 'all'


def plot_data(dataset_name, fig2, canvas):
    if dataset_name != 'all':
        if dataset_name == 'blue_2d':
            point_color = 'b'
        elif dataset_name == 'red_2d':
            point_color = 'r'
        elif dataset_name == 'unknown_2d':
            point_color = 'g'
        selected_file = 'Files_Assignment3/' + dataset_name + '.txt'

        dataset = io.read_multi_dim_data(selected_file)
        print(dataset)
        arr = np.array(dataset)

        # start fot mat plotlib inside tkinter
        fig2.add_subplot(111).scatter(arr[:, 0], arr[:, 1], c=point_color)

        canvas.draw()
        # end fot mat plotlib inside tkinter

        """make a scatter plot from dataset"""
        # plt.scatter(arr[:, 0], arr[:, 1], s=10, c=point_color)
        # plt.title(dataset_name)

    else:
        """read all datasets"""
        blue_file = 'Files_Assignment3/blue_2d.txt'
        red_file = 'Files_Assignment3/red_2d.txt'
        unknown_file = 'Files_Assignment3/unknown_2d.txt'
        blue_data = np.array(io.read_multi_dim_data(blue_file))
        red_red = np.array(io.read_multi_dim_data(red_file))
        unknown_data = np.array(io.read_multi_dim_data(unknown_file))

        print(blue_data)
        print(red_red)
        print(unknown_data)

        fig, axs = plt.subplots(2, 2)
        # axs[0, 0].scatter(blue_data[:, 0], blue_data[:, 1], s=10, c='b')
        fig2.add_subplot(2,2,1).scatter(blue_data[:, 0], blue_data[:, 1], s=10, c='b')
        # axs[0, 0].set_title('Blue Dataset')

        # axs[0, 1].scatter(red_red[:, 0], red_red[:, 1], s=10, c='r')
        fig2.add_subplot(2,2,2).scatter(red_red[:, 0], red_red[:, 1], s=10, c='r')
        # axs[0, 1].set_title('Red Dataset')

        # axs[1, 0].scatter(unknown_data[:, 0], unknown_data[:, 1], s=10, c='g')
        fig2.add_subplot(2,2,3).scatter(unknown_data[:, 0], unknown_data[:, 1], s=10, c='g')
        # axs[1, 0].set_title('Unknown Dataset')

        canvas.draw()

    # plt.show()
