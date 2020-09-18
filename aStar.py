from Map import Map_Obj
import time

def generateAllSuccessors(node):
    """Generates all potential successor nodes for a given node"""

    # The positions of the nodes to each intermediate direction
    positions = [
        [node.pos[0]+1,node.pos[1]],
        [node.pos[0]-1,node.pos[1]],
        [node.pos[0],node.pos[1]+1],
        [node.pos[0],node.pos[1]-1]
    ]

    successors = []
    for position in positions:

        # Ensuring that the positions are inside of the map and that they are not walls
        if 0 <= position[0] <= map.str_map.shape[0] and 0 <= position[1] <= map.str_map.shape[1] and map.get_cell_value(position) >= 1:
            successor = Node(node,position)
            successors.append(successor)

    return successors

def attachAndEval(successor,parent):
    """Updates the successors parent and distance"""

    successor.parent = parent
    successor.g = parent.g + arcCost(successor.pos)

def arcCost(pos):
    """Gives the cost of a single cell"""

    return map.get_cell_value(pos)

def h(pos,goal_pos):
    """Heuristic function that gives the minimum distance to the goal"""

    return abs(pos[0]-goal_pos[0]) + abs(pos[1]-goal_pos[1]) #Manhattan distance 
 
class Node:
    """Node structure"""

    def __init__ (self,parent = None,pos = None):
        self.parent =  parent
        self.pos = pos
        self.g = 0
        self.h = h(self.pos,map.goal_pos)

    # Comparision operator used to compare the state of two nodes 
    def __eq__ (self,node):
        return self.pos == node.pos 

def aStar(start_pos,goal_pos):
    """A* best-first search algorithm"""

    print(f"Initiating A* search from {start_pos} to {goal_pos}")
    print(f"----------------------------------------------------")
    start_time = time.time()
    
    CLOSED = [] # Untraversed nodes
    OPEN = [] # Traversed nodes

    startNode = Node(None,start_pos) # Generate the initial node for the start state.
    OPEN.append(startNode)

    while(OPEN):

        # If the goal position moves
        map.tick()
        goal_pos = map.get_goal_pos() 

        # Priority queue based on the sum of the path distance and the heuristic distance
        current = min(OPEN, key=lambda Node:Node.g + Node.h)

        OPEN.remove(current)
        CLOSED.append(current)

        # Check if the current node is the goal node, and if so, loop backwards through the parents to get the path
        if current.pos == goal_pos:
            path = []
            while current.parent:
                path.append(current.pos)
                current = current.parent
            path.append(current.pos)

            print(f"Path:{path[::-1]}")
            print(f"The execution of the script took a total of {round(time.time() - start_time,2)} seconds ")
            return path[::-1]

        # Generate the successors of the current node
        successors = generateAllSuccessors(current)
        for successor in successors:

            # If a successor is in the closed list, the optimal path to it has already been found
            if successor in CLOSED:
                continue

            # If a successor is in the open list, check if the path through the current node is shorter
            elif successor in OPEN:
                if current.g + arcCost(successor.pos) < successor.g:
                    attachAndEval(successor,current)
         
            # The node was expanded for the first now
            else:
                attachAndEval(successor,current)
                OPEN.append(successor)
    
    raise ValueError("Could not find a path")

map = Map_Obj(3)
path = aStar(map.start_pos,map.goal_pos)

# Draw the path
for i in range(1,len(path)-1):
    map.set_cell_value(path[i], "  ", str_map = True)    

map.show_map()







