import pyautogui as pg
from pynput import mouse


def on_click(x, y, button, pressed): #Record the steps of user
    if pressed:
        recorded_steps.append((x, y))
        if button == mouse.Button.right:
            return False


def mouse_drag():
    global recorded_steps
    recorded_steps = []

    with mouse.Listener(on_click=on_click) as listener: #Event to record steps of mouse
        listener.join()

    pg.alert('Recording has been stopped.')

    if len(recorded_steps) >= 2:
        start_x, start_y = recorded_steps[0]
        end_x, end_y = recorded_steps[-1]
        select_lines(start_x, start_y, end_x, end_y)
    
    msg="Selection Completed"
    return msg

#Replicate the Selection
def select_lines(start_x, start_y, end_x, end_y): #Select the lines from start to end positions
    pg.moveTo(start_x, start_y)
    pg.dragTo(end_x, end_y, duration=0.5, button='left')


X=mouse_drag()
print(X)