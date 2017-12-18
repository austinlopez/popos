from graphics import *
import random

## Written by Sarina Canelake & Kelly Casteel, August 2010
## Revised January 2011

############################################################
# GLOBAL VARIABLES
############################################################
    
BLOCK_SIZE = 12
BLOCK_OUTLINE_WIDTH = 2
BOARD_WIDTH = 100
BOARD_HEIGHT = 60

midPointX = BOARD_WIDTH/2
midPointY = BOARD_HEIGHT/2

neighbor_test_blocklist = [(0,0), (1,1)]
toad_blocklist = [(4,4), (3,5), (3,6), (5,7), (6,5), (6,6)]
beacon_blocklist = [(2,3), (2,4), (3,3), (3,4), (4,5), (4,6), (5,5), (5,6)]
glider_blocklist = [(1,2), (2,3), (3,1), (3,2), (3,3)]
pulsar_blocklist = [(2,4), (2,5), (2,6), (4,2), (4,7), (5,2), (5,7),
                    (6,2), (6,7), (7,4), (7,5), (7,6), ]

line_blocklist = [(1,10),(2,10),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(10,10),(11,10),(12,10),(13,10),(14,10),(18,10),(19,10),(20,10),(27,10),(28,10),(29,10),(30,10),
                    (31,10),(32,10),(33,10),(35,10),(36,10),(37,10),(38,10),(39,10)]

acorn_blocklist = [(47,30),(48,30),(48,28),(50,29),(51,30),(52,30),(53,30)]
a5x5_blocklist = [(47,27),(48,27),(49,27),(51,27),(47,28),(50,29),(51,29),(48,30),(49,30),(51,30),(47,31),(49,31),(51,31)]
# for diehard, make board at least 25x25, might need to change block size
diehard_blocklist = [(5,7), (6,7), (6,8), (10,8), (11,8), (12,8), (11,6)]

############################################################
# TEST CODE (don't worry about understanding this section)
############################################################

def test_neighbors(board):
    '''
    Code to test the board.get_block_neighbor function
    '''
    for block in board.block_list.values():
        neighbors = board.get_block_neighbors(block)
        ncoords = [neighbor.get_coords() for neighbor in neighbors]
        if block.get_coords() == (0,0):
            zeroneighs = [(0,1), (1,1), (1,0)]
            for n in ncoords:
                if n not in zeroneighs:
                    print "Testing block at (0,0)"
                    print "Got", ncoords
                    print "Expected", zeroneighs
                    return False

            for neighbor in neighbors:
                if neighbor.get_coords() == (1, 1):
                    if neighbor.is_live() == False:
                        print "Testing block at (0, 0)..."
                        print "My neighbor at (1, 1) should be live; it is not."
                        print "Did you return my actual neighbors, or create new copies of them?"
                        print "FAIL: get_block_neighbors() should NOT return new Blocks!"
                        return False

        elif block.get_coords() == (1,1):
            oneneighs = [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1),(2,2)]
            for n in ncoords:
                if n not in oneneighs:
                    print "Testing block at (1,1)"
                    print "Got", ncoords
                    print "Expected", oneneighs
                    return False
            for n in oneneighs:
                if n not in ncoords:
                    print "Testing block at (1,1)"
                    print "Got", ncoords
                    print "Expected", oneneighs
                    return False
    print "Passed neighbor test"
    return True


############################################################
# BLOCK CLASS (Read through and understand this part!)
############################################################

class Block(Rectangle):
    ''' Block class:
        Implement a block for a tetris piece
        Attributes: x - type: int
                    y - type: int
        specify the position on the board
        in terms of the square grid
    '''

    def __init__(self, pos, color):
        '''
        pos: a Point object specifing the (x, y) square of the Block (NOT in pixels!)
        color: a string specifing the color of the block (eg 'blue' or 'purple')
        '''
        self.x = pos.x
        self.y = pos.y
        
        p1 = Point(pos.x*BLOCK_SIZE,
                   pos.y*BLOCK_SIZE)
        p2 = Point(p1.x + BLOCK_SIZE, p1.y + BLOCK_SIZE)

        Rectangle.__init__(self, p1, p2)
        self.setWidth(BLOCK_OUTLINE_WIDTH)
        self.setFill(color)
        self.status = 'dead'
        self.new_status = 'None'
        
    def get_coords(self):
        return (self.x, self.y)

    def set_live(self, canvas):
        '''
        Sets the block status to 'live' and draws it on the grid.
        Be sure to do this on the canvas!
        '''
        if self.status=='dead':
          self.status = 'live'
          self.draw(canvas)

    def set_dead(self):
        '''
        Sets the block status to 'dead' and undraws it from the grid.
        '''
        if self.status=='live':
          self.status = 'dead'
          self.undraw()

    def is_live(self):
        '''
        Returns True if the block is currently 'live'. Returns False otherwise.
        '''
        if self.status == 'live':
            return True
        return False

    def reset_status(self, canvas):
        '''
        Sets the new_status to be the current status
        '''
        if self.new_status=='dead':
            self.set_dead()
        elif self.new_status=='live':
            self.set_live(canvas)
        

