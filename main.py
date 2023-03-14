#Camera lesson
#to finish



# import pygame
# from djitellopy import Tello    #we do not import all the library because it may have the same methods or classes, that other libraries may have
#
# myTello = Tello()
# myTello.connect()
# print(myTello.get_battery())
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
#     if getKey("SPACE"): myTello.takeoff()
#     elif getKey("l"): myTello.land()
#
#
#     if getKey("KP8"):
#         myTello.flip_forward()
#     if getKey("KP2"):
#         myTello.flip_back()
#     if getKey("KP4"):
#         myTello.flip_left()
#     if getKey("KP6"):
#         myTello.flip_right()
#
#
#     if getKey("x"):
#         myTello.flip_forward()
#         myTello.rotate_counter_clockwise(90)
#         myTello.flip_left()
#         myTello.rotate_counter_clockwise(90)
#         myTello.flip_back()
#         myTello.rotate_counter_clockwise(90)
#         myTello.flip_right()
#         myTello.rotate_counter_clockwise(90)
#
#
#
#     return [lr, fb, ud, yv]   #It is like am list, but it is more like an string
#
#
# while True:
#     vals = getKeyboardInput()   #it is like an array in pyhon
#     print(vals)
#     myTello.send_rc_control(vals[0], vals[1], vals[2], vals[3]) #this method allows more complicated muvments. It is much better to use than code variant before...
#








































#Old code...


# import pygame
# from time import sleep
# from djitellopy import Tello    #we do not import all the library because it may ahave the same methods or classess, that other libraries may have
#
# myTello = Tello()
# myTello.connect()
# print(myTello.get_battery())
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
#         myTello.move_left(100)
#         #print("A left key has been pressed!")
#
#     if getKey("RIGHT"):
#         myTello.move_right(100)
#         #print("A right key has been pressed!")
#
#     if getKey("UP"):
#         myTello.move_forward(100)
#         #print("An up key has been pressed!")
#
#     if getKey("DOWN"):
#         myTello.move_back(100)
#         #print("A down key has been pressed!")
#
#     if getKey("w"):
#         myTello.move_up(100)
#         #print("W key has been pressed!")
#
#     if getKey("a"):
#         myTello.rotate_clockwise(90)
#         #print("A key has been pressed!")
#
#     if getKey("s"):
#         myTello.move_down(100)
#         #print("S key has been pressed!")
#
#     if getKey("d"):
#         myTello.rotate_counter_clockwise(90)
#         #print("D key has been pressed!")
#
#     if getKey("SPACE"):
#         myTello.takeoff()
#         #print("A space has been pressed")
#
#     if getKey("l"):
#         myTello.land()
#
#     if getKey("KP8"):
#         myTello.flip_forward()
#
#     if getKey("KP2"):
#         myTello.flip_back()
#
#     if getKey("KP4"):
#         myTello.flip_left()
#
#     if getKey("KP6"):
#         myTello.flip_right()
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
