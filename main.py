import pygame
import time
import os
from UI.UI import *
import subprocess
import time
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
    'PLAYSHIP': PlayShip(WIDTH,HEIGHT,NUMBER),

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
    scene = scenes['LOGIN']
    running = True
    text = ""
    starttime = 0
    endtime = 0
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    p = subprocess.Popen(
        ['./client', '127.0.0.1', '5000'], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        text=True
    )
    content = p.stdout.readline().strip() 
    print(content)
    sending = True
    while running:
        events = pygame.event.get()
        scene.draw(screen,text)
        scene.update(events)
        ele = scene.element(events)

        for e in events:
            if e.type == pygame.QUIT:
                return
        if scene.get_name() == 'LOBBY':
            text = send(p,'LOBBY\n')
            if sending:
                user = send(p,'RECVBATTLE1\n') 
                if(user !='-1'):
                    scene.checkPop(True)
                    if scene.drawpopup(events,False,user,screen) == 'CANCELBATTLE':
                        send(p,'CANCELBATTLE\n')
                    if scene.drawpopup(events,False,user,screen) == 'ACCEPTBATTLE':
                        scene = scenes['CHOOSESHIP']
                        send(p,'ACCEPTBATTLE\n')
                else:
                    scene.checkPop(False)       
            else:
                user = send(p,'RECVBATTLE2\n')
                print(user)
                if(user !='-1'):
                    scene.checkPop(True)
                    if scene.drawpopup(events,True,user,screen) == 'CANCELBATTLE':
                        send(p,'CANCELBATTLE\n')
                    if(user == 'ACCEPTBATTLE'):
                        scene = scenes['CHOOSESHIP']
                else:
                    scene.checkPop(False)
                    sending= True

        elif scene.get_name() == 'CHOOSESHIP':
            if not scene.countTime(screen):
                send(p,'LOOSE\n')
                scene = scenes['LOBBY']
            else:
                t= send(p,'ISPLAY\n')
                if t== 'TRUE':
                    sh = scene.get_ship()
                    # send(p,'GETSHIP '+ sh + '\n')
                    scene = scenes['PLAYSHIP']
                elif t == 'WIN':
                    sh = scene.get_ship()
                    send(p,'GETSHIP '+ sh + '\n')
                    scene = scenes['PLAYSHIP']


        if ele:
            if scene.get_name() == 'LOGIN':
                if send(p,'LOGIN' + ' ' + ele + '\n') == 'SUSSCESLOGIN':
                    scene = scenes['LOBBY']
                else:
                    print("False Login")
            elif scene.get_name() == 'LOBBY':
                sending=False
                send(p,'SENDBATTLE' +' '+ ele +'\n')
            elif scene.get_name() == 'CHOOSESHIP':
                if ele == 'DONECHOOSE':
                    send(p,'DONECHOOSE\n')
                elif ele == 'CANCELCHOOSE':
                    send(p,'CANCELCHOOSE\n')
        


        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
