from tkinter import filedialog
from matplotlib  import pyplot as plt
import matplotlib.image as mpimg
import tkinter as tk
from tkinter import ttk
import base64
import requests
import io
import json

server = "http://vcm-21170.vm.duke.edu"
filename = None


# Select image to upload
def select_image():
    global filename
    filename = filedialog.askopenfilename(initialdir="BME547")
    return


# Convert image file to base64 string
def convert_image_file_to_base_64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


# Upload base64 string to server
def upload_base64_string_to_server(b64_image):
    out_data = {"image": b64_image, "net_id": "yc551", "id_no": 1}
    r = requests.post(server + '/add_image', json=out_data)
    print(r.text)


# Download water marked image
def download_water_marked_image():
    global filename
    r = requests.get(server + "/get_image/yc551/1")
    filename = filedialog.asksaveasfilename(initialdir="BME547", defaultextension=".txt")
    file = open(filename, 'w')
    file.write(r.text)
    file.close
    return


# View b64 image
def view_b64_image(base64_string):
    image_bytes = base64.b64decode(base64_string)
    image_buf = io.BytesIO(image_bytes)
    i = mpimg.imread(image_buf, format='JPG')
    plt.imshow(i, interpolation='nearest')
    plt.show()
    return

def main():
    select_image()
    if filename == "":
        return
    b64_image = convert_image_file_to_base_64_string(filename)
    upload_base64_string_to_server(b64_image)
    download_water_marked_image()
    file = open(filename, "r")
    base64_string = file.read()
    file.close()
    view_b64_image(base64_string)


def set_up_window():
    root = tk.Tk()
    root.title("Image Server GUI")
    select_button = ttk.Button(root, text="Select image", command=select_image)
    select_button.grid(column=0, row=0)
    root.mainloop()


if __name__ == '__main__':
    main()
    # set_up_window()
