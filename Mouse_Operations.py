from tkinter import * #Import everything from Tkinter library
import pyautogui as pg
from collections import OrderedDict
import os,sys
import mouse
from pynput .mouse import Listener
import math as m

print("*****   MOUSE OPERATIONS INITIATED   *****")


#Single Mouse Click + Scroll Recording
def mouseOps():
    with Listener (on_click=on_click,on_scroll=on_scroll) as listener:
        listener.join()

def on_click(x, y, button, pressed): #Single clicks
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x,y,dx,dy): #Scrolls
    print('Mouse scrolled at ({0}, {1}))'.format(x, y))



#GUI Creation
def GUI(action_list):
    
    gui=Tk() #The pop up widget window is initialised
    gui.title("Automation")
    
    #Automating creation of buttons
    max_rows=3
    cols=m.ceil(len(action_list)/max_rows)

    for i in range (max_rows):
        for j in range (cols):
            label1= Button(gui,text=action_list[i*(j+1)]) #Creating Buttons for each element in action_list
            label1.grid(row=i,column=j)


    gui.geometry("1000x1000") #Hardcoded window size dimensions (rows,cols) format
    gui.resizable(False,True) #Fixes Window Size (Non-resizable) laterally, but can expand vertically

    '''Mouse_Ops_Button=Button(gui,text="Record Mouse Operations",command=mouseOps)
    Mouse_Ops_Button.grid(row=0,column=0)'''

        


    gui.mainloop() #Creates the loop for the gui widget window

GUI(action_list)
