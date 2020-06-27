def bidirectional(tuples):
    bidirectional_dict = {}
    for (orbited, orbiter) in coupled_data:
        if orbiter not in bidirectional_dict.keys():
            this_value = []
            this_value.append(orbited)
            bidirectional_dict[orbiter] = this_value
        elif orbiter in bidirectional_dict.keys():
            bidirectional_dict[orbiter].append(orbited)
        if orbited not in bidirectional_dict.keys():
            this_value = []
            this_value.append(orbiter)
            bidirectional_dict[orbited] = this_value
        elif orbited in bidirectional_dict.keys():
            bidirectional_dict[orbited].append(orbiter)
    return bidirectional_dict



def find_next_node(candidates):
    filtered_dict = {}
    for key, value in candidates.items():
        if not value['visited'] and value['distance'] != -1:
            filtered_dict[key] = value
    shortest = None
    if len(filtered_dict) == 0:
        return None
    for key, value in filtered_dict.items():
        if shortest == None:
            shortest = (key, value)
        elif value['distance'] < shortest[1]['distance']:
            shortest = (key, value)
    return shortest[0]


def search_dict(bidirectional_graph, origin, destination):
    outer_dict = {}
    for k in bidirectional_graph.keys():
        outer_dict[k] = {
            'visited' : False, 'distance' : -1
        }

    outer_dict[origin]['distance'] = 0

    current_node = origin
    
    while True:
        for neighbour_value in bidirectional_graph[current_node]:
            distance = outer_dict[current_node]['distance'] + 1
            if outer_dict[neighbour_value]['distance'] == -1:
                outer_dict[neighbour_value]['distance'] = distance
            elif distance < outer_dict[neighbour_value]['distance']:
                outer_dict[neighbour_value]['distance'] = distance
        
        outer_dict[current_node]['visited'] = True
        next_node = find_next_node(outer_dict)
        if next_node is None:
            break
        else: 
            current_node = next_node

    return outer_dict[destination]['distance']   


def count_paths(node, graph):
    total = 0
    to_visit = [node]
    while len(to_visit):
        node_to_process = to_visit.pop()
        neighbours = graph.get(node_to_process)
        if neighbours is not None:
            neighbour_count = len(neighbours)
            total += neighbour_count
            to_visit.extend(neighbours)
    return total

with open("advent_of_code_day_six_textfile.txt") as f:    
    map_data = f.read().splitlines()

coupled_data = []
for i in map_data:
    couple = tuple(i.split(")"))
    coupled_data.append(couple)

bidirectional_dict = bidirectional(coupled_data)
answer = search_dict(bidirectional_dict, 'SAN', 'YOU') - 2


map_dict = {}
for i in coupled_data:
    if i[1] not in map_dict.keys():
        this_value = []
        this_value.append(i[0])
        map_dict[i[1]] = this_value
    elif i[1] in map_dict.keys():
        map_dict[i[1]].append(i[0])

all_keys = map_dict.keys()
grand_total = 0
for key in all_keys:
    grand_total += count_paths(key, map_dict)

print(grand_total)





