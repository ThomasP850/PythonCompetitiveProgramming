DESTINATION = 'C:/where/is/my/water/'

class FileSystem():
    def __init__(self):
        self.graph = {}
    
    def add_file(self, absolute_path):
        directories = self.__extract_directories(absolute_path)
        # If there is a shortcut...
        if '[' in directories[-1]:
            self.__add_connection(self.__build_path(directories[:-1]), directories[-1][1:-1])
            directories.pop()  # remove shortcut so we dont bind it to other things
        # Add normal file structure connections
        for i in range(1, len(directories)):
            self.__add_connection(self.__build_path(directories[:i]), self.__build_path(directories[:i+1]))
            
    
    def __add_connection(self, name1, name2):
        """
        Add a connection between two folders.
        
        Parameters:
            name1 (str): absolute path of first directory to connect
            name2 (str): absolute path of second directory to connect
        """
        if name1 not in self.graph:
            self.graph[name1] = set()
        if name2 not in self.graph:
            self.graph[name2] = set()
        
        self.graph[name1].add(name2)
        self.graph[name2].add(name1)
    
    def clicks_to_destination(self, start, directories_visited=[]):
        """
        Get the minimum number of clicks to get from start folder to DESTINATION
        Parameters:
            start (str): the path to start at
            directories_visited (str[]): paths of directories that have already been visited
        Returns:
            the minimum number of clicks to get from start to DESTINATION
            -1 if DESTINATION is not reached
        """
        if start in directories_visited:
            return -1
        elif start == DESTINATION:
            return 0
        
        new_directories = directories_visited + [start]
        possible_clicks = list(filter(lambda n: n>=0, [self.clicks_to_destination(d, new_directories) for d in self.graph[start]]))
        if len(possible_clicks) == 0:
            return -1
        else:
            return 1 + min(possible_clicks)

    def __extract_directories(self, raw):
        """
        Extract the directory names from a string
        
        Parameters:
            raw (str): The path as a string. ex: 'C:/this/is/a/path'
        
        Returns:
            (str[]): A list of directory names in order. ex: ['C:', 'this', 'is', 'a', 'path']
        """
        if '[' in raw:
            return list(filter(len, raw[:raw.index('[')].split('/'))) + [raw[raw.index('['):]]
        else:
            return list(filter(len, raw.split('/')))
    
    def __build_path(self, dir_names):
        """
        Build an absolute path using directory names
        
        Parameters:
            dir_names (str[]): names of directories. ex: ['C:', 'a', 'b', 'c']
        Returns:
            (str): the absolute path. ex: 'C:/a/b/c'
        """
        return '/'.join(dir_names) + '/'
        

file_system = FileSystem()
n = int(input())
for i in range(n):
    file_system.add_file(input())
results = []
c = int(input())
for case in range(1, c+1):
    results.append(f'Case {case}: {file_system.clicks_to_destination(input())}')

print('\n'.join(results))