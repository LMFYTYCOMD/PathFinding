import algorithms

class Node:
    def __init__(self, x, y, face_val = 0):
        self.face_val = face_val
        self.coordinate = (x, y)

    def __repr__(self) -> str:
        return str(self.face_val)

    def __lt__(self, other):
        return self.coordinate < other.coordinate

    def change_face_val(self, new_val):
        self.face_val = new_val


class Grid:
    def __init__(self, x_num, y_num):
        self.grid = [[Node(x, y) for x in range(x_num)] for y in range(y_num)]

    def print_grid(self):
        for row in self.grid:
            print(row)


#access node in the grid by grid[y][x], the value return will be coordinate of x, y. For example grid[1][2] = (2, 1)

grid1 = Grid(10,10)
algorithms.A_star.a_star(grid1.grid, 3, 5, 9, 9)
grid1.print_grid()