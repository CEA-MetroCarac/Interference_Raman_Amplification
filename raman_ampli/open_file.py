import tkinter as tk
from tkinter import filedialog as fd
import os


# In[choose file]

def open_file_selection():
    file = fd.askopenfile()
    # print(label)
    # print(file.read())
    if file:
        file_path = os.path.abspath(file.name)
        return file_path

# file_path = open_file_selection()
