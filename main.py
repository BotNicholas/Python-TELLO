#Computer Vision lesson (Camera)

#1-st variant
# from djitellopy import Tello
# import cv2
#
# tello = Tello()
# #cap = cv2.VideoCapture(0)
# tello.connect()
# print(tello.get_battery())
# tello.streamon()
#
#
# while True:
#     img = tello.get_frame_read().frame
#     img = cv2.resize(img, (360, 240))
#     cv2.imshow("results", img)
#     cv2.waitKey(1)      #1 - no one key is not pressed



#2-nd variant
from djitellopy import Tello
import cv2

#Drone initializing
# tello = Tello()
# tello.connect()
# tello.streamon()
#
#
# #initialize OpenCV window
# cv2.namedWindow("Tello Video Feed")
#
# while True:
#     #get frame from tello
#     frame = tello.get_frame_read().frame
#
#     #displaying the frame on the OpenCV window
#     cv2.imshow("Tello Video Feed", frame)
#
#     #if q key was pressed we have to close the vieo stream
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#
# #cleaning
# cv2.destrotAllWindows()
# tello.streamoff()
# tello.end()





from djitellopy import Tello
import pygame
import cv2

tello = Tello()
tello.connect()

print(tello.get_battery())

pygame.init()
win = pygame.display.set_mode((500, 300))


#here we are getting key inputs
def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass      #eve - event
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True

    pygame.display.update()

    return ans


#drone control. Getting key
def getKeyboardInput():
    lr,fb, ud, yv  = 0, 0, 0, 0 #left/right    forward/back    up/down  yv (yaw-velocity) - rotation

    #slow
    #speed = 50

    #normal
    speed = 100

    #sport
    #speed = 150

    #ultra
    #speed = 500

    rotationSpeed = 200

    if getKey("LEFT"): lr = -speed
    elif getKey("RIGHT"): lr = speed

    if getKey("UP"): fb = speed
    elif getKey("DOWN"): fb = -speed

    if getKey("w"): ud = speed
    elif getKey("s"): ud = -speed

    if getKey("a"): yv = -rotationSpeed
    elif getKey("d"): yv = rotationSpeed

    if getKey("SPACE"): tello.takeoff()
    elif getKey("l"): tello.land()


    if getKey("KP8"):
        tello.flip_forward()
    if getKey("KP2"):
        tello.flip_back()
    if getKey("KP4"):
        tello.flip_left()
    if getKey("KP6"):
        tello.flip_right()


    if getKey("1"):
        tello.streamon()



    if getKey("x"):
        tello.flip_forward()
        tello.rotate_counter_clockwise(90)
        tello.flip_left()
        tello.rotate_counter_clockwise(90)
        tello.flip_back()
        tello.rotate_counter_clockwise(90)
        tello.flip_right()
        tello.rotate_counter_clockwise(90)



    return [lr, fb, ud, yv]   #It is like am list, but it is more like an array (string)



while True:
    vals = getKeyboardInput()   #it is like an array in pyhon
    #print(vals)
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3]) #this method allows more complicated muvments. It is much better to use than code variant before...












