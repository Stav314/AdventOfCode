with open("day4/input.txt", 'r') as file:
    grid = [line.strip() for line in file]

ans2 = 0

#First, we will locate the center A, then check the letter around it for the MAS cross pattern

 #exclude the edges since we're looking for the centers
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        if grid[y][x] == 'A':  

            #All diagonals
            top_left = grid[y-1][x-1]
            top_right = grid[y-1][x+1]
            bottom_left = grid[y+1][x-1]
            bottom_right = grid[y+1][x+1]
            
            # Check for ALL DIAGONALS
            if ((top_left == 'M' and bottom_right == 'S' and top_right == 'S' and bottom_left == 'M') or
                (top_left == 'S' and bottom_right == 'M' and top_right == 'M' and bottom_left == 'S') or
                (top_left == 'S' and bottom_right == 'M' and top_right == 'S' and bottom_left == 'M') or
                (top_left == 'M' and bottom_right == 'S' and top_right == 'M' and bottom_left == 'S')):
                
                ans2 += 1

print(ans2)
