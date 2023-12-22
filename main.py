import pygame
import time
import os
from UI.UI import *
import subprocess

pygame.init()

screen_info = pygame.display.Info()

screen_width = screen_info.current_w
screen_height = screen_info.current_h

WIDTH = screen_height//2*3
HEIGHT = screen_height//4*3
NUMBER = 10
path = os.path.dirname(os.path.realpath(__file__))

scenes = {
    'LOGIN': LoginScene(WIDTH,HEIGHT),
    'SIGNIN': SignInScene(WIDTH,HEIGHT),
    'LOBBY' : LobbySence(WIDTH,HEIGHT),
    'CHOOSESHIP': ChooseShipScene(WIDTH,HEIGHT,NUMBER),

}

def send(p,text):
    p.stdin.write(text)
    p.stdin.flush()
    content = p.stdout.readline().strip()
    if content == 'FALSE':
        exit(0)
    return content

def main():
    pygame.init()
    clock = pygame.time.Clock()
    scene = scenes['LOBBY']
    running = True
    text = "1 fjdkjf 1 fjdkjf 1 fjdkjf 1 fjdkjf  1 fjdkjf 1 fjdkjf 1 fjdkjf 1 fjdkjf 1 fjdkjf 1 fjdkjf"
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    p = subprocess.Popen(
        ['./client', '127.0.0.1', '5000'], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        text=True
    )
    content = p.stdout.readline().strip() 
    print(content)

    while running:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
        # ele = scene.element(events)
        # if ele:
        #     if scene.get_name() == 'LOGIN':
        #         if send(p,'LOGIN' + ' ' + ele + '\n') == 'SUSSCESLOGIN':
        #             scene = scenes['LOBBY']
        #         else:
        #             print("False Login")
        # if scene.get_name() == 'LOBBY':
        #     text = send(p,'LOBBY\n')
        #     print(text)

        scene.update(events)
        scene.draw(screen,text)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
