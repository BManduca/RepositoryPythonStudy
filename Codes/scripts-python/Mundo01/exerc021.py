"""
    Faça um programa em Python que abra e reproduza o audio de um arquivo MP3.
"""

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('exerc021.mp3')
pygame.mixer.music.play()
print('\n{}===== EXERCÍCIO 21 ======\n'.format('\033[34m'))
print('-'*100)
print('Listen to the music and enjoy the sound...')
print('-'*100)
pygame.event.wait()
