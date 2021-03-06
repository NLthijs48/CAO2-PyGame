import time

import pygame

from game.classes.ball import Ball
from game.classes.finish import Finish
from game.classes.hole import Hole
from game.classes.wall import Wall
import game.constants as c


class Game(object):
    
    # Maps
    map2 = [     
    "WWWWWWWw",
    "WS      ",
    "W       ",
    "WWWWWWWw"
    ]
    
    map = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WS       HWH       W        WH                   W",
    "W         W        W   H    W                E   W",
    "WWWWWWWW  W    W   W   H    W   WWWWWWWWWWWWWWWWWW",
    "W         W    W            W                    W",
    "W H       WH   W      WW    WWWWWWWWWWWWWWWWWWW  W",
    "W         W    WH    WW     WH      W     W     WW",
    "W         W   WWWW HWW  H  WW    W     W     W  HW",
    "W         W        WW     WW     WWWWWWWWWWWWWWWWW",
    "W    H    W H     WW     WW      W              HW",
    "W         WWWW   WW  H  WW  H    W               W",
    "W         W      W     WW        W  WWWWWWWWWWW  W",
    "W         W      W    WWWWWWWWW  W  W H W     W  W",
    "W  WWWWWWWW  WWWWW            W  W  W   W     W  W",
    "W        W      HWH           W  W  W   W  W  W  W",
    "W        W       WWWWWWWWWWW  W  W  W W W  W  W  W",
    "WWWWWWW  W  H        W        W  W  W W W  W  W  W",
    "W        W           W        WH W  W W W  W  W  W",
    "W        WWWWWWWW    W    HHHHW  W  W W W  W  W  W",
    "W  WWWW  W      WWW  W        W  W  W W W  W  W  W",
    "W  W     W      W    W        W  W  W W    W  W  W",
    "W  W     W  W   W    WHHHH    W  W    W    W  W  W",
    "W  W   WWW  W   W  WWW        W  W    W H  W  W  W",
    "W  W    H   W   W    W        W  WWWWWWWWWWW  W  W",
    "W  W        W   W    W    HHHHW               W  W",
    "W  WWWWWWWWWW   WWW  W        W         H     W  W",
    "W          H         W    W   WWWWWWWWWWWWWWWWW  W",
    "WH                   WH              W           W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW     WWW WWWWWWWWW",
    "WH                 HWWW              WH          W",
    "W                   WW             HHWWWWWWWWW WWW",
    "W   W WWWWWWWWWWW   W   WWH  HWWWWWWWW          HW",
    "W  HW          HW   W  HW            W  WWWWWWWWWW",
    "W   WWWWWW   WWWW   W   W    WWWWW   W   H      HW",
    "W   W        WH     W   W   WWH     WW           W",
    "WH  W WWWWWWWW     HW  W   WW      WW        H   W",
    "W   W        W   WWWW     WW      WW      H     HW",
    "W   WWWWWWWW W     HW    WW  H   WWH             W",
    "W  HW        WH     WWWWWW      WWWWWWWWW        W",
    "W   W WWWWWWWWWWW    HHWW      WW       WH       W",
    "W   W          HW    HWW  H   WW        WWWWW    W",
    "WH  W           W    WW      WW    WW   W        W",
    "W   WWWWWWWWW  WW   WWH     WW    WW    W   W    W",
    "W   W      HW   W          WW    WW    WW   W    W",
    "W  HW  W    WW  W        HWW    WW    WW    WWW  W",
    "W   W  WW       WWWWWWWWWWW    WW           W    W",
    "W   W   WWWWWWWWW             WW            W    W",
    "W          W       W  WWWWWWWWWWWWWWWWWWWWWWW  WWW",
    "WH     W       W   W                            HW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
    
    #main objects
    screen = ''
    start_screen = True

    #Game objects
    walls = []
    finishes = []
    holes = []
    ball = ''
    sprites = []
    clock = ''
    clicked_pos = (0,0)
    clicked = False
    start_time = 0
    end_time = 0
    win = False
    end_lives = 0
    end_win = False
    next_live_time = 0
    
    #Sprites
    sprites = {}

    # Current map
    current_map = 0

    def __init__(self, file_path, set_map, screen):
        
        self.sprites["wall"] = pygame.image.load(file_path + 'images/wall2.png')
        self.sprites["ball"] = pygame.image.load(file_path + 'images/Ball_green.png') 
        self.sprites["hole"] = pygame.image.load(file_path + 'images/hole.png')
        self.sprites["finish"] = pygame.image.load(file_path + 'images/finish.png')
        self.sprites["background"] = pygame.image.load(file_path + 'images/background2.png')

        #set screen
        self.screen = screen
        
        # Set map
        self.current_map = set_map
        
        # Set clock   
        self.clock = pygame.time.Clock()
   
   
    def play(self):
        
        running = True
                
        while(running):
            
            # Stop running
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    return False
                if e.type == pygame.KEYDOWN:
                    if self.start_screen :
                        self.start_time = time.time()
                        self.nextLive()
                        self.start_screen = False
                                 
            #check  over
            if self.ball.get_lives() <= 0 or self.win:
                
                self.end_time = int(time.time() - self.start_time)
                self.end_lives = self.ball.get_lives()
                self.end_win = self.win
                return True               
            
            else :   
                # Game do step
                if not self.start_screen and not self.next_live_time > 0:
                    self.game_move()
                
                # Times for next level
                if self.next_live_time > 0:
                    if int(time.time() - self.next_live_time) > c.WAIT_TIME_BETWEEN_LIVES :
                        self.next_live_time = 0
                        self.start_time+= time.time() - self.temp_time
                
                # Draw new  field
                self.draw_play_screen()
                
                # Wait a clock tick
                self.clock.tick(c.FPS)
                
                
    def getHoles(self):
        return self.holes

    def getWalls(self):
        return self.walls
    
    def getFinishes(self):
        return self.finishes
    
    def setWin(self):
        self.win = True
        
    def nextLive(self):
        self.next_live_time = time.time()
        self.temp_time = time.time()
   
    def create_map(self):
        self.walls = []
        self.finishes = []
        self.holes = []
        self.start_screen = True
        self.win = False
        x = y = 0
        for row in self.map:
            for coll in row:
                if coll == "W" :
                    self.walls.append(Wall((x,y)))
                if coll == "E" :
                    self.finishes.append(Finish((x,y)))
                if coll == "S" :
                    self.ball = Ball((x,y), c.HOLE_OVERLAP, self)
                if coll == "H":
                    self.holes.append(Hole((x,y)))
                x+= c.OBJECT_SIZE
            y+= c.OBJECT_SIZE
            x=0
            
    def game_move(self):
        
        speed_x = self.ball.get_speed()[0]
        speed_y = self.ball.get_speed()[1]
            
        if pygame.mouse.get_pressed()[0]:
            if not self.clicked:
                self.clicked = True
                self.clicked_pos = pygame.mouse.get_pos()
            else:
                xdif = (pygame.mouse.get_pos()[0] - self.clicked_pos[0])
                if (xdif > 0 and xdif > c.DEAD_ZONE) or  (xdif < 0 and xdif < c.DEAD_ZONE):
                    if xdif < 0:
                        xdif = xdif + c.DEAD_ZONE
                    if xdif > 0:
                        xdif = xdif - c.DEAD_ZONE
                    speed_x = speed_x + ((xdif) * c.PIXEL_SPEED_INC)
                    if speed_x > c.MAX_SPEED:
                        speed_x = c.MAX_SPEED
                    if speed_x < -c.MAX_SPEED:
                        speed_x = -c.MAX_SPEED
                ydif = (pygame.mouse.get_pos()[1] - self.clicked_pos[1])
                if (ydif > 0 and ydif > c.DEAD_ZONE) or  (ydif < 0 and ydif < c.DEAD_ZONE):
                    if ydif < 0:
                        ydif = ydif + c.DEAD_ZONE
                    if ydif > 0:
                        ydif = ydif - c.DEAD_ZONE
                    speed_y = speed_y + ((ydif) * c.PIXEL_SPEED_INC)
                    if speed_y > c.MAX_SPEED:
                        speed_y = c.MAX_SPEED
                    if speed_y < -c.MAX_SPEED:
                        speed_y = -c.MAX_SPEED
        else:
            self.clicked = False
        
        # Get the movement of the ball
        dx = speed_x * 1.6 * (c.FPS / 120);
        dy = speed_y * (c.FPS / 120);
        # Add drag
        if speed_x > 0 and speed_x > c.PIXEL_DRAG:
            speed_x -= c.PIXEL_DRAG
        elif speed_x < 0 and speed_x < -c.PIXEL_DRAG:
            speed_x += c.PIXEL_DRAG
        else:
            speed_x = 0 
        if speed_y > 0 and speed_y > c.PIXEL_DRAG:
            speed_y -= c.PIXEL_DRAG
        elif speed_y < 0 and speed_y < -c.PIXEL_DRAG:
            speed_y += c.PIXEL_DRAG
        else:
            speed_y = 0 
        # Move and update speed
        self.ball.set_speed((speed_x, speed_y))
        self.ball.move(dx, dy)
    
    def draw_play_screen(self):
        
        self.screen.fill((0,0,0))
        background_image = self.sprites["background"].get_rect()
        self.screen.blit(self.sprites["background"], background_image)
        
        if self.start_screen :
            font_startscreen = pygame.font.Font(None, 80)
            text = font_startscreen.render("Press a key to start!", 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.centery = 400
            textpos.centerx = 500
            self.screen.blit(text, textpos)
            
            if not self.end_time == 0 :
                font_startscreen = pygame.font.Font(None, 60)
                if self.end_win :
                    text = font_startscreen.render("You won!", 1, (0, 255, 0))
                else:
                    text = font_startscreen.render("You failed!", 1, (255, 0, 0))
                textpos = text.get_rect()
                textpos.centery = 200
                textpos.centerx = 500
                self.screen.blit(text, textpos)
                font_startscreen = pygame.font.Font(None, 40)
                text = font_startscreen.render("Time: " + str(self.end_time) + " seconds", 1, (0, 0, 0))
                textpos = text.get_rect()
                textpos.centery = 250
                textpos.centerx = 500
                self.screen.blit(text, textpos)
                text = font_startscreen.render(" Lives left: " + str(self.end_lives) , 1, (0, 0, 0))
                textpos = text.get_rect()
                textpos.centery = 290
                textpos.centerx = 500
                self.screen.blit(text, textpos)
                
        else :
            for wall in self.walls:
                self.screen.blit(self.sprites["wall"], wall.rect)  
            for hole in self.holes:
                self.screen.blit(self.sprites["hole"], hole.rect) 
            self.screen.blit(self.sprites["ball"], self.ball.rect) 
          
            font = pygame.font.Font(None, 45)
            text = font.render("Lives: " + str(self.ball.get_lives()), 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.left = 820
            textpos.top = 20
            self.screen.blit(text, textpos)
            if self.next_live_time > 0:
                play_time = int(self.temp_time - self.start_time)
            else: 
                play_time = int(time.time() - self.start_time)
            text = font.render("Time: " + str(play_time), 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.left = 820
            textpos.top = 60
            self.screen.blit(text, textpos)
            
            # DEBUG
            font = pygame.font.Font(None, 20)
            text = font.render("xspeed=" + str(self.ball.get_speed()[0]), 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.left = 820
            textpos.centery = 600
            self.screen.blit(text, textpos)
            text = font.render("yspeed=" + str(self.ball.get_speed()[1]), 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.left = 820
            textpos.centery = 630
            self.screen.blit(text, textpos)
            # END DEBUG
            
            for finish in self.finishes:
                draw_finish = finish.rect.copy()
                draw_finish.centery = draw_finish.centery - 16
                self.screen.blit(self.sprites["finish"], draw_finish)  
            
            # Timer for next level
            if self.next_live_time > 0:
                timer = c.WAIT_TIME_BETWEEN_LIVES - int(time.time() - self.next_live_time)
                if timer > 0:
                    font_time = pygame.font.Font(None, 45)
                    text = font_time.render("Start in:", 1, (0, 0, 0))
                    textpos = text.get_rect()
                    textpos.left = 820
                    textpos.top = 150
                    self.screen.blit(text, textpos)
                    text = font_time.render(str(timer) + " seconds", 1, (0, 0, 0))
                    textpos = text.get_rect()
                    textpos.left = 820
                    textpos.top = 190
                    self.screen.blit(text, textpos)
            
            # Clicked location indicator
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.circle(self.screen, (0, 0, 0), (self.clicked_pos[0], self.clicked_pos[1]), 5)
            
        pygame.display.flip()
