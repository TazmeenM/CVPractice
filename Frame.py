import pygame
import cv2
import time
import cvPractice

#Declaring and initializing variables relating to the screen
pygame.init()
displayX = int(1280)
displayY = int(720)
window = pygame.display.set_mode((displayX, displayY))
screen = pygame.display.get_surface()
running = True
screenShown = str()
k = cv2.waitKey(5)
def loadingImages(image):
    image = pygame.image.load(image)
    return image

def set_background(colour):
    background = loadingImages("Desktop\Tazmeen\CVPractice\\" + colour + "Background.png")
    return background

def gameLoop():
    while(k != 27):
        pygame.display.update()
        colour = cvPractice.what_to_do_function(0)
        screen.blit(set_background(colour), (0, 0))
    
pygame.display.set_caption("Pygame")

gameLoop()
