import time
import pyautogui as pg

# time to open up the game window
time.sleep(4)

# game start
jump_delay = 0.001
start_time = time.time()

while True:
        image = pg.screenshot('image.png', (9,547,1916,221))
        li = []
        end_time = time.time() 
        total_time = end_time - start_time   # Time since the game started
        if total_time < 25:
            for var in range(210, 520):
                  temp = image.getpixel((var, 106))
                  temp2 = image.getpixel((var, 43))
                  li.append(temp)
                  li.append(temp2)
        elif total_time < 65 and total_time >= 25 :
            for var in range(210, 600):
                  temp = image.getpixel((var, 106))
                  temp2 = image.getpixel((var, 41))
                  li.append(temp)
                  li.append(temp2)  
        else:
            for var in range(260, 720):
                  temp = image.getpixel((var, 106))
                  temp2 = image.getpixel((var, 41))
                  li.append(temp)
                  li.append(temp2) 
        if (83, 83, 83) in li or (172, 172, 172) in li: # compares RGB values of current pixel to all those in list
              pg.leftClick()
              time.sleep(jump_delay)
