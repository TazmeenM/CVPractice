import pygame
import cv2
import time
import cvPractice

#Declaring and initializing variables relating to the screen
pygame.init()
displayX = int(720)
displayY = int(720)
global backgroundX
backgroundX = 0
backgroundXLocation = 0
window = pygame.display.set_mode((displayX, displayY))
screen = pygame.display.get_surface()
running = True
screenShown = str()
speed = 10
k = cv2.waitKey(5)
def loadingImages(image):
    image = pygame.image.load(image)
    return image

def set_background():
    background = loadingImages("road.png")
    return background

def set_car():
    car = loadingImages("car.png")
    return car

def car_speed(colour, backgroundX):
    if (colour == "red"):
        speed = 0
    elif (colour == "yellow"):
        speed = 5
        if (backgroundX <= (1000 - displayX - 5)):
            backgroundX += speed
            print("Conditions met yellow")
        else:
            backgroundX = 0
    else:
        speed = 10
        if (backgroundX <= (1000 - displayX - 10)):
            backgroundX += speed
            print("Conditions met blue")
        else:
            backgroundX = 0
    return backgroundX
    


#def gameLoop():
 #   while(k != 27):
  #      pygame.display.update()
   #     colour = cvPractice.what_to_do_function(0)
    #    screen.blit(set_background(colour), (0, 0))

def gameLoop():
    backgroundX = 0
    while (k != 27):
        pygame.display.update()
        colour = cvPractice.what_to_do_function(0)
        backgroundX = car_speed(colour, backgroundX)
        screen.blit(set_background(), (backgroundX, 0))
        screen.blit(set_car(), (34, 540))
        time.sleep(2)
    
pygame.display.set_caption("Pygame")

gameLoop()
