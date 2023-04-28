class Node:
    def __init__(self, index, bomb_time=-1):
        """
        Create a new node
        
        Parameters:
            index (int): the index of this node
            bomb_time: the time that the bomb at this node will go off,
                       this will be -1 if there is no bomb
        """
        self.index = index
        self.bomb_time = bomb_time
    
    def get_index(self):
        return self.index
    
    def get_bomb_time(self):
        return self.bomb_time
        
    def set_bomb_time(self, new_time):
        self.bomb_time = new_time
        
    def __hash__(self):
        return hash((self.index, self.bomb_time))
    
    def __eq__(self, other):
        return self.index == other.get_index() and self.bomb_time == other.get_bomb_time()
    
    def __repr__(self):
        if self.bomb_time > -1:
            return f'Node[{self.index}, Bomb:{self.bomb_time}]'
        else:
            return f'Node[{self.index}]'

class Sewer:
    def __init__(self):
        self.graph = {}
    
    def add_path(self, node1, node2, time):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append((node2, time))
        self.graph[node2].append((node1, time))
        
    def print_graph(self):
        for key, value in self.graph.items():
            print(str(key) + ': ')
            for val in value:
                print('     ' + str(val))
        
    def __get_all_paths_to_node(self, from_node, to_node, nodes_visited=[], time=0):
        """
        Get all of the possible paths from from_node to to_node
        
        Parameters:
            from_node (Node): the node to start at
            to_node (Node): the node to end at
            nodes_visited (int[]): node indexes that have been visited and cannot be used again
            time (int): the total time of this path so far
        
        Returns:
            ((int, Node[])[]): The list of possible paths
        """
        nodes_visited.append(from_node.get_index())
        if from_node == to_node:
            return [(time, nodes_visited)]
        def evaluate_path(path):
            if path[0].get_index() in nodes_visited:
                return False
            elif -1<path[0].get_bomb_time()<=time+path[1]:
                return False
            return True
        available_paths = filter(evaluate_path, self.graph[from_node])
        paths = []
        for path in available_paths:
            paths += self.__get_all_paths_to_node(path[0], to_node, nodes_visited, time+path[1])
        return paths
    
    def find_shortest_time(self, from_node, to_node):
        paths = self.__get_all_paths_to_node(from_node, to_node)
        return min(map(lambda t: t[0], paths))

results = []
c = int(input())
for case in range(1,c+1):
    num_nodes = int(input())+1
    num_pipes, num_bombs = map(int, input().split())
    nodes = [Node(i) for i in range(num_nodes)]
    sewer = Sewer()
    for i in range(num_pipes):
        index_one, index_two, time = map(int, input().split())
        sewer.add_path(nodes[index_one], nodes[index_two], time)
    for i in range(num_bombs):
        index, time = map(int, input().split())
        nodes[index].set_bomb_time(time)
    results.append(f'Batman can reach the gold in time {sewer.find_shortest_time(nodes[0], nodes[-1])}.')
print('\n'.join(results))