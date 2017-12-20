import pygame, sys, random, time
from pygame.locals import *
from threading import Timer

# Constants
gameActive = True
PAUSE = False

BLOCK_SIZE = 30
OUTLINE_WIDTH = 3

BOARD_WIDTH = 12
BOARD_HEIGHT = 20
OUTLINE_BLOCKS = 1

BG_COLOR = [211,211,255]


CYAN = [0,255,255] # I Shape
DARK_ORANGE = [255,165,0] # L Shape
Color = [255,105,180] # J Shape
YELLOW = [255,255,0] #[255,250,205]
PURPLE = [155,48,255] # T Shape
RED = [255,0,0] # Z Shape
GREEN = [0,255,0] # S Shape

# Functions

def playSound(name, times=0):
    path = ''
    try:
        pygame.mixer.music.load(path+name)
        pygame.mixer.music.play(times)
    except pygame.error:
        print('There is no file with this name')

def randomColor():
    color = [random.randrange(1,250),random.randrange(1,250),random.randrange(1,250)]
    return color

def text_to_screen(screen, text, x, y, size = 50,
            color = (50, 50, 50), font_type = None):
    try:

        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception as e:
        print('Font Error, saw it coming')
        raise e

# Classes

class Block():

    def __init__(self, color, pos, outlineColor=[0,0,0]):
        self.color = color
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.outlineColor = outlineColor

    def draw(self, screen):
        self.piece = pygame.draw.rect(screen,self.outlineColor,[self.x*BLOCK_SIZE+OUTLINE_WIDTH-2,self.y*BLOCK_SIZE+OUTLINE_WIDTH-2,BLOCK_SIZE+1,BLOCK_SIZE+1],OUTLINE_WIDTH)
        self.piece1 = pygame.draw.rect(screen,self.color,[self.x*BLOCK_SIZE+OUTLINE_WIDTH,self.y*BLOCK_SIZE+OUTLINE_WIDTH,BLOCK_SIZE-OUTLINE_WIDTH,BLOCK_SIZE-OUTLINE_WIDTH])
        #self.outline = pygame.draw.lines(screen,[0,0,0],True,self.points,OUTLINE_WIDTH)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        #print('moving')
        #Rect.move(self, self.x*BLOCK_SIZE, self.y*BLOCK_SIZE)
    
    def changeColor(self,color,oulineColor=None):
        self.color = color
        if not oulineColor == None:
            self.outlineColor = outlineColor

    def canMove(self, board, dx, dy):
        futureX = self.x + dx
        futureY = self.y + dy
        if not board.canMove(futureX,futureY):
            return False
        return True

class Shape():
    
    def __init__(self, coordinates, color):
        self.blocks = []
        self.rotationDir = 1
        self.shiftRotateDir = False
        
        for pos in coordinates:
            self.blocks.append(Block(color, pos))

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)
    
    def move(self, dx, dy):
        for block in self.blocks:
            block.move(dx, dy)

    def getBlocks(self):
        return self.blocks

    def canMove(self, board, dx, dy):
        for block in self.blocks:
            if not block.canMove(board, dx, dy):
                return False
        return True

    def getRotateDir(self):
        return self.rotationDir

    def canRotate(self, board):
        direction = self.getRotateDir()
        for block in self.blocks:
            futureX = self.center_block.x - direction*self.center_block.y + direction*block.y
            futureY = self.center_block.y + direction*self.center_block.x - direction*block.x
            if not board.canMove(futureX, futureY):
                return False
        return True

    def rotate(self, board):
        direction = self.getRotateDir()

        for block in self.blocks:
            futureX = self.center_block.x - direction*self.center_block.y + direction*block.y
            futureY = self.center_block.y + direction*self.center_block.x - direction*block.x
            block.move(futureX-block.x,futureY-block.y)
        
        # After rotate, switch the direction
        if self.shiftRotateDir:
            self.rotationDir *= -1


class I_Shape(Shape):
    def __init__(self, center):
        coords = [(center[0]-2,center[1]),(center[0]-1,center[1]),(center[0],center[1]),(center[0]+1,center[1])]
        Shape.__init__(self, coords, randomColor())
        #Shape.__init__(self, coords, CYAN)
        self.center_block = self.blocks[2]
        self.shiftRotateDir = True

class J_Shape(Shape):
    def __init__(self, center):
        coords = [(center[0]-1,center[1]),(center[0],center[1]),(center[0]+1,center[1]),(center[0]+1,center[1]+1)]
        Shape.__init__(self, coords, randomColor())
        #Shape.__init__(self, coords, Color)
        self.center_block = self.blocks[1]

class L_Shape(Shape):
    def __init__(self, center):
        coords = [(center[0]-1,center[1]+1),(center[0]-1,center[1]),(center[0],center[1]),(center[0]+1,center[1])]
        Shape.__init__(self, coords, randomColor())
        #Shape.__init__(self, coords, DARK_ORANGE)
        self.center_block = self.blocks[2]

