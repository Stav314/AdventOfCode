from collections import defaultdict

def is_valid_update(update, graph):
    positions = {page: i for i, page in enumerate(update)}
    for x in update:
        for y in graph.get(x, []):
            if y in positions and positions[x] > positions[y]:
                return False
    return True

def sort_update(update, graph):
    sorted=update
    positions = {page: i for i, page in enumerate(update)}
    for x in update:
        for y in graph.get(x, []):
            if y in positions and positions[x] > positions[y]:
               sorted.pop(sorted.index(x))
               sorted.insert(sorted.index(y),x)
    return sorted

with open('day5/input.txt', 'r') as file:
    content = file.read().strip()
rules_section, updates_section = content.split("\n\n")
rules = rules_section.splitlines()
updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]

#dictionary of a page and those that preceed it
graph = defaultdict(set)
for rule in rules:
    x, y = map(int, rule.split('|'))
    graph[x].add(y)

middle_values = 0
middle_values2= 0
for update in updates:
    if is_valid_update(update, graph):
        middle_values+=update[len(update)//2]
    else:
        update=sort_update(update,graph)
        middle_values2+=update[len(update)//2]


print(middle_values)
print(middle_values2)
