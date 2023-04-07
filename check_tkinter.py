import tkinter as tk
from tkinter import ttk


def main_window():

    def close_cmd():
        root.destroy()

    root = tk.Tk()
    root.title("Check tkinter")

    ttk.Label(root, text="You have successfully run a tkinter interface",
              font=("Arial", 14)).grid(column=0, row=0)
    close_button = ttk.Button(root, text="Click Here To Close",
                              command=close_cmd)
    close_button.grid(column=0, row=1)

    root.mainloop()


if __name__ == '__main__':
    main_window()