# A* Search Algorithm 
# h1 - Nr of missplaced tiles; number of squares that are not in the right place. 
# Data structure: two lists, "open" & "closed"
# Open list = Nodes left to explore, explores most optimal with help of f = heuristics + path cost
# Closed list = Explored nodes

''' Define one Node and generate child states from the current state '''
class Node: 
    ''' Initialize a node '''
    def __init__(self, puzzle, level, f):
        # Initialize the node
        self.puzzle = puzzle # 
        self.level = level # level in the tree
        self.f = f # h+g (h = nr of misplaced tiles, g = the path cost)

    ''' Generate child nodes by moving all possible directions (moving blank space) '''
    def get_child(self):
        x, y = self.find(self.puzzle,'_') # find blank space
        positions = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]] # positions to move blank space in the 4 directions
        children = []

        for i in positions:
            child = self.move(self.puzzle, x, y, i[0], i[1]) # i[0]=x pos of child, i[1]=y pos of child, move blank to that position
            if child is not None: # make node and add to children
                child_node = Node(child, self.level+1, 0)
                children.append(child_node)
        return children
                

    ''' Move the blank space in the given direction and of the position value are out
        of limits then return None '''  
    def move(self, puzzle, x1, y1, x2, y2): 
        if x2 >= 0 and x2 <len(self.puzzle) and y2 >= 0 and y2 < len(self.puzzle):
            # Allocating memory to move the tiles
            temp_puzzle = [] 
            temp_puzzle = self.copy(puzzle) # copy the current puzzle
            temp = temp_puzzle[x2][y2] # Position of what we want to move the blank space too
            temp_puzzle[x2][y2] = temp_puzzle[x1][y1] # Gives the current blank the child 
            temp_puzzle[x1][y1] = temp # Moves the blank to the child 
            return temp_puzzle # returns the puzzle with the new moved tiles
        else:
            return None # If trying to move the empty tile out of bounds return none
        
    ''' Copy function to create a copy of the current puzzle matrix '''
    def copy(self, root): # root of the puzzle that is the input
        temp = [] 
        for i in root: 
            t = []
            for j in i:
                t.append(j) # append node to row
            temp.append(t) # append row to matrix

        return temp
    
    ''' Returns position of blank space '''
    def find(self, puzzle, blank):
        for i in range(0, len(self.puzzle)): 
            for j in range(0, len(self.puzzle)):
                if puzzle[i][j] == blank:
                    return i, j
   
    
''' Accepts the initial goal states of the N-Puzzle problem
    and provides the functions to calculate the f-score of any given node(state) '''
class Puzzle:
    ''' Initialize the puzzle ''' 
    def __init__(self, size):
        self.n = size # Size of the puzzle
        self.open = [] # Initialize the open list to empty
        self.closed = [] # Intialize the closed list to empty
        
    ''' Accepts puzzle from user '''
    def define_puzzle(self):
        puz = []
        for i in range(0, self.n):
            temp = input().split(' ')
            puz.append(temp)
        return puz
    
    ''' Heurisitc function to calculate heuristic value f(x) = h(x) + g(x) '''
    def cal_f(self, start, goal): 
        return self.cal_h(start.puzzle, goal) + start.level

    ''' Calcualtes the different between the given puzzles '''
    def cal_h(self, start, goal):
        counter = 0; 
        for i in range(0, self.n): #row
            for j in range(0, self.n): #col
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    counter += 1 # Counts all squares that are in the wrong position

        return counter
        
    ''' Accept start and goal puzzle state''' 
    def solve_puzzle(self):
        print('Enter puzzle at start state:')
        start = self.define_puzzle()
        # Enter own goal state
        #print('Enter puzzle at goal state')
        #goal = self.define_puzzle()
        
        # Pre-defined goal, increasing order
        goal = [['1', '2', '3'], ['4', '5', '6'],['7', '8', '_']]
        #print("\ngoal: ", goal)
        print('\nGoal State, increasing order:')
        print("1 2 3\n4 5 6\n7 8 _")
    
        start = Node(start, 0, 0)
        start.f = self.cal_f(start, goal) # calculate f by comparing start & goal state

        # Put start node in open list
        self.open.append(start)

        print('\n')
        print('Solution: ')

        iter = 0

        while True:
            current = self.open[0]
            print('')

            for i in current.puzzle:
                for j in i:
                    print(j, end = ' ')
                print('')

            # If goal node is reached
            if(self.cal_h(current.puzzle, goal) == 0): # reached if difference between current state and goal is 0
                break
            for i in current.get_child():
                i.f = self.cal_f(i, goal)
                if not any(node.puzzle == i.puzzle for node in self.open) and not any(node.puzzle == i.puzzle for node in self.closed): #i.puzzle not in self.open:
                    self.open.append(i)
                elif any(node.puzzle == i.puzzle for node in self.open):
                    for j in self.open:
                        if j.puzzle == i.puzzle:
                            if j.f > i.f:
                                del self.open[j]
                                self.open.append(i)



            self.closed.append(current)

            iter += 1

            del self.open[0]
           # for i in self.open:
             #   print(i.puzzle)

            # sort open list based of f value
            self.open.sort(key = lambda x:x.f, reverse = False)

        print('iterations: ', iter)

puz = Puzzle(3) # n = 3
puz.solve_puzzle()