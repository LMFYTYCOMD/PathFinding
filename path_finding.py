import grid_structure, algorithms

class PathFinding:

    def informative():
        print('\nDenotation: ')
        print('0: node that has not been explored nor added to neighbors')
        print('1: node that has been explored')
        print('2: neighboring node that was added to neighbors but never explored')
        print('O: obstacles')

    def create_grid():
        print('Creating grid...\n')
        x = input('Enter the number of column: ')
        while not x.isnumeric():
            x = input('Enter number only: ')

        y = input('Enter the number of row: ')
        while not y.isnumeric():
            y = input('Enter number only: ')

        return int(x), int(y)

    def start_coordinate():
        print('\nChoose starting point: ')
        x = input('Enter x of start: ')
        while not x.isnumeric(): #when return if x y is out of range prompt user and call this function again
            x = input('Enter number only: ')

        y = input('Enter y of start: ')
        while not y.isnumeric():
            y = input('Enter number only: ')

        return int(x), int(y)

    def target_coordinate():
        print('\nChoose target: ')
        x = input('Enter x of target: ')
        while not x.isnumeric(): #when return if x y is out of range prompt user and call this function again
            x = input('Enter number only: ')

        y = input('Enter y of target: ')
        while not y.isnumeric():
            y = input('Enter number only: ')

        return int(x), int(y)

    def pathfinding_type():
        print('\nThere 4 types of pathfinding algorithms: DFS, BFS, Dijkstra and A*. You can choose up to 4')

        dfs = input('Do you want to use DFS? (y/n): ')
        while dfs != 'y' and dfs != 'n': # if or, then if dfs = y, dfs is != n, the condition is true and the loop goes on
            dfs = input('Enter (y/n) only: ')

        bfs = input('Do you want to use BFS? (y/n): ')
        while bfs != 'y' and bfs != 'n':
            bfs = input('Enter (y/n) only: ')

        dijkstra = input('Do you want to use Dijkstra? (y/n): ')
        while dijkstra != 'y' and dijkstra != 'n':
            dijkstra = input('Enter (y/n) only: ')

        a_star = input('Do you want to use A*? (y/n): ')
        while a_star != 'y' and a_star != 'n':
            a_star = input('Enter (y/n) only: ')

        return [dfs + '0', bfs + '1', dijkstra + '2', a_star + '3'] #iterate through this list. If index and y -> run algo

    def start():
        x_col, y_row = PathFinding.create_grid()
        grid_object = grid_structure.Grid(x_col, y_row)
     
        while True:
            try:
                obs_percentage = int(input('\nInput the amount of obstacles you want (in percentage, between 0 and 100): '))
                assert 0 <= obs_percentage <= 100
            except ValueError:
                print('Invalid input. Enter numeric value only')
            except AssertionError:
                print('Invalid input. Enter number between 0 and 100')
            else:
                break
            
        grid_object.set_obs(obs_percentage)
        grid = grid_object.grid

        x_start, y_start = PathFinding.start_coordinate()
        while not (0 <= x_start < x_col and 0 <= y_start < y_row):
            print('Coordinate out of range. Choose again.')
            x_start, y_start = PathFinding.start_coordinate()

        x_target, y_target = PathFinding.target_coordinate()
        while not (0 <= x_target < x_col and 0 <= y_target < y_row):
            print('Coordinate out of range. Choose again.')
            x_target, y_target = PathFinding.target_coordinate()

        pathfinding_choice = PathFinding.pathfinding_type()
        PathFinding.informative()

        for choice in pathfinding_choice:
            
            if choice == 'y0' and pathfinding_choice.index(choice) == 0:
                print('\n')
                grid_object.reset_grid_value()
                grid[y_start][x_start].reset()
                grid[y_target][x_target].reset()
                algorithms.DFS.depth_first(grid, x_start, y_start, x_target, y_target)
                grid_object.print_grid()

            elif choice == 'y1' and pathfinding_choice.index(choice) == 1:
                print('\n')
                grid_object.reset_grid_value()
                grid[y_start][x_start].reset()
                grid[y_target][x_target].reset()
                algorithms.BFS.breath_first(grid, x_start, y_start, x_target, y_target)
                grid_object.print_grid()

            elif choice == 'y2' and pathfinding_choice.index(choice) == 2:
                print('\n')
                grid_object.reset_grid_value()
                grid[y_start][x_start].reset()
                grid[y_target][x_target].reset()

                algorithms.Dijkstra.dijkstra(grid, x_start, y_start, x_target, y_target)
                grid_object.print_grid()

            elif choice == 'y3' and pathfinding_choice.index(choice) == 3:
                print('\n')
                grid_object.reset_grid_value()
                grid[y_start][x_start].reset()
                grid[y_target][x_target].reset()

                algorithms.A_star.a_star(grid, x_start, y_start, x_target, y_target)
                grid_object.print_grid()

PathFinding.start()