from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore", category=matplotlib.MatplotlibDeprecationWarning)


def display():
    root = Tk()
    root.title("Regression Model")
    root.minsize(500, 500)
    root.resizable(False, False)

    description = Label(text="Select regression type")
    description.place(x=200, y=20)
    btn_linear_regression = Button(text="Random Linear Regression", width=30, height=3, command=run)
    btn_linear_regression.place(relx=0.5, rely=0.25, anchor=E)

    btn_polynomial_regression = Button(text="Random Polynomial Regression", width=30, height=3)
    btn_polynomial_regression.place(relx=0.95, rely=0.25, anchor=E)

    root.mainloop()


def run():

    # X = 4 * np.random.rand(100, 1) - 2  # Generates random values between 0 and 1
    # y = 2*X + np.random.randn(100, 1)

    df = 0.5 * pd.DataFrame(np.random.randint(0, 100, size=(90, 2)), columns=list('AB'))

    data = df.to_csv()
    print(df)
    columns = df.columns.values.tolist()
    column1 = columns[0]
    min = math.ceil(df[column1].min(axis=0)) - 1
    max = math.ceil(df[column1].max(axis=0)) + 1

    def gradient_descent(m_current, b_current, points, l_rate):
        m_gradient = 0
        b_gradient = 0
        n = len(points)
        for i in range(n):
            x = points.iloc[i].A
            y = points.iloc[i].B
            m_gradient += -(2 / n) * x * (y - ((m_current * x) + b_current))
            b_gradient += -(2 / n) * (y - ((m_current * x) + b_current))
        m = m_current - m_gradient * l_rate
        b = b_current - b_gradient * l_rate
        return m, b

    def return_slope(m, b):
        return m, b

    m = 0
    b = 0
    learning_rate = 0.0001
    num_epochs = 400

    for i in range(num_epochs):
        if i % 50 == 0:
            print(f"Epoch: {i}")
        m, b = gradient_descent(m, b, df, learning_rate)

    print(f"y = {m}x + {b}")
    column_names = list(df.columns.values.tolist())
    slope = f"y = {round(m, 2)}x + {round(b, 2)}"

    font1 = {'color': 'blue', 'size': 18}

    x = list(range(min, max))
    y = [m * x + b for x in range(min, max)]

    plt.scatter(df.A, df.B)
    plt.plot(x, y, label=slope, color="red")
    plt.xlabel(column_names[0].title())
    plt.ylabel(column_names[1].title())
    plt.title(f"{column_names[0].title()} vs. {column_names[1].title()}", fontdict=font1)
    plt.legend(loc='upper left')
    plt.show()

display()
