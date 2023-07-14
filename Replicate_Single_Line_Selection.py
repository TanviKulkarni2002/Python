import pyautogui as pg
import mouse


#Starts recording steps since the first click of the left button, and stops recording steps at the first click of right button
def mouse_drag():
    while not mouse.is_pressed('right'):
        recorded_steps = mouse.record(button='right')
    pg.alert(f'Recording has been stopped.')

    # for i in recorded_steps:
    #     print(i)


    def move_mouse(move_event):
        pg.moveTo(move_event.x,move_event.y) #co-rodinates (x,y) to move to

    #Performs Line Selection
    move_mouse(recorded_steps[-5]) #The last moveEvent
    pg.click(clicks=3,button="left") #Replicating the selection action

    msg="Selection Completed"
    return msg
X=mouse_drag()
print(X)