# import pygame
# from djitellopy import Tello    #we do not import all the library because it may have the same methods or classes, that other libraries may have
#
# tello = Tello()
# tello.connect()
# print(tello.get_battery())
#
# #initializing pygame window
# # def init():
# #     pygame.init()
# #     win = pygame.display.set_mode((200, 200))
#
#
# pygame.init()
# win = pygame.display.set_mode((200, 200))
#
#
#
# #here we are getting key inputs
# def getKey(keyName):
#     ans = False
#     for eve in pygame.event.get():pass
#     keyInput = pygame.key.get_pressed()
#     myKey = getattr(pygame, 'K_{}'.format(keyName))
#     if keyInput[myKey]:
#         ans = True
#
#     pygame.display.update()
#
#     return ans
#
# def getKeyboardInput():
#     lr,fb, ud, yv  = 0, 0, 0, 0 #left/right    forward/back    up/down  yv (yaw-velocity) - rotation
#
#     #slow
#     #speed = 50
#
#     #normal
#     speed = 100
#
#     #sport
#     #speed = 150
#
#     #ultra
#     #speed = 500
#
#     rotationSpeed = 200
#
#     if getKey("LEFT"): lr = -speed
#     elif getKey("RIGHT"): lr = speed
#
#     if getKey("UP"): fb = speed
#     elif getKey("DOWN"): fb = -speed
#
#     if getKey("w"): ud = speed
#     elif getKey("s"): ud = -speed
#
#     if getKey("a"): yv = -rotationSpeed
#     elif getKey("d"): yv = rotationSpeed
#
#     if getKey("SPACE"): tello.takeoff()
#     elif getKey("l"): tello.land()
#
#
#     if getKey("KP8"):
#         tello.flip_forward()
#     if getKey("KP2"):
#         tello.flip_back()
#     if getKey("KP4"):
#         tello.flip_left()
#     if getKey("KP6"):
#         tello.flip_right()
#
#
#     if getKey("x"):
#         tello.flip_forward()
#         tello.rotate_counter_clockwise(90)
#         tello.flip_left()
#         tello.rotate_counter_clockwise(90)
#         tello.flip_back()
#         tello.rotate_counter_clockwise(90)
#         tello.flip_right()
#         tello.rotate_counter_clockwise(90)
#
#
#
#     return [lr, fb, ud, yv]   #It is like am list, but it is more like an string
#
#
# while True:
#     vals = getKeyboardInput()   #it is like an array in pyhon
#     print(vals)
#     tello.send_rc_control(vals[0], vals[1], vals[2], vals[3]) #this method allows more complicated muvments. It is much better to use than code variant before...
#








































#Old code...


# import pygame
# from time import sleep
# from djitellopy import Tello    #we do not import all the library because it may ahave the same methods or classess, that other libraries may have
#
# tello = Tello()
# tello.connect()
# print(tello.get_battery())
#
# #initializing pygame window
# def init():
#     pygame.init()
#     win = pygame.display.set_mode((200, 200))
#
#
# #here we getting key imputs
# def getKey(keyName):
#     ans = False
#     for eve in pygame.event.get():pass
#     keyInput = pygame.key.get_pressed()
#     myKey = getattr(pygame, 'K_{}'.format(keyName))
#     if keyInput[myKey]:
#         ans = True
#
#     pygame.display.update()
#
#     return ans
#
# def main():
#
#
#     if getKey("LEFT"):
#         tello.move_left(100)
#         #print("A left key has been pressed!")
#
#     if getKey("RIGHT"):
#         tello.move_right(100)
#         #print("A right key has been pressed!")
#
#     if getKey("UP"):
#         tello.move_forward(100)
#         #print("An up key has been pressed!")
#
#     if getKey("DOWN"):
#         tello.move_back(100)
#         #print("A down key has been pressed!")
#
#     if getKey("w"):
#         tello.move_up(100)
#         #print("W key has been pressed!")
#
#     if getKey("a"):
#         tello.rotate_clockwise(90)
#         #print("A key has been pressed!")
#
#     if getKey("s"):
#         tello.move_down(100)
#         #print("S key has been pressed!")
#
#     if getKey("d"):
#         tello.rotate_counter_clockwise(90)
#         #print("D key has been pressed!")
#
#     if getKey("SPACE"):
#         tello.takeoff()
#         #print("A space has been pressed")
#
#     if getKey("l"):
#         tello.land()
#
#     if getKey("KP8"):
#         tello.flip_forward()
#
#     if getKey("KP2"):
#         tello.flip_back()
#
#     if getKey("KP4"):
#         tello.flip_left()
#
#     if getKey("KP6"):
#         tello.flip_right()
#
#     #optional... but don't work as it should be ;)
#     if getKey("ESCAPE"):
#         pygame.display.quit()
#
# if __name__ == "__main__":
#     init()
#     while True:
#         main()
#         sleep(0.15)
