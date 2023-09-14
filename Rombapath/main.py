

import pygame, sys,os.path
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


cwd =  os.path.join(os.path.curdir,'Rombapath')
mapa_img = os.path.join(cwd,'map.png')
selection_img = os.path.join(cwd,'selection.png')
roomba_img = os.path.join(cwd,'roomba.png')


class Roomba(pygame.sprite.Sprite):
    
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(roomba_img).convert_alpha()
        self.rect = self.image.get_rect(center = (60,60))
        
        #movement
        self.pos = self.rect.center 
        self.speed = 0.6
        self.direction = pygame.math.Vector2(0,0)
        
        # path
        self.path = []
        
        
        
        

class PathFinder:
    def __init__(self,matrix) -> None:
        self.matrix = matrix
        self.grid = Grid(matrix=matrix)
        self.select_surf = pygame.image.load(selection_img).convert_alpha()
        
        
        #pathfinding
        self.path = []
        
        # Roomba
        self.roomba = pygame.sprite.GroupSingle(Roomba())
        

    def create_path(self):
        #start
        start_x,start_y = [1,1]
        start = self.grid.node(start_x,start_y)
        #end
        x,y = pygame.mouse.get_pos()
        end_x,end_y = x // 32,y // 32
        end = self.grid.node(end_x,end_y)
        
        #path
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        tmp_path, _ = finder.find_path(start,end,self.grid)
        self.path =  [ (x,y) for x,y in tmp_path ]
        
        self.grid.cleanup()
        #print(self.path)
        
        
    def draw_path(self):
        if self.path:
            #points = [ ( (x*32)+16 ,(y*32)+16 ) for x,y in self.path]
            points = []
            
            for point in self.path:
                x = (point[0] * 32) +16
                y = (point[1] * 32) +16
                
                points.append( ( x,y ) )
                pygame.draw.circle(screen,'#4a4a4a',(x,y),2)
            
            pygame.draw.lines(screen,color='#4a4a4a',closed=False,points=points,width=5)

    def draw_active_cell(self):
        x,y = pygame.mouse.get_pos()
        #print(mouse_pos) #50,14 each cell is 32 pixels high and wide
        row = y // 32
        col = x // 32
        current_cell_value = self.matrix[row][col]
        
        if current_cell_value == 1:
            rect = pygame.Rect( (col * 32, row * 32),(32,32))
            screen.blit(self.select_surf,rect)
        #print(f'x:{x} y:{y} row:{row} col:{col}, col*32:{col*32},row*32:{row*32},')
        
        
    def update(self):
        self.draw_active_cell()
        self.draw_path()
        
        # Roomba updating and drawing
        self.roomba.update()
        self.roomba.draw(screen)
        

pygame.init()
screen = pygame.display.set_mode((1280,736))
clock = pygame.time.Clock()


bg_surf = pygame.image.load(mapa_img).convert()
matrix = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0],
    [0,1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0],
    [0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

pathfinder = PathFinder(matrix)

#print( (tmp:=list(map(len,matrix)))[0],len(tmp) ) #23,40

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pathfinder.create_path()
    
    screen.blit(bg_surf,(0,0))
    pathfinder.update()        
    
    pygame.display.update()
    clock.tick(60)