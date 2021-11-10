import io_q9 as io

# blue_2d.txt, red_2d.txt and unknown_2d.txt
selected_file = 'Files_Assignment3/blue_2d.txt'
# selected_file = 'Final_Assignment3/red_2d.txt'
# selected_file = 'Final_Assignment3/unknown_2d.txt'

dataset = io.read_multi_dim_data(selected_file)
print(dataset)
