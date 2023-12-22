import pygame
import os

path = os.path.dirname(os.path.realpath(__file__))

class SignInScene:
    def __init__(self, width , height ):
        self.WIDTH = width
        self.HEIGHT = height
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        bg = pygame.transform.scale(pygame.image.load(path+"/image/bg.png"), (self.WIDTH, self.HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.username_textbox = Textbox(self.WIDTH //3*2, self.HEIGHT // 2 - self.HEIGHT //12, "Username:",width,height)
        self.password_textbox = Textbox(self.WIDTH  //3*2, self.HEIGHT // 2 + self.HEIGHT //12, "Password:", width,height,is_password=True)
        self.repassword_textbox = Textbox(self.WIDTH  //3*2, self.HEIGHT // 2 + self.HEIGHT //12, "Rewrite Password:", width,height,is_password=True)
        self.color = pygame.Color('lightskyblue3')
        
    def draw(self, screen,text):
        screen.blit(self.background, (0, 0))
        font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 7)
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
        self.repassword_textbox.draw(screen)
        play = pygame.transform.scale(pygame.image.load("UI/image/start.png"), (
            pygame.image.load("UI/image/start.png").get_width() // 6,
            pygame.image.load("UI/image/start.png").get_height() // 6))
        self.playRect = play.get_rect()
        self.playRect.center = (self.WIDTH  // 2, self.HEIGHT  // 1.2)
        screen.blit(play, self.playRect)
    def get_name():
        return 'LOGIN'
    def update(self, events):
        self.username_textbox.update(events)
        self.password_textbox.update(events)
        self.repassword_textbox.draw(events)

    def element(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playRect.collidepoint(event.pos):
                    return 'Username:' + self.username_textbox.text + 'Password:' + self.password_textbox.text

class LoginScene:
    def __init__(self, width , height ):
        self.WIDTH = width
        self.HEIGHT = height
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        bg = pygame.transform.scale(pygame.image.load(path+"/image/bg.png"), (self.WIDTH, self.HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.username_textbox = Textbox(self.WIDTH //3*2, self.HEIGHT // 2 - self.HEIGHT //12, "Username:",width,height)
        self.password_textbox = Textbox(self.WIDTH  //3*2, self.HEIGHT // 2 + self.HEIGHT //12, "Password:", width,height,is_password=True)
        self.color = pygame.Color('lightskyblue3')
        
    def draw(self, screen,text):
    
        screen.blit(self.background, (0, 0))
        
        font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 7)
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
        play = pygame.transform.scale(pygame.image.load("UI/image/start.png"), (
            pygame.image.load("UI/image/start.png").get_width() // 6,
            pygame.image.load("UI/image/start.png").get_height() // 6))
        self.playRect = play.get_rect()
        self.playRect.center = (self.WIDTH  // 2, self.HEIGHT  // 1.2)
        screen.blit(play, self.playRect)

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
        font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', self.width // 30)
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
                if event.key == pygame.K_RETURN:
                    print(f"{self.label.strip()}: {self.text}")
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode


class ChooseShipScene:
    def __init__(self, width , height, number ):
        self.WIDTH = width
        self.HEIGHT = height
        self.NUMBER = number
        self.GAP = 1
        self.CELL_SIZE = height // (number + 2)
        self.OPACITY =  75
        self.list_ship = [2,3,3,4,5]
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
        for x in self.list_ship_obj:
            x.draw(screen)        



    def get_name(self):
        return 'CHOOSESHIP'
    
    def update(self, events):
        for x in self.list_ship_obj:
            tr = x.update(events)
            if tr:
                self.add_matrices()
        
    def element(self, events):
        pass

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
        self.posision = 0
        self.numberPlayer = 10
        self.WIDTH = width
        self.HEIGHT = height
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        bg = pygame.transform.scale(pygame.image.load(path+"/image/bg.png"), (self.WIDTH, self.HEIGHT))
        self.background.blit(bg, (-1, 0))
        self.color = pygame.Color('lightskyblue3')
        self.boxObject = []
        for i in range(self.numberPlayer):
            self.boxObject.append(TextboxLobby(self.WIDTH //3*2, self.HEIGHT //12 * (i+1),width,height,i))

        
    def draw(self, screen, text):
        screen.blit(self.background, (0, 0))
        font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', self.WIDTH // 7)
        text_battle = font.render("Battle", True, pygame.Color(198, 216, 207))
        text_ship = font.render("Ship", True, pygame.Color(198, 216, 207))
        textRect = text_battle.get_rect()
        textRect.center = (self.WIDTH // 4 ,self.HEIGHT // 2-self.HEIGHT //7)
        screen.blit(text_battle, textRect)
        textRect = text_ship.get_rect()
        textRect.center = (self.WIDTH // 4, self.HEIGHT // 2+self.HEIGHT //7)
        screen.blit(text_ship, textRect)
        elements = text.split()
        ids = elements[::2]
        usernames = elements[1::2] 
        for index,x in enumerate(self.boxObject):
            if(index >= len(usernames)):
                break
            x.draw(screen,usernames[index+self.posision])   
        
    def get_name(self):
        return 'LOBBY'
    def update(self, events):
        pass

    def element(self, events):
        pass

class TextboxLobby:
    def __init__(self, x, y, width,height,i):
        self.rect = pygame.Rect(x , y, width // 4, height//15)
        self.color = pygame.Color('lightskyblue3')
        self.position = i
        self.hover = False
        self.width = width
        self.height = height

    def draw(self, screen,text):
        font = pygame.font.Font('UI/font/iCielBCDDCHardwareRough-Compressed.ttf', self.width // 30)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.color, self.rect, 2)
        
        
        text_surface = font.render(text , True, pygame.Color('white'))
        width = max(self.width // 4, text_surface.get_width() + 10)
        self.rect.width = width
        screen.blit(text_surface, (self.rect.x + self.width // 8 - text_surface.get_width()//2, self.rect.y + 5))


    def update(self, events):
        pass
        # for event in events:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         self.is_active = self.rect.collidepoint(event.pos)
        #     if event.type == pygame.KEYDOWN and self.is_active:
        #         if event.key == pygame.K_RETURN:
        #             print(f"{self.label.strip()}: {self.text}")
        #             self.text = ""
        #         elif event.key == pygame.K_BACKSPACE:
        #             self.text = self.text[:-1]
        #         else:
        #             self.text += event.unicode