class Line:
    def __init__(self):
        self.current_x = 0
        self.current_y = 0
        self.visited = []
        self.travelled = 0
        self.distances = {}

    def moves_up(self, n):
        for i in range(n):
            self.current_y += 1
            self.visited.append((self.current_x, self.current_y))
            self.travelled += 1
            if not (self.current_x, self.current_y) in self.distances:
                self.distances[(self.current_x, self.current_y)] = self.travelled
    def moves_down(self, n):
        for i in range(n):
            self.current_y -= 1
            self.visited.append((self.current_x, self.current_y))
            self.travelled += 1
            if not (self.current_x, self.current_y) in self.distances:
                self.distances[(self.current_x, self.current_y)] = self.travelled
    def moves_right(self, n):
        for i in range(n):
            self.current_x += 1
            self.visited.append((self.current_x, self.current_y))
            self.travelled += 1
            if not (self.current_x, self.current_y) in self.distances:
                self.distances[(self.current_x, self.current_y)] = self.travelled
    def moves_left(self, n):
        for i in range(n):
            self.current_x -= 1
            self.visited.append((self.current_x, self.current_y))
            self.travelled += 1
            if not (self.current_x, self.current_y) in self.distances:
                self.distances[(self.current_x, self.current_y)] = self.travelled
    def visited_set(self):
        return set(self.visited)
    
    
    
with open("advent_of_code_puzzle_file_day_three.txt") as instructions:
    lines = instructions.read().splitlines()
    first_line_input = lines[0].split(',')
    second_line_input = lines[1].split(',')

# (type(first_line_input))

first_line = Line()
second_line = Line()


for i in first_line_input:
    letter = i[0]
    number = int(i[1:])
    if letter == 'U':
        first_line.moves_up(number)
    elif letter == 'D':
        first_line.moves_down(number)
    elif letter == 'R':
        first_line.moves_right(number)
    elif letter == 'L':
        first_line.moves_left(number)
    else:
        print(f"Whoops, that's a {letter}")


for i in second_line_input:
    letter = i[0]
    number = int(i[1:])
    if letter == 'U':
        second_line.moves_up(number)
    elif letter == 'D':
        second_line.moves_down(number)
    elif letter == 'R':
        second_line.moves_right(number)
    elif letter == 'L':
        second_line.moves_left(number)
    else:
        print(f"Whoops, that's a {letter}")

first_set = first_line.visited_set()
second_set = second_line.visited_set()
intersection = first_set & second_set

def manhattan_distance(tupe):
    (x, y) = tupe
    distance = abs(x) + abs(y)
    return distance

smallest = (99999, 99999)
for i in intersection:
    if manhattan_distance(i) < manhattan_distance(smallest):
        smallest = i
print(manhattan_distance(smallest))   

shortest = 99999
for i in intersection:
    path_length = first_line.distances[i] + second_line.distances[i]
    if path_length < shortest:
        shortest = path_length
print(shortest)

