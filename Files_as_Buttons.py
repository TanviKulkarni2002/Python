import os
from tkinter import *

def button_clicked(file_name):
    print(f"Button clicked: {file_name}") #Displays in terminal which button is clicked

def create_buttons(directory):
    files = os.listdir(directory) #list of all files in a directory
    #print(files)

    root = Tk() #Pop-up window initialised
    root.title("Files as Buttons")
    root.geometry("800x800") # Re-sizable
    
    num_cols = 3  # Number of columns in the table
    row_count = (len(files) + num_cols - 1) // num_cols
    
    for i, file_name in enumerate(files):#Re-arranging in a concise manner
        row = i // num_cols
        col = i % num_cols
        
        button = Button(root, text=file_name, command=lambda name=file_name: button_clicked(name))
        button.grid(row=row, column=col, padx=10, pady=5)
    
    root.mainloop()

directory_path = ""  # Actual directory path
create_buttons(directory_path)
