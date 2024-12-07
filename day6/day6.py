with open("day6/input.txt") as f:
    grid = [list(line.strip()) for line in f]

directions = [(-1, 0),(0, 1),(1, 0),(0, -1)]

directions_idx = 0
visited = set()

for r,row in enumerate(grid):
    for c,col in enumerate(row):
        if col == "^":  
            guard_pos = (r, c) #guard starting position

rows, cols = len(grid), len(grid[0])
visited.add(guard_pos)

while True:
    dx, dy = directions[directions_idx]
    next_x = guard_pos[0] + dx
    next_y = guard_pos[1] + dy

    #Check if guard left the grid
    if next_x < 0 or next_x >= rows or next_y < 0 or next_y >= cols:
        break

    if grid[next_x][next_y] == '#':
        directions_idx = (directions_idx + 1) % 4
    else:
        guard_pos = (next_x,next_y)
        visited.add(guard_pos)

print(len(visited))

#and part B is just brute force :D