class O_Shape(Shape):
    def __init__(self, center):
        coords = [(center[0],center[1]),(center[0]+1,center[1]),(center[0]+1,center[1]+1),(center[0],center[1]+1)]
        Shape.__init__(self, coords, randomColor())
        #Shape.__init__(self, coords, YELLOW)
        self.center_block = self.blocks[1]
    
    def rotate(self, board):
        # Over ride the Shape Function Since no rotate
        return

class T_Shape(Shape):
    def __init__(self, center):
        coords = [(center[0]-1,center[1]),(center[0],center[1]),(center[0]+1,center[1]),(center[0],center[1]+1)]
        Shape.__init__(self, coords, randomColor())
        #Shape.__init__(self, coords, PURPLE)
        self.center_block = self.blocks[1]

class Z_Shape(Shape):
    def __init__(self, center):
        coords = [(center[0]-1,center[1]),(center[0],center[1]),(center[0],center[1]+1),(center[0]+1,center[1]+1)]
        Shape.__init__(self, coords, randomColor())
        #Shape.__init__(self, coords, RED)
        self.center_block = self.blocks[1]
        self.shiftRotateDir = True

class S_Shape(Shape):
    def __init__(self, center):
        coords = [(center[0]+1,center[1]),(center[0],center[1]),(center[0],center[1]+1),(center[0]-1,center[1]+1)]
        Shape.__init__(self, coords, randomColor())
        #Shape.__init__(self, coords, GREEN)
        self.center_block = self.blocks[1]
        self.shiftRotateDir = True

###
### Game Board
###

class Game_Board():

    def __init__(self, board_width, board_height):
        self.background = [211,211,211]
        self.board_width = board_width
        self.board_height = board_height
        self.active = {}
        self.border = {}

    def initBorder(self):
        for y in range(0,BOARD_HEIGHT+2):
            if y == 0 or y == BOARD_HEIGHT + OUTLINE_BLOCKS:
                for x in range(0,BOARD_WIDTH+2):
                    #self.border[(x,y)] = Block(randomColor(),[x,y])
                    #self.border[(x,y)] = Block([255,255,255],[x,y])
                    #self.border[(x,y)] = Block([0,0,0],[x,y],[255,255,255])
                    pass
            else:
                for x in [0,BOARD_WIDTH+OUTLINE_BLOCKS]:
                    #self.border[(x,y)] = Block(randomColor(),[x,y])
                    #self.border[(x,y)] = Block([255,255,255],[x,y])
                    #self.border[(x,y)] = Block([0,0,0],[x,y],[255,255,255])
                    pass

    def changeBorderColor(self):
        for block in self.border:
            self.border[block].changeColor(randomColor())
    
    def changeActiveColor(self):
        for block in self.active:
            self.active[block].changeColor(randomColor())
    
    def clearBoard(self):
        self.active.clear()

    def drawShape(self, shape):
        if shape.canMove(self, 0, 0):
            shape.draw(screen)
            return True
        return False

    def drawPieces(self):
        if not PAUSE:
            for block in self.active:
                self.active[block].draw(screen)
        for block in self.border:
            self.border[block].draw(screen)

    def canMove(self, x, y):
        if (OUTLINE_BLOCKS<= x < BOARD_WIDTH+OUTLINE_BLOCKS) and (OUTLINE_BLOCKS <= y < BOARD_HEIGHT+OUTLINE_BLOCKS):
            if (x,y) in self.active:
                return False
            return True
        else:
            return False

    def addShape(self, shape):
        blocks = shape.getBlocks()

        for block in blocks:
            self.active[block.x,block.y] = block
        playSound('Boi.mp3')
        #self.checkCompleteRow()

    def checkCompleteRow(self):
        completed = 0
        rows = []
        sounds = ['TheTingGoes.mp3','PopPop.mp3']
        for y in range(OUTLINE_BLOCKS,BOARD_HEIGHT+OUTLINE_BLOCKS):
            if self.isRowComplete(y):
                completed += 1
                rows.append(y)
        for y in rows:
            self.clearRow(y)
            self.moveRowsDown(y)
        if completed > 0:
            playSound(sounds[random.randint(0,1)])
        return completed

    def isRowComplete(self, y):
        for x in range(OUTLINE_BLOCKS,BOARD_WIDTH+OUTLINE_BLOCKS):
            if not (x,y) in self.active:
                return False
        return True
    
    def clearRow(self, y):
        for x in range(OUTLINE_BLOCKS,BOARD_WIDTH+OUTLINE_BLOCKS):
            del self.active[x,y]
    
    def moveRowsDown(self, yStart):
        for y in range(yStart-1,OUTLINE_BLOCKS,-1):
            for x in range(0,BOARD_WIDTH+OUTLINE_BLOCKS):
                if (x,y) in self.active:
                    block = self.active[x,y]
                    del self.active[x,y]
                    block.move(0,1)
                    self.active[block.x,block.y] = block

    def gameOver(self):
        print('Game Over')
        gameActive = False
        self.clearBoard()