###########################################################
# BOARD CLASS (Read through and understand this part!)
# Print out and turn in this section.
# Name:
# Recitation:
###########################################################

class Board(object):
    ''' Board class: it represents the Game of Life board

        Attributes: width - type:int - width of the board in squares
                    height - type:int - height of the board in squares
                    canvas - type:CanvasFrame - where the blocks will be drawn
                    block_list - type:Dictionary - stores the blocks for a given position
    '''
    
    def __init__(self, win, width, height):
        self.width = width
        self.height = height
        self.win = win
        # self.delay is the number of ms between each simulation. Change to be
        # shorter or longer if you wish!
        self.delay = 100

        # create a canvas to draw the blocks on
        self.canvas = CanvasFrame(win, self.width * BLOCK_SIZE,
                                       self.height * BLOCK_SIZE)
        self.canvas.setBackground('white')

        # initialize grid lines
        for x in range(1,self.width):
            self.draw_gridline(Point(x, 0), Point(x, self.height))

        for y in range(1,self.height):
            self.draw_gridline(Point(0, y), Point(self.width, y))

        # For each square on the board, we need to initialize
        # a block and store that block in a data structure. A
        # dictionary (self.block_list) that has key:value pairs of
        # (x,y):Block will be useful here.
        self.block_list = {}
        #for name in range(1,((self.width+1)*(self.height+1))):
        for columns in range(0,self.height):
            for rows in range(0,self.width):
                self.block_list[(rows,columns)] = Block(Point(rows,columns),'red')
        #print(sorted(self.block_list.keys()))
        ####### YOUR CODE HERE ######
        #raise Exception("__init__ not implemented")


    def draw_gridline(self, startp, endp):
        ''' Parameters: startp - a Point of where to start the gridline
                        endp - a Point of where to end the gridline
            Draws two straight 1 pixel lines next to each other, to create
            a nice looking grid on the canvas.
        '''
        line = Line(Point(startp.x*BLOCK_SIZE, startp.y*BLOCK_SIZE), \
                    Point(endp.x*BLOCK_SIZE, endp.y*BLOCK_SIZE))
        line.draw(self.canvas)
        
        line = Line(Point(startp.x*BLOCK_SIZE-1, startp.y*BLOCK_SIZE-1), \
                    Point(endp.x*BLOCK_SIZE-1, endp.y*BLOCK_SIZE-1))
        line.draw(self.canvas)


    def random_seed(self, percentage):
        ''' Parameters: percentage - a number between 0 and 1 representing the
                                     percentage of the board to be filled with
                                     blocks
            This method activates the specified percentage of blocks randomly.
        '''
        for block in self.block_list.values():
            if random.random() < percentage:
                block.set_live(self.canvas)

    def seed(self, block_coords):
        '''
        Seeds the board with a certain configuration.
        Takes in a list of (x, y) tuples representing block coordinates,
        and activates the blocks corresponding to those coordinates.
        '''

        for coords in block_coords:
            #print(coords)
            self.block_list[coords].set_live(self.canvas)

        #### YOUR CODE HERE #####
        #raise Exception("seed not implemented")
    


    def get_block_neighbors(self, block):
        '''
        Given a Block object, returns a list of neighboring blocks. -- Given as the name (coords)
        Should not return itself in the list. -- return the list with coords of neighbors
        '''
        blocks_around = []
        test = block.get_coords()
        #print(test)
        #print(block.x)
        #print(block.y)
        for xTest in [-1,0,1]:
            for yTest in [-1,0,1]:
                testPointx = block.x + xTest
                testPointy = block.y + yTest
                if (-1 < testPointx < self.width) and (-1 < testPointy < self.height):
                    if ((testPointx, testPointy) != block.get_coords()):
                        blocks_around.append(self.block_list[testPointx,testPointy])
                    
        # for xTest in [-1, 1]:
        #     for yTest in [-1, 0, 1]:
        #         #print(xTest,yTest)
        #         if (-1 < block.x + xTest < self.width) and (-1 < block.y + yTest < self.height):
        #             if self.block_list[(block.x + xTest, block.y + yTest)].is_live() == True:
        #                 blocks_around.append((block.x + xTest, block.y + yTest))
        
        #print(blocks_around)
        
        return blocks_around
        #### YOUR CODE HERE #####
        #### Think about edge conditions!
        #raise Exception("get_block_neighbors not implemented")
       

    def simulate(self):
        '''
        Executes one turn of Conways Game of Life using the rules
        listed in the handout. Best approached in a two-step strategy:
        
        1. Calculate the new_status of each block by looking at the
           status of its neighbors.

        2. Set blocks to 'live' if their new_status is 'live' and their
           status is 'dead'. Similarly, set blocks to 'dead' if their
           new_status is 'dead' and their status is 'live'. Then, remember
           to call reset_status(self.canvas) on each block.
        '''
        #ncoords = [neighbor.get_coords() for neighbor in neighbors]
        deadOnes = 0
        for block in self.block_list.values():
            neighbors = self.get_block_neighbors(block)
            ncoords = [neighbor.get_coords() for neighbor in neighbors]
            alive = 0
            
            if block.is_live() == False:
                #print(block.get_coords())
                #neighborsAlive = [(neighbor.is_live(),neighbor.get_coords()) for neighbor in neighbors]
                deadOnes += 1
                for n in ncoords:
                    #print(n)
                    if self.block_list[n].is_live() == True:
                        #print(self.block_list[n].get_coords())
                        #print(self.block_list[n].is_live())
                        alive += 1
                if (alive == 3):
                    block.new_status = 'live'
                    #print(neighborsAlive)
                else:
                    block.new_status = 'dead'
                alive = 0

            elif block.is_live() == True:
                #print(block.get_coords())
                #print(block.is_live())
                for n in ncoords:
                    if self.block_list[n].is_live() == True:
                        #print(self.block_list[n].get_coords())
                        #print(self.block_list[n].is_live())
                        #print("it is true")
                        alive += 1
                    #print(alive)
                #print("Final:",alive)
                if (2 <= alive <= 3):
                    block.new_status = 'live'
                    #print("Will stay alive")
                else:
                    block.new_status = 'dead'
            
            else:
                print("Error")
        


        for block in self.block_list.values():
            if block.is_live() == True:
                #print(block.new_status)
                block.reset_status(self.canvas)
            if block.is_live() == False:
                #print(block.new_status)
                block.reset_status(self.canvas)
                    
        


        # for block in board.block_list.values():
        #     alive = 0
        #     neighbors = self.get_block_neighbors(block)
        #     ncoords = [neighbor.get_coords() for neighbor in neighbors]
        #     if block.is_live() == True:
        #         #alive = 0
        #         for n in neighbors:
        #             if n.is_live() == True:
        #                 alive += 1
        #         if alive < 2:
        #             new_status = False
        #         elif alive > 3:
        #             new_status = False
        #         else:
        #             new_status = True
        #         print(block.get_coords())
        #         print(alive)
        #         print(new_status)
        #         print(n.get_coords())
        #     elif block.is_live() == False:
        #         #alive = 0
        #         for n in neighbors:
        #             if n.is_live() == True:
        #                 alive += 1
        #         if alive < 2:
        #             new_status = False
        #         elif alive > 3:
        #             new_status = False
        #         else:
        #             new_status = True
        
        # for block in board.block_list.values():     
        #     if new_status != block.is_live():
        #         if block.is_live() == True:
        #             block.set_dead()
        #         elif block.is_live() == False:
        #             block.set_live(self.canvas)
                    

        # for block in board.block_list.values():
        #     new_status= ''
        #     neighbors = self.get_block_neighbors(block)
        #     for neighbor in neighbors:
        #         if neighbor.is_live() == True:
        #             neighbors_alive += 1
        #     print(neighbors_alive, block.get_coords())
        #     if neighbors_alive == 2 or neighbors_alive == 3:
                
        #         block.new_status = 'live'
        #     elif neighbors_alive < 2 or neighbors_alive > 3:
        #         block.new_status = 'dead'

        # for block in board.block_list.values():
        #     block.reset_status(self.canvas)
        
        #### YOUR CODE HERE #####
        #raise Exception("simulate not implemented")

        

    def animate(self):
        '''
        Animates the Game of Life, calling "simulate"
        once every second
        '''
        self.simulate()
        self.win.after(self.delay, self.animate)



################################################################
# RUNNING THE SIMULATION
################################################################

if __name__ == '__main__':    
    # Initalize board
    win = Window("Conway's Game of Life")
    board = Board(win, BOARD_WIDTH, BOARD_HEIGHT)

    ## PART 1: Make sure that the board __init__ method works    
    #board.random_seed(1)

    ## PART 2: Make sure board.seed works. Comment random_seed above and uncomment
    ##  one of the seed methods below
    #board.seed(toad_blocklist)

    ## PART 3: Test that neighbors work by commenting the above and uncommenting
    ## the following two lines:
    #board.seed(neighbor_test_blocklist)
    #test_neighbors(board)


    ## PART 4: Test that simulate() works by uncommenting the next two lines:
    #board.seed(toad_blocklist)
    #board.seed(line_blocklist)
    #board.seed(acorn_blocklist)
    board.seed(a5x5_blocklist)
    #win.after(2000, board.simulate)

    ## PART 5: Try animating! Comment out win.after(2000, board.simulate) above, and
    ## uncomment win.after below.
    win.after(250, board.animate)
    
    ## Yay, you're done! Try seeding with different blocklists (a few are provided at the top of this file!)
    
    win.mainloop()
                


