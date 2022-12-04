from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import filedialog
# import fileinput

def display():
    root = Tk()
    root.title("Regression Model")
    root.minsize(500, 500)

    # def select_linear_regress_file():
    #     root.filename = filedialog.askopenfilename(initialdir=r"filepath", title="Select A File", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    #     return root.filename

    # root.iconbitmap()

    description = Label(text="Select regression type")
    description.place(x=200, y=20)
    btn_linear_regression = Button(text="Random Linear Regression", width=30, height=3)
    btn_linear_regression.place(relx=0.5, rely=0.25, anchor=E)

    btn_polynomial_regression = Button(text="Random Polynomial Regression", width=30, height=3)
    btn_polynomial_regression.place(relx=0.95, rely=0.25, anchor=E)



    root.mainloop()

display()