###
### Tetris Class
###

class Tetris():
    
    SHAPES = [I_Shape, J_Shape, L_Shape, O_Shape ,T_Shape, Z_Shape, S_Shape]
    DIRECTIONS = {'Left':(-1,0), 'Right':(1,0), 'Up':(0,-1), 'Down':(0,1)}

    def __init__(self, screen):
        self.gameBoard = Game_Board(BOARD_WIDTH,BOARD_HEIGHT)
        self.delay = 1 # ms
        PAUSE = False
        gameActive = True
        self.gameBoard.initBorder()
        self.linesCleared = 0
        self.score = 0

        self.currentShape = self.creatNewShape()
        #self.gameBoard.drawShape(self.currentShape)
        self.t = Timer(self.delay, self.animateShape)

        self.animateShape()
    
    def creatNewShape(self):
        #whichBlock = Tetris.SHAPES[random.randrange(0,len(Tetris.SHAPES))]
        whichBlock = I_Shape
        print('Creating Shape...',whichBlock)
        newBlock = whichBlock([int((BOARD_WIDTH+2)/2),OUTLINE_BLOCKS])
        return newBlock

    def drawPieces(self):
        self.gameBoard.drawPieces()
        self.gameBoard.drawShape(self.currentShape)

    def animateShape(self):
        #self.t.cancel()
        self.moveCurrentShape('Down')
        self.t = Timer(self.delay,self.animateShape)
        self.t.start()

    def moveCurrentShape(self, direction):
        if direction == 'Space':
            while self.currentShape.canMove(self.gameBoard,0,1):
                self.currentShape.move(0,1)
            return
        dx = Tetris.DIRECTIONS[direction][0]
        dy = Tetris.DIRECTIONS[direction][1]
        if self.currentShape.canMove(self.gameBoard,dx,dy):
            self.currentShape.move(dx, dy)
            #self.gameBoard.checkCompleteRow()
            return True
        elif direction == 'Down':
            self.gameBoard.addShape(self.currentShape)
            self.linesCleared += self.gameBoard.checkCompleteRow()
            self.currentShape = self.creatNewShape()
            if not self.currentShape.canMove(self.gameBoard,0,0):
                self.gameBoard.gameOver()
            return False

    def rotateCurrentShape(self):
        if self.currentShape.canRotate(self.gameBoard):
            self.currentShape.rotate(self.gameBoard)


# Start Drawing
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([BLOCK_SIZE * (BOARD_WIDTH+2) + OUTLINE_WIDTH, BLOCK_SIZE * (BOARD_HEIGHT+2) + OUTLINE_WIDTH])
pygame.display.set_caption('Some Tetris Thing')

# pygame.draw.rect(screen,[0,255,0], [100,50,50,150]) # left test
# pygame.draw.rect(screen,[0,255,0], [150,50,150,50]) # top test
# pygame.draw.rect(screen,[0,255,0], [200,50,50,150]) # right test
# pygame.draw.rect(screen,[0,255,0], [100,150,150,50]) # bottom test

# shape3 = I_Shape([4,3])
# shape1 = J_Shape([8,3])
# shape2 = L_Shape([10,3])
# shape = O_Shape([13,3])


game = Tetris(screen)
pygame.key.set_repeat(200,50)

while gameActive:
    screen.fill(BG_COLOR)
    pygame.event.pump()
    msElapsed = clock.tick(60)
    #print(msElapsed)

    text_to_screen(screen,"Lines: {0}".format(game.linesCleared),30,100)
    text_to_screen(screen,"Score: {0}".format(game.score),30,150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try:
                game.t.cancel()
                print('Timer Stopped')
            except Exception as e:
                raise e
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_DOWN:
                game.moveCurrentShape('Down')
            if event.key == K_LEFT:
                game.moveCurrentShape('Left')
            if event.key == K_RIGHT:
                game.moveCurrentShape('Right')
            if event.key == K_UP:
                game.rotateCurrentShape()
                #game.moveCurrentShape('Up')
            if event.key == K_SPACE:
                game.moveCurrentShape('Space')
            if event.key == K_c:
                game.gameBoard.changeBorderColor()
            if event.key == K_v:
                game.gameBoard.changeActiveColor()

    game.drawPieces()

    #key = pygame.key.get_pressed()
    #if key[pygame.K_a]: print('a')
    # if key[pygame.K_UP]: shape.move(0,-1)
    # if key[pygame.K_DOWN]: shape.move(0,1)
    # if key[pygame.K_LEFT]: shape.move(-1,0)
    # if key[pygame.K_RIGHT]: shape.move(1,0)
    # if count % 5000 == 0:
    #     print('Focused:',pygame.key.get_focused())
    #     #print('Sharing:',pygame.event.get_grab())
    # shape.draw(screen)
    # shape1.draw(screen)
    # shape2.draw(screen)
    # shape3.draw(screen)

    pygame.display.flip()

if not gameActive:
    pygame.QUIT();sys.exit()