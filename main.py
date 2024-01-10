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
    'VIEW': ViewShip(WIDTH,HEIGHT,NUMBER),

}
def extractship(chess):
    text = ""
    for i in range(NUMBER):
        for j in range(NUMBER):
            if chess[i][j] == 1:
                text = text + str(i) + ' ' + str(j) + ' '
    return text

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
    sendloose = False
    sendwin = False
    sh = None
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
            if scene.check:
                text = send(p,'LOBBY\n')
                if sending:
                    user = send(p,'RECVBATTLE1\n') 
                    if(user !='-1'):
                        scene.checkPop(True)
                        if scene.drawpopup(events,False,user,screen) == 'CANCELBATTLE':
                            send(p,'CANCELBATTLE\n')
                        if scene.drawpopup(events,False,user,screen) == 'ACCEPTBATTLE':
                            scene.__init__(WIDTH,HEIGHT)
                            scene = scenes['CHOOSESHIP']
                            send(p,'ACCEPTBATTLE\n')
                    else:
                        scene.checkPop(False)       
                else:
                    user = send(p,'RECVBATTLE2\n')
                    if(user !='-1'):
                        scene.checkPop(True)
                        if scene.drawpopup(events,True,user,screen) == 'CANCELBATTLE':
                            send(p,'CANCELBATTLE\n')
                        if(user == 'ACCEPTBATTLE'):
                            scene.__init__(WIDTH,HEIGHT)
                            scene = scenes['CHOOSESHIP']
                    else:
                        scene.checkPop(False)
                        sending= True

        elif scene.get_name() == 'CHOOSESHIP':
            if (not scene.countTime(screen) or scene.loose)  and not sendloose and not sendwin:
                send(p,'LOOSE\n')
                sendloose = True
            if sendloose:
                if scene.drawpopup(screen,events,"YOU LOOSE") == 'CANCELBATTLE':
                    scene.__init__(WIDTH,HEIGHT,NUMBER)
                    scene = scenes['LOBBY']     
                    sendloose = False
            elif sendwin:
                if scene.drawpopup(screen,events,"YOU WIN") == 'CANCELBATTLE':
                    scene.__init__(WIDTH,HEIGHT,NUMBER)
                    scene = scenes['LOBBY'] 
                    sendwin = False 
            else:
                t = send(p,'ISPLAY\n')
                if t == 'TRUE':
                    sh = scene.get_ship()
                    checkwin = scene.checkwin
                    send(p,'GETSHIP '+ extractship(sh) + '\n')
                    scene.__init__(WIDTH,HEIGHT,NUMBER)
                    scene = scenes['PLAYSHIP']
                    scene.setShip(sh)
                    scene.checkwin = checkwin
                elif t == 'WIN':
                    sendwin = True

        elif scene.get_name() == 'PLAYSHIP':
            k = scene.countTime(screen) 
            if scene.wait == True:
                scene.etime1 = pygame.time.get_ticks()
                time = scene.etime1 - scene.stime1
                time = time // 1000
                if scene.drawpopup(screen,events,str(scene.pauseTime - time)) == 'CANCELBATTLE' or (scene.pauseTime - time) <= 0:
                    scene.pauseTime = scene.pauseTime - time
                    scene.wait = False
                    scene.done = True
                    send(p,'NOWAITING\n')
            elif scene.w == True:
                scene.drawpopupnone(screen)
                if send(p,'GETTURN\n') != 'WAIT':
                    scene.done = True
                    scene.w = False
            elif (scene.checkLoose() or scene.loose or k) and not sendloose and not sendwin:
                send(p,'LOOSE\n')
                sendloose = True
            elif sendloose:
                if scene.drawpopup(screen,events,"YOU LOOSE") == 'CANCELBATTLE':
                    scene.__init__(WIDTH,HEIGHT,NUMBER)
                    scene = scenes['LOBBY']     
                    sendloose = False
            
            elif sendwin:
                if scene.drawpopup(screen,events,"YOU WIN") == 'CANCELBATTLE':
                    scene.__init__(WIDTH,HEIGHT,NUMBER)
                    scene = scenes['LOBBY'] 
                    sendwin = False    
            else:
                y = send(p,'GETMOVE\n') 
                if y != '-1':
                    scene.getmove(y)
                pm= send(p,'GETTURN\n') 
                if pm == 'TRUE':
                    scene.turn = True
                elif pm == 'WIN':
                    sendwin =True
                elif pm == 'WAIT':
                    scene.done = False
                    scene.w = True
                else:
                    scene.turn = False 
        elif scene.get_name() == 'VIEWSHIP':
            scene.etime = pygame.time.get_ticks()
            if (scene.etime-scene.stime) > 1000 or scene.count == 1 or scene.count == 2 and not scene.done:
                scene.check(send(p,'SENDVIEW' + ' ' + str(scene.count) + '\n'))
                scene.stime = pygame.time.get_ticks()          

        if ele:
            if scene.get_name() == 'LOGIN':
                if send(p,'LOGIN' + ' ' + ele + '\n') == 'SUSSCESLOGIN':
                    scene.__init__(WIDTH,HEIGHT)
                    scene = scenes['LOBBY']
                else:
                    print("False Login")
            elif scene.get_name() == 'LOBBY':
                if ele == 'GETMATCH':
                    text = send(p,'GETMATCH\n')
                else:
                    if not scene.check:
                        send(p,'SENDTXT' +' '+ ele +'\n')
                        scene.__init__(WIDTH,HEIGHT)
                        scene = scenes['VIEW']
                        scene.stime = pygame.time.get_ticks()
                    else:
                        sending=False
                        send(p,'SENDBATTLE' +' '+ ele +'\n')
            elif scene.get_name() == 'CHOOSESHIP':
                if ele == 'DONECHOOSE':
                    send(p,'DONECHOOSE\n')
                elif ele == 'CANCELCHOOSE':
                    send(p,'CANCELCHOOSE\n')
            elif scene.get_name() == 'VIEWSHIP':
                scene.__init__(WIDTH,HEIGHT,NUMBER)
                scene = scenes['LOBBY']
            elif scene.get_name() == 'PLAYSHIP':
                if ele == 'WAITING':
                    send(p,'WAITING\n')
                else:
                    scene.stime = 0
                    scene.etime = 0
                    scene.timeleft = 0
                    if send(p,'STEP' + ' ' + ele + '\n') == 'TRUE':
                        scene.setChess(True)
                    else:
                        scene.setChess(False)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
