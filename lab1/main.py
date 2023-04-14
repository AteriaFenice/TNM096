# A* Search Algorithm 
# h1 - Nr of missplaced tiles; number of squares that are not in the right place. 
# Data structure: two lists, "open" & "closed"
# Open list = Nodes left to explore, explores most optimal with help of f = heuristics + path cost
# Closed list = Explored nodes
from itertools import chain
from queue import PriorityQueue
import time
import copy

heuristics = input('Enter heuristic method: \nh1: Misplaced tiles \nh2: Manhattan Distance\n')

''' Define one Node and generate child states from the current state '''
class Node: 
    ''' Initialize a node '''
    def __init__(self, puzzle, level, h, parent = None):
        # Initialize the node
        self.puzzle = puzzle # 
        self.level = level # level in the tree
        self.h = h # h+g (h = nr of misplaced tiles, g = the path cost)
        self.parent = parent

    def __lt__(self, other): # less than operator
        return self.f() < other.f()
    
    '''Heurisitc function to calculate heuristic value f(x) = h(x) + g(x)'''
    def f(self):
        return self.level + self.h
        
''' Calcualtes the different between the given puzzles '''
def h1(start, goal):
    counter = 0
    for i in range(0, 3): #row
        for j in range(0, 3): #col
            if start[i][j] != goal[i][j] and start[i][j] != '_':
                counter += 1 # Counts all squares that are in the wrong position
    return counter

''' Manhattan Distance '''
def h2(start, goal):
    counter = 0

    for i in range(0, 3): #row
        for j in range(0, 3): #col
            if start[i][j] != goal[i][j] and start[i][j] != '_':

                for x in range(0, 3): 
                    for y in range(0, 3):
                        if goal[x][y] == start[i][j]:
                            x_pos = x
                            y_pos = y
                            break

                # calculate distance 
                manhattan = abs(i-x_pos) + abs(j-y_pos)

                counter += manhattan # Counts all manhattan distances of squares that are in the wrong position 

    return counter

''' Generate child nodes by moving all possible directions (moving blank space) '''
def get_child(self):
    x, y = find(self.puzzle,'_') # find blank space
    positions = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]] # positions to move blank space in the 4 directions
    children = []

    for i in positions:
        child = move(self.puzzle, x, y, i[0], i[1]) # i[0]=x pos of child, i[1]=y pos of child, move blank to that position
        if child is not None: # make node and add to children
            #child_node = Node(child, self.level+1, 0)
            children.append(child)
    return children

''' Returns position of blank space '''
def find(puzzle, blank):
    for i in range(0, len(puzzle)): 
        for j in range(0, len(puzzle)):
            if puzzle[i][j] == blank:
                return i, j
            

''' Move the blank space in the given direction and of the position value are out
    of limits then return None '''  
def move(puzzle, x1, y1, x2, y2): 
    if x2 >= 0 and x2 <len(puzzle) and y2 >= 0 and y2 < len(puzzle):
        # Allocating memory to move the tiles
        temp_puzzle = [] 
        temp_puzzle = copy.deepcopy(puzzle) # copy the current puzzle
        temp = temp_puzzle[x2][y2] # Position of what we want to move the blank space too
        temp_puzzle[x2][y2] = temp_puzzle[x1][y1] # Gives the current blank the child 
        temp_puzzle[x1][y1] = temp # Moves the blank to the child 
        return temp_puzzle # returns the puzzle with the new moved tiles
    else:
        return None # If trying to move the empty tile out of bounds return none
     
def a_star(start_puzzle, goal_puzzle, heuristics):
    start = Node(start_puzzle, level = 0, h = heuristics(start_puzzle, goal_puzzle))
    #goal = Node(goal)

    open = PriorityQueue()
    open.put(start)

    closed = set()

    it = 0 

    while not open.empty():
        current = open.get()
        
        if current.puzzle == goal_puzzle:
            path = []
            while current.parent is not None:
                path.append(current.puzzle)
                current = current.parent
            path.append(start)
            path.reverse()

            print()
            print("iterations: ", it)
            return path
        
        closed.add(tuple(map(tuple,current.puzzle)))
        it += 1

        for child in get_child(current):
            child_puzzle = tuple(map(tuple, child))

            if child_puzzle not in closed:
                child_node = Node(child, level=current.level+1, h = heuristics(start_puzzle, goal_puzzle), parent = current)
                open.put(child_node)

    return None

'''Accepts puzzle from user'''
def define_puzzle():
    puz = []
    for i in range(0, 3):
        temp = input().split(' ')
        puz.append(temp)
    return puz


print('Enter puzzle at start state:')
# Enter puzzle to solve
start = define_puzzle()

# Pre-defined goal, increasing order
goal = [['1', '2', '3'], ['4', '5', '6'],['7', '8', '_']]
#print("\ngoal: ", goal)
print('\nGoal State, increasing order:')
print("1 2 3\n4 5 6\n7 8 _")

st = time.time() # Start time

path = a_star(start, goal, eval(heuristics))

et = time.time() # End time

if path is not None:
    print('Number of moves:', len(path)-1)
    print()

    counter = 0
    for i in path:
        
        if counter != 0:
            print('Step: ', counter)
            for row in range(0,3):
                print( i[row][0], i[row][1], i[row][2])
            print()
        counter += 1

    print("time: ", et-st, 's')

else: 
    print('no solution found')

#print('solved puzzle!')
#print('nr of iterations: ', it)

