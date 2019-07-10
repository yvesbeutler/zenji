from grid import Grid
from node import Node

def rotate(grid, position):
    """
    Rotate a single tile clockwise.
    """
    row = position[0]
    col = position[1]
    grid.nodes[row][col] = Node([
        grid.nodes[row][col].west,
        grid.nodes[row][col].north,
        grid.nodes[row][col].east,
        grid.nodes[row][col].south
    ], grid.nodes[row][col].is_goal)

def depth_search(origin, pos, grid):
    """
    Approach to solve the zenji puzzle with a recursive depth search.
    """
    # check borders
    if (pos[0] == grid.size or pos[1] == grid.size):
        print('outside')
        return -1

    # rotate max 3 times
    for _i in range(4):
        node = grid.nodes[pos[0]][pos[1]]
        # if water input is at right place
        if node.values[origin] == 1:
            # check goal state
            if node.is_goal == True:
                print('goal')
                return 1
            if node.east == 2:
                # go right
                print('right')
                x = depth_search(3, (pos[0], pos[1]+1), grid)
                if x == 1: return 1
            if node.south == 2:
                # go down
                print('down')
                x = depth_search(0, (pos[0]+1, pos[1]), grid)
                if x == 1: return 1
            
            # try to rotate
            print('rotate')
            rotate(grid, pos)
        else:
            print('rotate')
            rotate(grid, pos)

    # this node is a dead end
    print('dead end')
    return -1

def main():

    grid = Grid([
        [[1,2,2,0], [2,1,0,0]],
        [[1,2,1,2], [0,0,1,0]]
    ])

    grid = Grid([
        [[1, 0, 2, 0], [1, 0, 1, 2], [1, 0, 2, 0], [0, 0, 0, 0]],
        [[0, 0, 1, 2], [0, 1, 0, 2], [1, 0, 0, 2], [0, 0, 0, 0]],
        [[1, 2, 2, 1], [1, 2, 2, 0], [0, 2, 0, 1], [2, 1, 0, 2]],
        [[0, 0, 1, 0], [0, 0, 1, 2], [0, 1, 0, 2], [0, 0, 0, 1]]
    ])

    grid.print("Initial State")

    # solve the riddle
    solution = depth_search(3, (0,0), grid)
    
    grid.print("Goal State")

    if solution != 1: print('The solution was not found!')

if __name__ == "__main__":
    main()