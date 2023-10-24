import numpy as np

#import and load all building names and coordinates
building_names = []
coordinates = []
f = open('map.msstate.csv', 'r')
for l in f:
    name, x, y = l.split(',')
    building_names.append(name)
    coordinates.append([float(x), float(y)])
f.close()
coordinates = np.array(coordinates)
print('Loaded coordinates from', len(coordinates), 'buildings')

#gets the distance between buildings from the current building
def get_neighbors(current_idx, visited, distance_threshold=200):
    neighbors = []
    distances = np.sqrt(np.sum((coordinates - coordinates[current_idx])**2, axis=1))
    for i in range(len(coordinates)):
        if i != current_idx and not i in visited and distances[i] < distance_threshold:
            neighbors.append(i)
    return neighbors

class SearchNode:
    def __init__(self, idx, parent):
        self.idx = idx
        self.parent = parent

def bfs(start, goal):
        start_idx = building_names.index(start)
        goal_idx = building_names.index(goal)
        print('start_idx ', start_idx, 'goal_idx ', goal_idx)
        visited = set()

        Q = [SearchNode(start_idx, None)]
        visited.add(start_idx)

        while not (len(Q) == 0):
            current_node = Q.pop(0)
            if current_node.idx == goal_idx:
                print('Found goal:', current_node.idx)
                path = []
                while current_node is not None:
                    path.append(building_names[current_node.idx])
                    current_node = current_node.parent
                path.reverse()
                return path
            
            for n in get_neighbors(current_node.idx, visited):
                visited.add(n)
                Q.append(SearchNode(n, current_node))

        return None
    
print(bfs('Rice Hall', 'Allen Hall'))
print(bfs('Rice Hall', 'Butler Hall'))
print(bfs('Hathorn Hall', 'Middleton Hall (ROTC Building)'))
print(bfs('Rice Hall', 'George Hall'))
print(bfs('Magnolia Hall', 'Nusz Park'))