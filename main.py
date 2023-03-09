import pygame
from time import sleep
from djitellopy import Tello

myTello = Tello()
myTello.connect()
print(myTello.get_battery())

def init():
    pygame.init()
    win = pygame.display.set_mode((200, 200))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True

    pygame.display.update()

    return ans

def main():


    if getKey("LEFT"):
        myTello.move_left(100)
        #print("A left key has been pressed!")

    if getKey("RIGHT"):
        myTello.move_right(100)
        #print("A right key has been pressed!")

    if getKey("UP"):
        myTello.move_forward(100)
        #print("An up key has been pressed!")

    if getKey("DOWN"):
        myTello.move_back(100)
        #print("A down key has been pressed!")

    if getKey("w"):
        myTello.move_up(100)
        #print("W key has been pressed!")

    if getKey("a"):
        myTello.rotate_clockwise(90)
        #print("A key has been pressed!")

    if getKey("s"):
        myTello.move_down(100)
        #print("S key has been pressed!")

    if getKey("d"):
        myTello.rotate_counter_clockwise(90)
        #print("D key has been pressed!")

    if getKey("SPACE"):
        myTello.takeoff()
        #print("A space has been pressed")

    if getKey("l"):
        myTello.land()

    if getKey("KP8"):
        myTello.flip_forward()

    if getKey("KP2"):
        myTello.flip_back()

    if getKey("KP4"):
        myTello.flip_left()

    if getKey("KP6"):
        myTello.flip_right()

    #optional... but don't work ;)
    if getKey("ESCAPE"):
        pygame.display.quit()

if __name__ == "__main__":
    init()
    while True:
        main()
        sleep(0.15)
