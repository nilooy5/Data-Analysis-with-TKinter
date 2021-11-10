import tkinter as tk
import data_plotter as dp

# import training as training

# some font configurations for GUI
myFont = "Arial, 12"
myFont_big = "Arial, 15 bold"
myFont_medium = "Arial, 10"
myFont_small = "Arial, 8"

window = tk.Tk()
window.title('Programming for Data Science')
window.geometry("700x500+400+100")

lbl_header = tk.Label(
    text="Final Assignment Q9 by Fazal Mahmud Niloy (u3228358)",
    font=myFont_big,
    height=1
)
lbl_header.place(x=150, y=10)

lbl_dataset = tk.Label(
    text="Select a dataset: ",
    fg="navy",
    anchor="w",
    width=25,
    height=1,
    font=myFont
)
lbl_dataset.place(x=10, y=50)

lbl_selected_dataset = tk.Label(
    text="",
    fg="red",
    anchor="w",
    width=25,
    height=1,
    font=myFont_small
)
lbl_selected_dataset.place(x=10, y=70)


def select_dataset():
    selected = dataset_name.get()
    selected_dataset_string = selected + ' dataset selected'
    lbl_selected_dataset.config(text=selected_dataset_string)
    select_widget_values()


dataset_name = tk.StringVar(value="")

rb_blue = tk.Radiobutton(
    text="Blue",
    variable=dataset_name,
    value='blue_2d',
    font=myFont,
    command=select_dataset
)
rb_blue.place(x=180, y=50)

rb_red = tk.Radiobutton(
    text="Red",
    variable=dataset_name,
    value='red_2d',
    font=myFont,
    command=select_dataset
)
rb_red.place(x=250, y=50)

rb_unknown = tk.Radiobutton(
    text="Unknown",
    variable=dataset_name,
    value='unknown_2d',
    font=myFont,
    command=select_dataset
)
rb_unknown.place(x=350, y=50)

rb_all = tk.Radiobutton(
    text="All",
    variable=dataset_name,
    value='all',
    font=myFont,
    command=select_dataset
)
rb_all.place(x=450, y=50)


def select_widget_values():
    # select_dataset()
    dp.plot_data(dataset_name.get())


window.mainloop()
