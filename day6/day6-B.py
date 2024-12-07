import time
start_time = time.time() #this thing takes way too long to run

with open("day6/input.txt") as f:
    grid = [list(line.strip()) for line in f]


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == "^":
            guard_pos = (r, c)
            break
    if guard_pos:
        break

loops = 0

# Try placing an obstruction at every empty space
# this would be much more efficient if I followed the "visited" positions from part A
# it works, though
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '.': 

            new_grid = [row[:] for row in grid]
            new_grid[r][c] = '#'

            new_visited = set()
            directions_idx = 0
            g_x, g_y = guard_pos
            new_visited.add((g_x, g_y, directions_idx))

            while True:
                dir_x, dir_y = directions[directions_idx]
                next_x, next_y = g_x + dir_x, g_y + dir_y

                if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                    break

                if new_grid[next_x][next_y] == '#':
                    directions_idx = (directions_idx + 1) % 4
                else:
                    g_x, g_y = next_x, next_y
                    if (g_x, g_y, directions_idx) in new_visited:
                        loops += 1  # Loop detected
                        break
                    new_visited.add((g_x, g_y, directions_idx))


print(loops)
print("Process finished --- %s seconds ---" % (time.time() - start_time))