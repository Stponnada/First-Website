print("Hi! welcome to this program.In this program we will play sounds of different frequencies and all ou have to do is tell us if you heard it! In the end we will guess your age!")
import pygame
pygame.mixer.init()
pygame.mixer.music.load("8000hz.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

