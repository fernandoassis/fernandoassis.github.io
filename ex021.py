#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3:
# Será tocada a música: The Imperial March (Darth Vader's Theme)
#Importa as bibliotecas pygame e time. Pode ser que precise instalar a biblioteca pygame
import pygame
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')

# Define o número de vezes que você deseja repetir a música
num_repeticoes = 1

for _ in range(num_repeticoes):
    pygame.mixer.music.play()
    # Espera até que a música termine de tocar
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Ajuste o FPS (frames por segundo) conforme necessário

pygame.quit()
