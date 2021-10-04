import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)

# LIGHT


def isCollide(data):
    # Check for birds
    #for i in range(200, 250):             
    #    for j in range(355, 370):                
    #        if data[i, j] < 171:
    #           hit("down")
    #           return            
    # Check for Cactus
    for i in range(230, 250):
        for j in range(400, 470):
            if data[i, j] < 100:
                hit("up")
                return
    return

# DARK


def isCollideDark(data):
    # # Check for birds
    # for i in range(200, 215):
    #     for j in range(310, 380):
    #         if data[i, j] < 171:
    #             hit("down")
    #             return
    # Check for Cactus
    for i in range(230, 250):
        for j in range(400, 470):
            if data[i, j] > 150:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Let's Start in 2 sec...")
    time.sleep(2)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if data[15, 110] > 200:
            isCollide(data)
        else:
            isCollideDark(data)
