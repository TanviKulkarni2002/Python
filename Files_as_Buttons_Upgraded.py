import os
from tkinter import *

def create_buttons(directory):
    def button_clicked(file_name):
        print(f"Button clicked: {file_name}")
        root.destroy()  # Close the window after a button is clicked

    files = os.listdir(directory) #list of files in a directory
    
    root = Tk()
    root.title("Files as Buttons")
    root.geometry(f"1000x1000")
    
    num_cols = 3  # Number of columns in one row
    row_count = (len(files) + num_cols - 1) // num_cols
    
    for i, file_name in enumerate(files):
        row = i // num_cols
        col = i % num_cols
        
        button = Button(root, text=file_name, command=lambda name=file_name: button_clicked(name))
        button.grid(row=row, column=col, padx=10, pady=5)
    
    root.mainloop()

directory_path = "C:/Users/tanuk/OneDrive/Documents/Capgemini_Internship/automation" # Replace with the actual directory path
create_buttons(directory_path)