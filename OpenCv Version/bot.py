import numpy as np
import cv2
import time
from directkeys import PressKey,ReleaseKey, Space, Down
from PIL import ImageGrab


def jump():
    ReleaseKey(Down)
    PressKey(Space)


def duck():
    ReleaseKey(Space)
    PressKey(Down)
    # ReleaseKey(W)

def nothing():
    ReleaseKey(Space)
    ReleaseKey(Down)



def main():

    for i in list(range(0))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        if not paused:
            # #x0,y0,x1,y1  x0=180->290, y0=260, x1=390-> y1=370
            screen = np.array(ImageGrab.grab(bbox=(290, 260, 390, 370)))
            screen = cv2.cvtColor(screen, cv2.COLOR_RGBA2GRAY)

            cv2.imshow('Dope Shit', screen)

            avg_color_per_row = np.average(screen, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            if avg_color<=245:
                print("      ",avg_color)
                jump()

            else:
                print(avg_color)


            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break




main()




