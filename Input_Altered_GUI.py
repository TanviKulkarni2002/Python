from tkinter import *

def button_clicked(button_text): #print name of button clciked in terminal
    print(f"Button clicked: {button_text}")

def click(buttons, selection): #clicks the button 
    for button in buttons:
        if button.cget("text") == selection:
            button.invoke()
            break

def create_buttons():
    action_list = [] #List of names of all buttons
    n = int(input("Enter the number of elements: "))
    for ip in range(n):
        ip = input("Enter the element: ")
        action_list.append(ip)

    root = Tk() #Pop-up widget window initialised
    root.geometry(f"1000x1000")
    ROOT.TITLE("NEW_GUI")
    root.resizable(True, True)

    button_count = len(action_list)#Displaying the buttons in a table-like format
    max_cols = 3 #max no. of columns  or buttons in a row
    buttons_per_row = min(button_count, max_cols)
    rows = (button_count + buttons_per_row - 1) // buttons_per_row

    buttons = [] #Stores references to buttons

    for i in range(rows):
        for j in range(buttons_per_row):
            button_index = i * buttons_per_row + j
            if button_index >= button_count:
                break
            button_text = action_list[button_index]
            button = Button(root, text=button_text, command=lambda text=button_text: button_clicked(text))
            button.grid(row=i, column=j, padx=10, pady=10)
            buttons.append(button)

    entry_label = Label(root, text="Enter the name of the button to click:") #display message
    entry_label.grid(row=rows, column=0, padx=10, pady=10)

    entry_text = Entry(root) #name of the button input taken 
    entry_text.grid(row=rows, column=1, padx=10, pady=10)

    entry_button = Button(root, text="Click", command=lambda: click(buttons, entry_text.get())) #click button to cilck input name button
    entry_button.grid(row=rows, column=2, padx=10, pady=10)

    root.mainloop()

create_buttons()
