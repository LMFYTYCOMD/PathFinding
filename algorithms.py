import math
import heapq
from collections import deque

class Heuristic:
    def Manhattan(start, target):
        x_distance = abs(start.coordinate[0] - target.coordinate[0])
        y_distance = abs(start.coordinate[1] - target.coordinate[1])
        return x_distance + y_distance

    def Euclidean(start, target):
        x_distance = abs(start.coordinate[0] - target.coordinate[0])**2
        y_distance = abs(start.coordinate[1] - target.coordinate[1])**2
        return math.sqrt(x_distance + y_distance)

class A_star:
    def a_star(grid, start_x, start_y, target_x, target_y):
        start = grid[start_y][start_x]
        target = grid[target_y][target_x]

        count = 0
        distance_to_others = {}

        path = {} #keep track of 
        
        for row in grid:
            for node in row:
                distance_to_others[node] = math.inf

        distance_to_others[start] = 0
        nodes_to_explore = [(0, start)]

        while nodes_to_explore and distance_to_others[target] == math.inf:
            current_distance, current_node = heapq.heappop(nodes_to_explore)

            #prevent index error
            neighboring_nodes = []
            x, y = current_node.coordinate
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    node = grid[ny][nx]
                    neighboring_nodes.append(node)

            for neighbor in neighboring_nodes:
                new_distance = current_distance + Heuristic.Manhattan(start, neighbor) + Heuristic.Manhattan(neighbor, target)

                if new_distance < distance_to_others[neighbor]:
                    distance_to_others[neighbor] = new_distance
                    current_node.face_val = 1
                    neighbor.face_val = 2 #uncomment to see border made up of unvisited neighbors

                    path[neighbor] = current_node #Each key-value pair represents a node in the grid and its previous node on the shortest path to that node.

                    heapq.heappush(nodes_to_explore, (new_distance, neighbor))
                    count += 1

        # construct shortest path
        shortest_path = []
        current_node = target
        while current_node in path:
            shortest_path.append(current_node)
            current_node = path[current_node] #access previous node of current_node. Current_node was the neighbor node of this node.
        shortest_path.append(start)

        for node in shortest_path:
            node.face_val = 'p'
        
        print(f'A* found Path distance of {len(shortest_path)} after exploring {count} nodes')

class Dijkstra:
    def dijkstra(grid, start_x, start_y, target_x, target_y):
        start = grid[start_y][start_x]
        target = grid[target_y][target_x]

        count = 0
        distance_to_others = {}

        path = {}

        for row in grid:
            for node in row:
                distance_to_others[node] = math.inf

        distance_to_others[start] = 0
        nodes_to_explore = [(0, start)]

        while nodes_to_explore:
            current_distance, current_node = heapq.heappop(nodes_to_explore)

            neighboring_nodes = []
            x, y = current_node.coordinate
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    node = grid[ny][nx]
                    neighboring_nodes.append(node)
            
            for neighbor in neighboring_nodes:
                new_distance = current_distance + Heuristic.Manhattan(start, neighbor)

                if new_distance < distance_to_others[neighbor]:
                    distance_to_others[neighbor] = new_distance
                    current_node.face_val = 1 #change face_val from 2 to 1
                    neighbor.face_val = 2

                    path[neighbor] = current_node

                    heapq.heappush(nodes_to_explore, (new_distance, neighbor))
                    count += 1

        shortest_path = []
        current_node = target
        while current_node in path:
            shortest_path.append(current_node)
            current_node = path[current_node]
        shortest_path.append(start)

        for node in shortest_path:
            node.face_val = 'p'
            
        print(f'Dijkstra found Path distance of {len(shortest_path)} after exploring {count} nodes')

class DFS:
    def depth_first(grid, start_x, start_y, target_x, target_y):
        start = grid[start_y][start_x]
        target = grid[target_y][target_x]

        nodes_path_to_visit = deque()
        initial_path = [start]
        nodes_path_to_visit.append(initial_path)

        count = 0
        visited_nodes = set()           

        while nodes_path_to_visit:

            current_path = nodes_path_to_visit.pop() #path of object nodes
            current_node = current_path[-1] #dfs -> get the last one

            if current_node not in visited_nodes:
                visited_nodes.add(current_node)

                visited_nodes.add(current_node)
                current_node.face_val = 1
                count += 1

                if current_node.coordinate == target.coordinate:
                    break

                neighboring_nodes = []
                x, y = current_node.coordinate
                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                        node = grid[ny][nx]
                        neighboring_nodes.append(node)
                
                for neighbor in neighboring_nodes:
                    neighbor.face_val = 2
                    new_path = current_path[:] #copy the current path
                    new_path.append(neighbor) #append the neighbor that is not in visited_nodes
                    nodes_path_to_visit.append(new_path)

        for node in current_path:
            node.face_val = 'p'
        
        print(f'DFS found Path distance of {len(current_path)} after exploring {count} nodes')
                                    
class BFS:
    def breath_first(grid, start_x, start_y, target_x, target_y):
        start = grid[start_y][start_x]
        target = grid[target_y][target_x]

        nodes_path_to_visit = deque()
        initial_path = [start]
        nodes_path_to_visit.appendleft(initial_path)

        count = 0
        visited_nodes = set()                 

        while nodes_path_to_visit:

            current_path = nodes_path_to_visit.pop() #path of object nodes
            current_node = current_path[-1] #dfs -> get the last one

            if current_node not in visited_nodes:
                visited_nodes.add(current_node)

                current_node.face_val = 1
                count += 1

                if current_node.coordinate == target.coordinate:
                    break

                neighboring_nodes = []
                x, y = current_node.coordinate
                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                        node = grid[ny][nx]
                        neighboring_nodes.append(node)

                for neighbor in neighboring_nodes:
                    neighbor.face_val = 2
                    new_path = current_path[:] #copy the current path
                    new_path.append(neighbor) #append the neighbor that is not in visited_nodes
                    nodes_path_to_visit.appendleft(new_path)

        for node in current_path:
            node.face_val = 'p'
        
        print(f'BFS found Path distance of {len(current_path)} after exploring {count} nodes')
























        #add new feature: allow users to add obstacles