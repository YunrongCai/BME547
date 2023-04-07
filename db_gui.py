import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk





def set_up_window():

    def ok_btn_cmd():
        print("OK clicked")
        patient_name = name_value.get()
        id_name = id_value.get()
        blood_letter = blood_letter_value.get()
        print(patient_name)
        print(id_name)
        print(blood_letter)

    def cancel_btn_cmd():
        root.destroy()

    def change_label_color():
        current_color = top_label.cget("foreground")
        if current_color == '':
            color = 'black'
        else:
            color = current_color.string
        if color == "black":
            new_color = "red"
        else:
            new_color = "black"
        top_label.configure(foreground=new_color)
        root.after(1000, change_label_color)

    root = tk.Tk()
    root.title("Donor Database GUI")
    root.geometry("600x300")
    top_label = ttk.Label(root, text="Blood Donor Database", foreground="red")
    top_label.grid(column=0, row=0)
    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1)
    name_value = tk.StringVar()
    name_entry = ttk.Entry(root, textvariable=name_value)
    name_entry.grid(column=1, row=1)
    id_label = ttk.Label(root, text="Id:")
    id_label.grid(column=0, row=2)
    id_value = tk.IntVar()
    id_entry = ttk.Entry(root, textvariable=id_value)
    id_entry.grid(column=1, row=2)

    ok_button = ttk.Button(root, text="Ok", command=ok_btn_cmd)
    ok_button.grid(column=1, row=6)
    cancel_button = ttk.Button(root, text="Cancel", command=cancel_btn_cmd)
    cancel_button.grid(column=2, row=6)

    blood_letter_value = tk.StringVar()
    A_check = ttk.Radiobutton(root, text="A", variable=blood_letter_value,
                              value ="A")
    A_check.grid(column=0, row=3)
    B_check = ttk.Radiobutton(root, text="B", variable=blood_letter_value,
                              value="B")
    B_check.grid(column=0, row=4)

    rh_factor_value = tk.StringVar()
    rh_factor_value.set("+")
    check_box_widget = ttk.Checkbutton(root, text = "Rh",
                                       variable = rh_factor_value,
                                       onvalue = '+', offvalue = '-')
    check_box_widget.grid(column=1, row=4)

    donation_label= ttk.Label(root, text='Closest Donation Center')
    donation_label.grid(column=2, row=0)
    donation_value = tk.StringVar
    donation_combobox = ttk.Combobox(root,textvariable=donation_value)
    donation_combobox.grid(column=2, row=1)
    donation_combobox["value"] = ("Apex", "Durham", "Raleigh")


    root.after(3000, change_label_color)
    root.mainloop()

if __name__ == "__main__":
    set_up_window()