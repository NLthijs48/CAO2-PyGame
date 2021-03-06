'''
Created on 23 jan. 2015

@author: Sjoerd
'''
import pygame
import game.constants as c

class Ball(object):
    
    #game object
    game = ''
    
    #ball objects
    start_position = [0.0, 0.0]     # Start position from the map
    ball_position = [16.0, 16.0]    # Ball position when started
    speed_x = 0.0
    speed_y = 0.0
    lives = 3
    lives_down_set = False
    hole_overlap = 12
        
    def __init__(self, position, hole_overlap, game):
        self.ball_position[0] = position[0]
        self.ball_position[1] = position[1]
        self.start_position[0] = position[0]
        self.start_position[1] = position[1]
        self.lives = 3
        self.lives_down_set = False
        self.rect = pygame.Rect(position[0], position[1], c.OBJECT_SIZE, c.OBJECT_SIZE)
        self.hole_overlap = hole_overlap
        self.game = game
        
    def move(self, x, y):
        if (x != 0):
            self.move_axis(x, 0)
        if (y !=0):
            self.move_axis(0, y)
    
    def move_axis(self, x, y):
        
        self.ball_position[0]+= x
        self.ball_position[1]+= y 
        
        # Round the float position to the rect. 
        self.rect.x = round(self.ball_position[0])
        self.rect.y = round(self.ball_position[1])
        
            
        for wall in self.game.getWalls():
            if self.rect.colliderect(wall.rect):
                if x > 0:
                    self.rect.right = wall.rect.left
                    self.ball_position[0] = self.rect.left
                    self.speed_x = 0
                if x < 0: 
                    self.rect.left = wall.rect.right
                    self.ball_position[0] = self.rect.left
                    self.speed_x = 0
                if y > 0: 
                    self.rect.bottom = wall.rect.top
                    self.ball_position[1] = self.rect.top
                    self.speed_y = 0
                if y < 0:
                    self.rect.top = wall.rect.bottom
                    self.ball_position[1] = self.rect.top
                    self.speed_y = 0
        
        # Check for holes
        for hole in self.game.getHoles():
            if self.rect.right > (hole.rect.left + self.hole_overlap) and self.rect.left < (hole.rect.right - self.hole_overlap) and self.rect.top < (hole.rect.bottom - self.hole_overlap) and self.rect.bottom > (hole.rect.top + self.hole_overlap):
                self.lives_down()
        
        for finish in self.game.getFinishes():
            if self.rect.right > (finish.rect.left + self.hole_overlap) and self.rect.left < (finish.rect.right - self.hole_overlap) and self.rect.top < (finish.rect.bottom - self.hole_overlap) and self.rect.bottom > (finish.rect.top + self.hole_overlap):
                self.game.setWin()
                
        # Update the rect poisiton  
        self.rect.x = round(self.ball_position[0])
        self.rect.y = round(self.ball_position[1])
    
    def lives_down(self):
        self.lives-=1
        self.ball_position[0] = self.start_position[0]
        self.ball_position[1] = self.start_position[1]
        self.speed_x = 0
        self.speed_y = 0
        if self.lives > 0:
            self.game.nextLive()

    
    def set_speed(self, speed):
        self.speed_x = speed[0]
        self.speed_y = speed[1]
    
    def get_speed(self):
        return [self.speed_x, self.speed_y]
    
    def set_live(self, lives):
        self.lives = lives
    
    def get_lives(self):
        return self.lives