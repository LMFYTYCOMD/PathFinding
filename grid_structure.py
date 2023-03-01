import algorithms
from random import randint

class Node:
    def __init__(self, x, y, face_val = 0):
        self.face_val = face_val
        self.coordinate = (x, y)
        self.obs = False

    def __repr__(self) -> str:
        return str(self.face_val)

    def __lt__(self, other):
        return self.coordinate < other.coordinate

    def change_face_val(self, new_val):
        self.face_val = new_val

    def reset(self):
        self.face_val = 0
        self.obs = False

class Grid:
    def __init__(self, x_num, y_num):
        self.grid = [[Node(x, y) for x in range(x_num)] for y in range(y_num)]

    def print_grid(self):
        for row in self.grid:
            print(row)

    def reset_grid_value(self):
        for row in self.grid:
            for node in row:
                if node.face_val != 'O':
                    node.face_val = 0

    def set_obs(self, percentage):
        for row in self.grid:
            for node in row:
                if randint(1, 100) <= percentage:
                    node.obs = True
                    node.face_val = 'O'



# grid1 = Grid(10,10)
# grid2 = Grid(10,10)
# grid3 = Grid(10,10)
# grid4 = Grid(10,10)

# algorithms.A_star.a_star(grid1.grid, 3, 5, 9, 9)
# grid1.print_grid()
# print('\n')

# algorithms.Dijkstra.dijkstra(grid2.grid, 3, 5 ,9, 9)
# grid2.print_grid()
# print('\n')

# algorithms.DFS.depth_first(grid3.grid, 3, 5, 9, 9)
# grid3.print_grid()
# print('\n')

# algorithms.BFS.breath_first(grid4.grid, 3, 5, 9, 9)
# grid4.print_grid()
# print('\n')





















































