from collections import defaultdict, deque

def is_valid_update(update, graph):
    positions = {page: i for i, page in enumerate(update)}
    for x in update:
        for y in graph.get(x, []):
            if y in positions and positions[x] > positions[y]:
                return False
    return True

def sort_update(update, graph):
    # number of incoming edges and local graph for the update
    preceeding = defaultdict(int)  #how many pages preceeding it
    local_graph = defaultdict(set) #for the current update being

    for page in update:
        # check its neighbors 
        for neighbor in graph.get(page, []):

            # Increment the neighbors of a page
            if neighbor in update:
                local_graph[page].add(neighbor)
                preceeding[neighbor] += 1
        
        preceeding.setdefault(page, 0)

    # Initialize the queue with all pages that have no others before them
    queue = deque([page for page in update if preceeding[page] == 0])
    sorted_update = []  # This will store the pages in topologically sorted order

    # topological sorting
    while queue:
        node = queue.popleft()
        sorted_update.append(node)  # Add it to the sorted result

        for neighbor in local_graph[node]:
            # Reduce the number of neighbours after resolving
            preceeding[neighbor] -= 1
            # If no more neighbours then it's sorted in place
            if preceeding[neighbor] == 0:
                queue.append(neighbor)
    return sorted_update 



with open('day5/input.txt', 'r') as file:
    content = file.read().strip()
rules_section, updates_section = content.split("\n\n")
rules = rules_section.splitlines()
updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]

graph = defaultdict(set)
for rule in rules:
    x, y = map(int, rule.split('|'))
    graph[x].add(y)

middle_values = 0
middle_values2 = 0

for update in updates:
    if is_valid_update(update, graph):  
        middle_values += update[len(update) // 2]
    else:  
        sorted_update = sort_update(update, graph)
        middle_values2 += sorted_update[len(sorted_update) // 2]

print("Part A:", middle_values)
print("Part B:", middle_values2)
