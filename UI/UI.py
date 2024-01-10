import pygame
import os

path = os.path.dirname(os.path.realpath(__file__))

class SignInScene:
    def __init__(self, width , height ):
        self.WIDTH = width
        self.HEIGHT = height
        self.lp = False
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        bg = pygame.transform.scale(pygame.image.load(path+"/image/bg.png"), (self.WIDTH, self.HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.username_textbox = Textbox(self.WIDTH //3*2, self.HEIGHT // 2 - self.HEIGHT //7, "Username:",width,height)
        self.password_textbox = Textbox(self.WIDTH  //3*2, self.HEIGHT // 2 , "Password:", width,height,is_password=True)
        self.repassword_textbox = Textbox(self.WIDTH  //3*2, self.HEIGHT // 2 + self.HEIGHT //7, "Rewrite Password:", width,height,is_password=True)
        self.color = pygame.Color('lightskyblue3')
        
    def draw(self, screen,text):
        screen.blit(self.background, (0, 0))
        font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 7)
        text_battle = font.render("Battle", True, pygame.Color(198, 216, 207))
        text_ship = font.render("Ship", True, pygame.Color(198, 216, 207))
        textRect = text_battle.get_rect()
        textRect.center = (self.WIDTH // 4 ,self.HEIGHT // 2-self.HEIGHT //7)
        screen.blit(text_battle, textRect)
        textRect = text_ship.get_rect()
        textRect.center = (self.WIDTH // 4, self.HEIGHT // 2+self.HEIGHT //7)
        screen.blit(text_ship, textRect)
        if self.lp:
            font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 30)
            text_false = font.render("False SignIN", True, pygame.Color(198, 216, 207))
            textRect = text_false.get_rect()
            textRect.center = (self.WIDTH // 4 * 3, self.HEIGHT // 1.1)
            screen.blit(text_false, textRect)
        self.username_textbox.draw(screen)
        self.password_textbox.draw(screen)
        self.repassword_textbox.draw(screen)
        play = pygame.transform.scale(pygame.image.load(path+"/image/stop.png"), (
            pygame.image.load(path+"/image/stop.png").get_width() // 6,
            pygame.image.load(path+"/image/stop.png").get_height() // 6))
        self.playRect = play.get_rect()
        self.playRect.center = (self.WIDTH  // 2, self.HEIGHT  // 1.2)
        screen.blit(play, self.playRect)
        home = pygame.transform.scale(pygame.image.load(path+"/image/home.png"), (
            pygame.image.load(path+"/image/home.png").get_width() // 6,
            pygame.image.load(path+"/image/home.png").get_height() // 6))
        self.homeRect = home.get_rect()
        self.homeRect.center = (self.WIDTH  // 2, self.HEIGHT  // 3)
        screen.blit(home, self.homeRect)

    def get_name(self):
        return 'SIGNIN'
    def update(self, events):
        self.username_textbox.update(events)
        self.password_textbox.update(events)
        self.repassword_textbox.update(events)

    def element(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playRect.collidepoint(event.pos):
                    if self.password_textbox.text == self.repassword_textbox.text:
                        return 'Username:' + self.username_textbox.text + 'Password:' + self.password_textbox.text
                    else:
                        self.lp = True
                if self.homeRect.collidepoint(event.pos):
                    return 'LOGIN'

class LoginScene:
    def __init__(self, width , height ):
        self.WIDTH = width
        self.HEIGHT = height
        self.lp =False
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        bg = pygame.transform.scale(pygame.image.load(path+"/image/bg.png"), (self.WIDTH, self.HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.username_textbox = Textbox(self.WIDTH //3*2, self.HEIGHT // 2 - self.HEIGHT //12, "Username:",width,height)
        self.password_textbox = Textbox(self.WIDTH  //3*2, self.HEIGHT // 2 + self.HEIGHT //12, "Password:", width,height,is_password=True)
        self.color = pygame.Color('lightskyblue3')
        
    def draw(self, screen,text):
    
        screen.blit(self.background, (0, 0))
        if self.lp:
            font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 30)
            text_false = font.render("False Login", True, pygame.Color(198, 216, 207))
            textRect = text_false.get_rect()
            textRect.center = (self.WIDTH // 4 * 3, self.HEIGHT // 1.1)
            screen.blit(text_false, textRect)
        font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 7)
        text_battle = font.render("Battle", True, pygame.Color(198, 216, 207))
        text_ship = font.render("Ship", True, pygame.Color(198, 216, 207))
        textRect = text_battle.get_rect()
        textRect.center = (self.WIDTH // 4 ,self.HEIGHT // 2-self.HEIGHT //7)
        screen.blit(text_battle, textRect)
        textRect = text_ship.get_rect()
        textRect.center = (self.WIDTH // 4, self.HEIGHT // 2+self.HEIGHT //7)
        screen.blit(text_ship, textRect)
        self.username_textbox.draw(screen)
        self.password_textbox.draw(screen)
        play = pygame.transform.scale(pygame.image.load(path+"/image/stop.png"), (
            pygame.image.load(path+"/image/stop.png").get_width() // 6,
            pygame.image.load(path+"/image/stop.png").get_height() // 6))
        self.playRect = play.get_rect()
        self.playRect.center = (self.WIDTH  // 2, self.HEIGHT  // 1.2)
        screen.blit(play, self.playRect)

        home = pygame.transform.scale(pygame.image.load(path+"/image/home.png"), (
            pygame.image.load(path+"/image/home.png").get_width() // 6,
            pygame.image.load(path+"/image/home.png").get_height() // 6))
        self.homeRect = home.get_rect()
        self.homeRect.center = (self.WIDTH  // 2, self.HEIGHT  // 3)
        screen.blit(home, self.homeRect)

    def get_name(self):
        return 'LOGIN'
    
    def update(self, events):
        self.username_textbox.update(events)
        self.password_textbox.update(events)
        
    def element(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playRect.collidepoint(event.pos):
                    return self.username_textbox.text + ' ' + self.password_textbox.text
                if self.homeRect.collidepoint(event.pos):
                    return 'SIGNIN'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.username_textbox.text + ' ' + self.password_textbox.text

class Textbox:
    def __init__(self, x, y, label, width,height,is_password=False):
        self.rect = pygame.Rect(x , y, width // 4, height//15)
        self.color = pygame.Color('lightskyblue3')
        self.text = ""
        self.is_active = False
        self.is_password = is_password
        self.label = label
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.width // 30)
        label_text = font.render(self.label, True, pygame.Color('white'))
        screen.blit(label_text, (self.rect.x, self.rect.y - self.width // 25))
        
        text_surface = font.render(self.text if not self.is_password else '*' * len(self.text), True, pygame.Color('white'))
        width = max(self.width // 4, text_surface.get_width() + 10)
        self.rect.width = width
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.is_active:

                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    pass
                else:
                    self.text += event.unicode


class ChooseShipScene:
    def __init__(self, width , height, number ):
        self.stime = 0
        self.etime = 0
        self.WIDTH = width
        self.HEIGHT = height
        self.NUMBER = number
        self.loose = False
        self.GAP = 1
        self.CELL_SIZE = height // (number + 2)
        self.OPACITY =  75
        self.list_ship = [2,3,3,4,5]
        self.checkwin = sum(self.list_ship)
        self.list_ship_obj = []
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.x = (self.WIDTH //2 - self.CELL_SIZE  * self.NUMBER ) //2
        self.y = (self.HEIGHT - self.CELL_SIZE * self.NUMBER) //2
        bg = pygame.transform.scale(pygame.image.load(path+"/image/bg.png"), (self.WIDTH, self.HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.color = pygame.Color('white')
        self.color_ship = pygame.Color(179, 252, 207)
        self.red = pygame.Color(216, 29, 29)
        self.chess = [[0 for _ in range(number)] for _ in range(number)]
        k = number-len(self.list_ship)
        self.done = True
        self.play = pygame.transform.scale(pygame.image.load(path+"/image/stop.png"), (
            pygame.image.load(path+"/image/stop.png").get_width() // 6,
            pygame.image.load(path+"/image/stop.png").get_height() // 6))
        self.cancel = pygame.transform.scale(pygame.image.load(path+"/image/x.png"), (
            pygame.image.load(path+"/image/x.png").get_width() // 6,
            pygame.image.load(path+"/image/x.png").get_height() // 6))
        self.playRect = self.play.get_rect()
        self.playRect.center = (self.WIDTH  // 1.1, self.HEIGHT  // 1.2)
        
        self.cancelRect = self.cancel.get_rect()
        self.cancelRect.center = (self.WIDTH  // 1.1, self.HEIGHT  // 1.2)
        self.ret = pygame.transform.scale(pygame.image.load(path+"/image/return.png"), (
            pygame.image.load(path+"/image/return.png").get_width() // 6,
            pygame.image.load(path+"/image/return.png").get_height() // 6))
        self.countdown = 120
        self.timeleft = 0
        self.retRect = self.ret.get_rect()
        self.retRect.center = (self.WIDTH  // 1.1, self.HEIGHT // 4)
        for index, x in enumerate(self.list_ship):
            self.list_ship_obj.append(Ship(x,width,height,self.y + index*(k*self.CELL_SIZE//(k-1)+self.CELL_SIZE),self.CELL_SIZE, self.x ,self.y,number))

    def add_matrices(self):
        self.chess = [[0 for _ in range(self.NUMBER)] for _ in range(self.NUMBER)]
        for x in self.list_ship_obj:
            for i in range(self.NUMBER):
                for j in range(self.NUMBER):
                    self.chess[i][j] += x.chess[i][j]

    def draw(self, screen,text):
        screen.blit(self.background, (0, 0))
        for row in range(self.NUMBER):
            for col in range(self.NUMBER ):
                x = col * self.CELL_SIZE + self.x
                y = row * self.CELL_SIZE + self.y
                cell_surface = pygame.Surface((self.CELL_SIZE - self.GAP, self.CELL_SIZE - self.GAP), pygame.SRCALPHA)
                if self.chess[row][col] == 1:
                    cell_surface.fill((self.color_ship[0], self.color_ship[1], self.color_ship[2], self.OPACITY*2))
                elif self.chess[row][col] == 2:
                    cell_surface.fill((self.red[0], self.red[1], self.red[2], self.OPACITY*3))
                else:
                    cell_surface.fill((self.color[0], self.color[1], self.color[2], self.OPACITY))
                screen.blit(cell_surface, (x, y))
        screen.blit(self.ret, (self.retRect))
        if(self.done):
            screen.blit(self.play, (self.playRect))
        else:
            screen.blit(self.cancel, (self.cancelRect))
        for x in self.list_ship_obj:
            x.draw(screen)        



    def get_name(self):
        return 'CHOOSESHIP'
    
    def update(self, events):
        if self.done:
            for x in self.list_ship_obj:
                tr = x.update(events)
                if tr:
                    self.add_matrices()
    
    def checkShip(self):
        k = 0
        for i in range(self.NUMBER):
            for j in range(self.NUMBER):
                if self.chess[i][j] == 2:
                    return False
                k += self.chess[i][j]
        if k == sum(self.list_ship):
            return True
        else:
            return False
    
    def element(self, events):
        if not self.loose:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.playRect.collidepoint(event.pos):
                        if self.done == True:
                            if self.checkShip():
                                self.done = False
                                return 'DONECHOOSE'
                        else:
                            self.done = True
                            return 'CANCELCHOOSE'
                    if self.retRect.collidepoint(event.pos):
                        self.loose = True
                
    def get_ship(self):
        return self.chess 
    
    def countTime(self,screen):
        if self.stime == 0 and  self.done:
            self.stime = pygame.time.get_ticks()
        if  self.done:
            self.etime = pygame.time.get_ticks()
            current_time =  pygame.time.get_ticks() - self.stime 
        elif not self.done:
            self.timeleft += self.etime -self.stime
            current_time = 0
            self.stime = 0
            self.etime = 0
        
        seconds = (self.timeleft +current_time)// 1000
        font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 30)
        if self.countdown - seconds > 0:
            label_text = font.render(f"{self.countdown - seconds}", True, pygame.Color('white'))
        else:
            label_text = font.render("0", True, pygame.Color('white'))
        textRect = label_text.get_rect()
        textRect.center = (self.WIDTH // 2 ,self.HEIGHT // 9)
        screen.blit(label_text, textRect)  
        if  self.countdown <= seconds:
            return False
        else:
            return True
    def drawpopup(self,screen,events,text):
        self.popup = PopupSend(self.WIDTH,self.HEIGHT,text)
        self.popup.draw(screen)
        return self.popup.update(events)
        

               

class Ship:
    def __init__(self,len,width,height,y_s,cell_size,x,y,number):
        self.WIDTH = width
        self.HEIGHT = height
        self.number = number
        self.start_x = 0
        self.start_y = 0
        self.CELL_SIZE = cell_size
        self.vec = True
        self.len = len
        self.GAP = 1

        self.x_c = x
        self.y_c = y

        self.x_s = x + width // 2
        self.y_s = y_s

        self.x_s_b = self.x_s 
        self.y_s_b = self.y_s

        self.x_b = 0
        self.y_b = 0

        self.pos = 0
        self.choose = False
        self.chess = [[0 for _ in range(number)] for _ in range(number)]
        self.mouse_drag = False
        self.color = pygame.Color(179, 252, 207)

        self.OPACITY = 128
        
    def draw(self, screen):
        for row in range(self.len):
            if(not self.check_is_in()):
                if self.vec:
                    x = row * self.CELL_SIZE + self.x_s_b 
                    cell_surface = pygame.Surface((self.CELL_SIZE - self.GAP, self.CELL_SIZE - self.GAP), pygame.SRCALPHA)
                    cell_surface.fill((self.color[0], self.color[1], self.color[2], self.OPACITY))
                    screen.blit(cell_surface, (x, self.y_s_b))
                else:
                    y = row * self.CELL_SIZE + self.y_s_b 
                    cell_surface = pygame.Surface((self.CELL_SIZE - self.GAP, self.CELL_SIZE - self.GAP), pygame.SRCALPHA)
                    cell_surface.fill((self.color[0], self.color[1], self.color[2], self.OPACITY))
                    screen.blit(cell_surface, (self.x_s_b, y))

    def check_pos(self,x,y):
        if self.vec:
            if self.x_s_b <= x  <= self.x_s_b + self.CELL_SIZE * self.len :
                if self.y_s_b + self.CELL_SIZE  >= y >= self.y_s_b:
                    self.x_b = x - self.x_s_b
                    self.y_b = y - self.y_s_b
                    self.choose = True
                    self.mouse_drag = True
        else: 
            if self.x_s_b <= x  <= self.x_s_b + self.CELL_SIZE :
                if self.y_s_b + self.CELL_SIZE * self.len >= y >= self.y_s_b:
                    self.x_b = x - self.x_s_b
                    self.y_b = y - self.y_s_b
                    self.choose = True
                    self.mouse_drag = True
    
    def get_len(self,x,y):
        if self.vec:
            return (x - self.x_s_b)// self.CELL_SIZE 
        else:
            return (y - self.y_s_b)// self.CELL_SIZE 

    def check_is_in(self):
        if self.vec:
            if self.x_c <= self.x_s_b  and self.y_c <= self.y_s_b:
                if self.x_c+ self.CELL_SIZE * self.number >= self.x_s_b + self.CELL_SIZE * self.len  and self.y_c + self.CELL_SIZE * self.number >= self.y_s_b + self.CELL_SIZE :
                    return True
        else:
            if self.x_c <= self.x_s_b  and self.y_c <= self.y_s_b:
                if self.x_c+ self.CELL_SIZE * self.number >= self.x_s_b + self.CELL_SIZE  and self.y_c + self.CELL_SIZE * self.number >= self.y_s_b + self.CELL_SIZE * self.len:
                    return True
            
        return False
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    self.check_pos(mouse_x,mouse_y)
                    if self.mouse_drag:
                        self.pos = self.get_len(mouse_x,mouse_y)
                    else:
                        self.choose = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if self.mouse_drag:
                        self.mouse_drag = False
                        mouse_x, mouse_y = event.pos
                        if(self.check_is_in()):
                            a = (mouse_x - self.x_c)// self.CELL_SIZE 
                            b = (mouse_y - self.y_c)// self.CELL_SIZE
                            if self.vec:
                                self.x_s_b = self.x_c +   (a-self.pos) *self.CELL_SIZE
                                self.y_s_b = self.y_c +   b*self.CELL_SIZE
                            else:
                                self.x_s_b = self.x_c +   a * self.CELL_SIZE
                                self.y_s_b = self.y_c +   (b-self.pos) * self.CELL_SIZE
                        else:
                            self.vec = True
                            self.x_s_b = self.x_s 
                            self.y_s_b = self.y_s

            elif event.type == pygame.MOUSEMOTION:
                if self.mouse_drag:
                    mouse_x, mouse_y = event.pos
                    if(self.check_is_in()):
                        a = (mouse_x - self.x_c)// self.CELL_SIZE 
                        b = (mouse_y - self.y_c)// self.CELL_SIZE 
                        if self.vec:
                            self.x_s_b = self.x_c +   (a-self.pos) * self.CELL_SIZE
                            self.y_s_b = self.y_c +   b * self.CELL_SIZE
                        else:
                            self.x_s_b = self.x_c +   a * self.CELL_SIZE
                            self.y_s_b = self.y_c +   (b-self.pos) * self.CELL_SIZE
                        self.chess = [[0 for _ in range(self.number)] for _ in range(self.number)]
                        if(self.check_is_in()):
                            for x in range(self.len):
                                if self.vec:
                                    self.chess[b][a+x-self.pos] = 1
                                else:
                                    self.chess[b+x-self.pos][a] = 1
                        return self.chess
                    else:
                        self.x_s_b = mouse_x - self.x_b
                        self.y_s_b = mouse_y - self.y_b

            elif event.type == pygame.KEYDOWN and self.choose:
                if event.key == pygame.K_x:
                    if(self.check_is_in()):
                        if self.vec :
                            self.x_s_b = self.x_s_b + self.CELL_SIZE * (self.len //2)
                            self.y_s_b = self.y_s_b - self.CELL_SIZE * (self.len //2)
                        else:
                            self.x_s_b = self.x_s_b - self.CELL_SIZE * (self.len //2)
                            self.y_s_b = self.y_s_b + self.CELL_SIZE * (self.len //2)
                        self.vec = not self.vec 
                        a = (self.x_s_b  - self.x_c)// self.CELL_SIZE 
                        b = (self.y_s_b - self.y_c)// self.CELL_SIZE 

                        if a < 0:
                            self.x_s_b = self.x_s_b + self.CELL_SIZE * -a
                            a = 0
                        if a +  self.len-1 > self.number-1 and self.vec:
                            self.x_s_b = self.x_s_b + self.CELL_SIZE * (a +  self.len-1 - self.number-1)
                            a = self.number-self.len
                        if b < 0:
                            self.y_s_b = self.y_s_b + self.CELL_SIZE * -b
                            b = 0  
                        if b +  self.len-1 > self.number-1 and not self.vec:
                            self.y_s_b = self.y_s_b + self.CELL_SIZE * (b +  self.len-1 - self.number-1)
                            b = self.number-self.len
                        
                        self.chess = [[0 for _ in range(self.number)] for _ in range(self.number)]

                        for x in range(self.len):
                            if self.vec:
                                self.chess[b][a+x] = 1
                            else:
                                self.chess[b+x][a] = 1
                        return self.chess
    

class LobbySence:
    def __init__(self, width , height ):
        self.check = True
        self.posision = 0
        self.numberPlayer = 12
        self.WIDTH = width
        self.HEIGHT = height
        self.pop = -1
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        bg = pygame.transform.scale(pygame.image.load(path+"/image/bg.png"), (self.WIDTH, self.HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.color = pygame.Color('lightskyblue3')
        self.boxObject = []
        self.us = 0
        self.popp = False
        self.click = False
        self.popup  = None
        self.ret = pygame.transform.scale(pygame.image.load(path+"/image/return.png"), (
            pygame.image.load(path+"/image/return.png").get_width() // 6,
            pygame.image.load(path+"/image/return.png").get_height() // 6))
        self.menu = pygame.transform.scale(pygame.image.load(path+"/image/menu.png"), (
            pygame.image.load(path+"/image/menu.png").get_width() // 6,
            pygame.image.load(path+"/image/menu.png").get_height() // 6))
        self.retRect = self.ret.get_rect()
        self.retRect.center = (self.WIDTH  // 2, self.HEIGHT  // 3)
        
        self.menuRect = self.menu.get_rect()
        self.menuRect.center = (self.WIDTH  // 2, self.HEIGHT  // 1.5)
        for i in range(self.numberPlayer):
            self.boxObject.append(TextboxLobby(self.WIDTH //3*2, self.HEIGHT //13 * (i+1),width,height,i))

        
    def draw(self, screen, text):
        screen.blit(self.background, (0, 0))
        font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 7)
        text_battle = font.render("Battle", True, pygame.Color(198, 216, 207))
        text_ship = font.render("Ship", True, pygame.Color(198, 216, 207))
        textRect = text_battle.get_rect()
        textRect.center = (self.WIDTH // 4 ,self.HEIGHT // 2-self.HEIGHT //7)
        screen.blit(text_battle, textRect)
        textRect = text_ship.get_rect()
        textRect.center = (self.WIDTH // 4, self.HEIGHT // 2+self.HEIGHT //7)
        screen.blit(text_ship, textRect)

        elements = text.split()
        self.ids = elements[::2]
        usernames = elements[1::2] 
        self.us = len(usernames)
        screen.blit(self.ret, (self.retRect))
        screen.blit(self.menu, (self.menuRect))
        
        for index,x in enumerate(self.boxObject):
            if(index == 0  and self.posision > 0 and self.us>10):
                x.draw(screen,"/\\")  
                continue
            if(index == 0):
                continue
            if(index == self.numberPlayer-1 and self.us>10 and self.posision+self.numberPlayer-1<self.us):
                x.draw(screen,"\\/")  
                continue
            if(index == self.numberPlayer-1):
                continue
            if(index-1 >= self.us):
                continue
            else:
                x.draw(screen,usernames[index-1+self.posision])   
            
        
    def get_name(self):
        return 'LOBBY'
    def update(self, events):
        if self.popp:
            pass
        else:
            for index,x in enumerate(self.boxObject):  
                if(index == 0  and self.posision == 0 and self.us>10):
                    continue
                if(index == self.numberPlayer-1 and self.us>10 and self.posision+self.numberPlayer-1 == self.us):
                    continue
                t = x.update(events)
                if t==0 and index == 0:
                    self.posision += -1
                    continue
                if t and index == self.numberPlayer -1:
                    self.posision += 1
                    continue
                if t and t <= self.us:
                    self.pop = t
                    self.click = True

    def element(self, events):
        if self.pop >= 1 and self.click:
            self.click=False
            return self.ids[self.posision+self.pop-1]
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menuRect.collidepoint(pygame.mouse.get_pos()):
                    self.check = not self.check
                    if not self.check:
                        return 'GETMATCH'
                if self.retRect.collidepoint(pygame.mouse.get_pos()):
                    return 'LOGOUT'
        
    def checkPop(self,check):
        self.popp = check

    def drawpopup(self,events,isSend,text,screen):
        if isSend:
            self.popup = PopupSend(self.WIDTH,self.HEIGHT,"")
        else:
            self.popup = PopupRecive(self.WIDTH,self.HEIGHT,text)
        self.popup.draw(screen)

        return self.popup.update(events)
        

class TextboxLobby:
    def __init__(self, x, y, width,height,i):
        self.rect = pygame.Rect(x , y, width // 4, height//15)
        self.color = pygame.Color('lightskyblue3')
        self.position = i
        self.hover = False
        self.width = width
        self.height = height
        self.is_active = False

    def draw(self, screen,text):
        font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.width // 30)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.color, self.rect, 2)
        
        
        text_surface = font.render(text , True, pygame.Color('white'))
        width = max(self.width // 4, text_surface.get_width() + 10)
        self.rect.width = width
        screen.blit(text_surface, (self.rect.x + self.width // 8 - text_surface.get_width()//2, self.rect.y + 5))


    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_active = self.rect.collidepoint(event.pos)
            if self.is_active:
                self.is_active = False
                return self.position
    
class PlayShip:
    def __init__(self, width , height, number ):
        self.WIDTH = width
        self.HEIGHT = height
        self.NUMBER = number
        self.GAP = 1
        self.turn = False
        self.stime = 0
        self.checkwin = 0
        self.done = True
        self.etime = 0
        self.stime1 = 0
        self.etime1 = 0
        self.timeleft = 0
        self.loose = False
        self.countdown = 20
        self.pauseTime = 120
        self.CELL_SIZE = height // (number + 2)
        self.OPACITY =  75
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.x = (self.WIDTH //2 - self.CELL_SIZE  * self.NUMBER ) //2
        self.y = (self.HEIGHT - self.CELL_SIZE * self.NUMBER) //2
        bg = pygame.transform.scale(pygame.image.load(path+"/image/bg.png"), (self.WIDTH, self.HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.color = pygame.Color('white')
        self.color_ship = pygame.Color(179, 252, 207)
        self.red = pygame.Color(216, 29, 29)
        self.blue = pygame.Color(36, 0, 215)
        self.chess = [[0 for _ in range(number)] for _ in range(number)]
        self.chess_op = [[0 for _ in range(number)] for _ in range(number)]
        self.rect = []
        self.wait = False
        self.row = -1
        self.column = -1
        self.w = False
        for row in range(self.NUMBER):
            for col in range(self.NUMBER ):
                x = col * self.CELL_SIZE + self.x + self.WIDTH//2
                y = row * self.CELL_SIZE + self.y 
                cell_rect = pygame.Rect(x, y, self.CELL_SIZE - self.GAP, self.CELL_SIZE - self.GAP)
                self.rect.append(cell_rect)
        self.play = pygame.transform.scale(pygame.image.load(path+"/image/play.png"), (
            pygame.image.load(path+"/image/play.png").get_width() // 6,
            pygame.image.load(path+"/image/play.png").get_height() // 6))
        self.cancel = pygame.transform.scale(pygame.image.load(path+"/image/return.png"), (
            pygame.image.load(path+"/image/return.png").get_width() // 6,
            pygame.image.load(path+"/image/return.png").get_height() // 6))
        self.playRect = self.play.get_rect()
        self.playRect.center = (self.WIDTH  // 2, self.HEIGHT  // 1.1)
        
        self.cancelRect = self.cancel.get_rect()
        self.cancelRect.center = (self.WIDTH  // 2, self.HEIGHT  // 4)
        self.popup  = None

    def draw(self, screen,text):
        screen.blit(self.background, (0, 0))
        for row in range(self.NUMBER):
            for col in range(self.NUMBER ):
                x = col * self.CELL_SIZE + self.x
                y = row * self.CELL_SIZE + self.y
                cell_surface = pygame.Surface((self.CELL_SIZE - self.GAP, self.CELL_SIZE - self.GAP), pygame.SRCALPHA)
                if self.chess[row][col] == 1:
                    cell_surface.fill((self.color_ship[0], self.color_ship[1], self.color_ship[2], self.OPACITY*2))
                elif self.chess[row][col] == 2:
                    cell_surface.fill((self.red[0], self.red[1], self.red[2], self.OPACITY*3))
                elif self.chess[row][col] == 3:
                    cell_surface.fill((self.blue[0], self.blue[1], self.blue[2], self.OPACITY*3))
                else:
                    cell_surface.fill((self.color[0], self.color[1], self.color[2], self.OPACITY))
                screen.blit(cell_surface, (x, y))  
        screen.blit(self.play, self.playRect) 
        screen.blit(self.cancel, self.cancelRect)        
        
        for i,cell_rect in enumerate(self.rect):
            r = i // self.NUMBER 
            c = i % self.NUMBER
            x = c * self.CELL_SIZE + self.x + self.WIDTH//2
            y = r * self.CELL_SIZE + self.y 
            if cell_rect.collidepoint(pygame.mouse.get_pos()) and self.chess_op[r][c] == 0:
                cell_surface.fill((self.blue[0], self.blue[1], self.blue[2], self.OPACITY*3))
            elif self.chess_op[r][c] == 1:
                cell_surface.fill((self.color_ship[0], self.color_ship[1], self.color_ship[2], self.OPACITY*2))
            elif self.chess_op[r][c] == 2:
                cell_surface.fill((self.red[0], self.red[1], self.red[2], self.OPACITY))
            else:
                cell_surface.fill((self.color[0], self.color[1], self.color[2], self.OPACITY))
            screen.blit(cell_surface, (x, y))       

    def get_name(self):
        return 'PLAYSHIP'
    def setShip(self,ship):
        self.chess = ship
    
    def update(self, events):
        pass
    def check(self,row,column):
        if(self.chess_op[row][column] != 0):
            return False
        else: 
            return True
    def setChess(self,true):
        if true:
            self.chess_op[self.row][self.column] = 2
        else:
            self.chess_op[self.row][self.column] = 1

    def element(self, events):    
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  not self.loose and not self.wait and not self.w:
                    if self.turn:
                        for i,cell_rect in enumerate(self.rect):
                            if cell_rect.collidepoint(event.pos):
                                self.row = i // self.NUMBER 
                                self.column = i % self.NUMBER 
                                if self.check(self.row ,self.column):
                                    return str(self.row) + ' ' + str(self.column)
                    if self.playRect.collidepoint(event.pos):
                        self.done = False
                        self.stime1 = pygame.time.get_ticks()
                        self.wait = True
                        return 'WAITING'
                    if self.cancelRect.collidepoint(event.pos):
                        self.loose = True

    def countTime(self,screen):
        if self.turn:
            if self.stime == 0 and self.done:
                self.stime = pygame.time.get_ticks()
            if  self.done:
                self.etime = pygame.time.get_ticks()
                current_time =  pygame.time.get_ticks() - self.stime 
            elif not self.done:
                self.timeleft += self.etime -self.stime
                current_time = 0
                self.stime = 0
                self.etime = 0
            
            seconds = (self.timeleft +current_time)// 1000
            font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 30)
            if self.countdown - seconds > 0:
                label_text = font.render(f"Your turn: {self.countdown - seconds}", True, pygame.Color('white'))
            else:
                label_text = font.render("Your turn: 0", True, pygame.Color('white'))
            textRect = label_text.get_rect()
            textRect.center = (self.WIDTH // 2 ,self.HEIGHT // 20)
            screen.blit(label_text, textRect)  
            if self.countdown <= seconds:
                return True
            else:
                return False
        else:
            self.stime = 0
            self.etime = 0
            self.timeleft = 0

    def getmove(self,move):
        string_list = move.split() 
        if (self.chess[int(string_list[0])][int(string_list[1])] == 1):
            self.chess[int(string_list[0])][int(string_list[1])] = 2
        else:
            self.chess[int(string_list[0])][int(string_list[1])] = 3

    def checkLoose(self):
        l = 0
        for row in range(self.NUMBER):
            for col in range(self.NUMBER):
                if self.chess[row][col] == 2:
                    l += 1
        if l == self.checkwin:
            return True
        
    def drawpopup(self,screen,events,text):
        self.popup = PopupSend(self.WIDTH,self.HEIGHT,text)
        self.popup.draw(screen)
        return self.popup.update(events)
    
    def drawpopupnone(self,screen):
        self.popup = PopupNone(self.WIDTH,self.HEIGHT)
        self.popup.draw(screen)

        

class PopupSend:
    def __init__(self, width, height,message):
        self.OPACITY = 100
        self.width = width
        self.height = height
        self.message = message
        self.color = pygame.Color(pygame.Color(100,200,123) [0], pygame.Color(100,200,123) [1], pygame.Color(100,200,123) [2], self.OPACITY)
        self.rect = pygame.Rect((width - width//3) // 2, (height - height//3) // 2, width//3, height//3)

        button_width, button_height = width//15, height//15
        self.cancel_button_rect = pygame.Rect(self.rect.centerx -button_width//2, self.rect.bottom - button_height - 20, button_width, button_height)

    def draw(self,screen):
        font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.width // 30)
        pygame.draw.rect(screen, (self.color[0], self.color[1], self.color[2], self.OPACITY), self.rect)

        text = font.render(self.message, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
   
        pygame.draw.rect(screen, (255, 0, 0), self.cancel_button_rect)
        cancel_text = font.render("Cancel", True, (0, 0, 0))
        cancel_text_rect = cancel_text.get_rect(center=self.cancel_button_rect.center)
        screen.blit(cancel_text, cancel_text_rect)


    def update(self,events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if self.cancel_button_rect.collidepoint(event.pos):
                        return 'CANCELBATTLE'               
class ViewShip:
    def __init__(self, width , height, number ):
        self.WIDTH = width
        self.HEIGHT = height
        self.NUMBER = number
        self.GAP = 1  
        self.stime = 0
        self.etime = 0
        self.done = False
        self.count = 1
        self.first = -1
        self.u1 = ""
        self.u2 = ""
        self.CELL_SIZE = height // (number + 2)
        self.OPACITY =  75
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.x = (self.WIDTH //2 - self.CELL_SIZE  * self.NUMBER ) //2
        self.y = (self.HEIGHT - self.CELL_SIZE * self.NUMBER) //2
        bg = pygame.transform.scale(pygame.image.load(path+"/image/bg.png"), (self.WIDTH, self.HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.color = pygame.Color('white')
        self.color_ship = pygame.Color(179, 252, 207)
        self.red = pygame.Color(216, 29, 29)
        self.blue = pygame.Color(36, 0, 215)
        self.chess = [[0 for _ in range(number)] for _ in range(number)]
        self.chess_op = [[0 for _ in range(number)] for _ in range(number)]

        self.cancel = pygame.transform.scale(pygame.image.load(path+"/image/return.png"), (
            pygame.image.load(path+"/image/return.png").get_width() // 6,
            pygame.image.load(path+"/image/return.png").get_height() // 6))

        self.cancelRect = self.cancel.get_rect()
        self.cancelRect.center = (self.WIDTH  // 2, self.HEIGHT  // 4)

    def draw(self, screen,text):
        screen.blit(self.background, (0, 0))
        for row in range(self.NUMBER):
            for col in range(self.NUMBER ):
                x = col * self.CELL_SIZE + self.x + + self.WIDTH//2
                y = row * self.CELL_SIZE + self.y 
                cell_surface = pygame.Surface((self.CELL_SIZE - self.GAP, self.CELL_SIZE - self.GAP), pygame.SRCALPHA)
                if self.chess_op[row][col] == 1:
                    cell_surface.fill((self.color_ship[0], self.color_ship[1], self.color_ship[2], self.OPACITY*2))
                elif self.chess_op[row][col] == 2:
                    cell_surface.fill((self.red[0], self.red[1], self.red[2], self.OPACITY*3))
                elif self.chess_op[row][col] == 3:
                    cell_surface.fill((self.blue[0], self.blue[1], self.blue[2], self.OPACITY*3))
                else:
                    cell_surface.fill((self.color[0], self.color[1], self.color[2], self.OPACITY))
                screen.blit(cell_surface, (x, y))  
        screen.blit(self.cancel, self.cancelRect)      

        for row in range(self.NUMBER):
            for col in range(self.NUMBER ):
                x = col * self.CELL_SIZE + self.x
                y = row * self.CELL_SIZE + self.y 
                cell_surface = pygame.Surface((self.CELL_SIZE - self.GAP, self.CELL_SIZE - self.GAP), pygame.SRCALPHA)
                if self.chess[row][col] == 1:
                    cell_surface.fill((self.color_ship[0], self.color_ship[1], self.color_ship[2], self.OPACITY*2))
                elif self.chess[row][col] == 2:
                    cell_surface.fill((self.red[0], self.red[1], self.red[2], self.OPACITY*3))
                elif self.chess[row][col] == 3:
                    cell_surface.fill((self.blue[0], self.blue[1], self.blue[2], self.OPACITY*3))
                else:
                    cell_surface.fill((self.color[0], self.color[1], self.color[2], self.OPACITY))
                screen.blit(cell_surface, (x, y))  
        screen.blit(self.cancel, self.cancelRect)   
             
        font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 30)
        label_text = font.render(self.u1, True, pygame.Color('white'))
        textRect = label_text.get_rect()
        textRect.center = (self.WIDTH // 4 ,self.HEIGHT // 20)
        screen.blit(label_text, textRect)  

        label_text_1 = font.render(self.u2, True, pygame.Color('white'))
        textRect_1 = label_text_1.get_rect()
        textRect_1.center = (self.WIDTH // 4 *3,self.HEIGHT // 20)
        screen.blit(label_text_1, textRect_1)  

    def get_name(self):
        return 'VIEWSHIP'
    
    def update(self, events):
        pass

    def check(self,mlm):
        elements = mlm.split()
        if mlm == 'DONE':
            self.done = True      
        elif self.count == 1 or self.count == 2:
            
            numbers = [int(element) for element in elements[1:] if element.isdigit()]
            if self.first == -1:
                self.u1 = elements[0]
                self.first = numbers[0]
                for i in range((len(numbers)-1)//2):
                    self.chess[numbers[i*2+1]][numbers[i*2+2]]= 1
                    
            else:
                self.u2 = elements[0]
                for i in range((len(numbers)-1)//2):
                    self.chess_op[numbers[i*2+1]][numbers[i*2+2]] = 1
                   
        else:
            numbers = [int(element) for element in elements[0:] if element.isdigit()]
            if not self.first == numbers[0]:
                if (self.chess[numbers[1]][numbers[2]] == 1):
                    self.chess[numbers[1]][numbers[2]] = 2
                else:
                    self.chess[numbers[1]][numbers[2]] = 3   
            else:
                if (self.chess_op[numbers[1]][numbers[2]] == 1):
                    self.chess_op[numbers[1]][numbers[2]] = 2
                else:
                    self.chess_op[numbers[1]][numbers[2]] = 3  
        self.count +=1


    def element(self, events):    
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.cancelRect.collidepoint(event.pos):
                    return 'ABC'
    
   
  
class PopupRecive:
    def __init__(self, width, height,message):
        self.OPACITY = 100
        self.width = width
        self.height = height
        self.message = message
        self.color = pygame.Color(pygame.Color(100,200,123) [0], pygame.Color(100,200,123) [1], pygame.Color(100,200,123) [2], self.OPACITY)
        self.rect = pygame.Rect((width - width//3) // 2, (height - height//3) // 2, width//3, height//3)

        button_width, button_height = width//15, height//15
        self.play_button_rect = pygame.Rect(self.rect.centerx - button_width - 10, self.rect.bottom - button_height - 20, button_width, button_height)
        self.cancel_button_rect = pygame.Rect(self.rect.centerx + 10, self.rect.bottom - button_height - 20, button_width, button_height)

    def draw(self,screen):
        font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.width // 30)
        pygame.draw.rect(screen, (self.color[0], self.color[1], self.color[2], self.OPACITY), self.rect)


        text = font.render(self.message, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

        pygame.draw.rect(screen, (0, 255, 0), self.play_button_rect)
        play_text = font.render("Play", True, (0, 0, 0))
        play_text_rect = play_text.get_rect(center=self.play_button_rect.center)
        screen.blit(play_text, play_text_rect)

   
        pygame.draw.rect(screen, (255, 0, 0), self.cancel_button_rect)
        cancel_text = font.render("Cancel", True, (0, 0, 0))
        cancel_text_rect = cancel_text.get_rect(center=self.cancel_button_rect.center)
        screen.blit(cancel_text, cancel_text_rect)


    def update(self,events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if self.play_button_rect.collidepoint(event.pos):
                        return 'ACCEPTBATTLE'
                    elif self.cancel_button_rect.collidepoint(event.pos):
                        return 'CANCELBATTLE'
                    
class PopupNone:
    def __init__(self, width, height):
        self.OPACITY = 100
        self.width = width
        self.height = height
        self.message = "Waiting"
        self.color = pygame.Color(pygame.Color(100,200,123) [0], pygame.Color(100,200,123) [1], pygame.Color(100,200,123) [2], self.OPACITY)
        self.rect = pygame.Rect((width - width//3) // 2, (height - height//3) // 2, width//3, height//3)

    def draw(self,screen):
        font = pygame.font.Font(path+'/font/iCielBCDDCHardwareRough-Compressed.ttf', self.width // 30)
        pygame.draw.rect(screen, (self.color[0], self.color[1], self.color[2], self.OPACITY), self.rect)
        text = font.render(self.message, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def update(self,events):
        pass