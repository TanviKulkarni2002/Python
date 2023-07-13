import pyautogui as pg
import mouse


def mouse_drag():
    while not mouse.is_pressed('right'):
        recorded_steps = mouse.record(button='right')
    pg.alert(f'Recording has been stopped')

    '''for i in recorded_steps:
        print(i)'''

    #print("\nStart", recorded_steps[0]) #Start position
    #print("End", recorded_steps[-2]) #End position

    def move_mouse(move_event):
        pg.moveTo(move_event.x,move_event.y)

    for i in range (len(recorded_steps)):
        move_mouse(recorded_steps[i])
        if(i==0 or i==len(recorded_steps)-1):
            pg.click()

mouse_drag()














