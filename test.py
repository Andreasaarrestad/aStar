import csv


def g():
    pass

def h():
    pass

def generateAllSuccessors(node,grid):
    pass


class node:

    def __init__ (self,value,pos):
        self.g = 0
        self.h = 0
        self.parent = None
        self.value = value
        self.pos = pos
        

def bestFirstSearch(start,goal):

    # List of nodes to be traversed
    CLOSED = []

    # List of already traversed nodes
    OPEN = []

    # Generate the initial node, n0, for the start state.
    current = start

    OPEN.append(current)

    while(OPEN):
        
        x = OPEN.pop()
        CLOSED.append(x)

        if x.pos == goal:
            return x

        #successors = generateAllSuccessors(x)

        #for s in successors:
            
def mainMethod():
    print("hello")

mainMethod()