with open("day4/input.txt", 'r') as file:
    grid = [line.strip() for line in file]

#tuples that indicate precious, current or next row/column
directions = []
for i in [-1,0,1]:
    for j in [-1,0,1]:
        directions.append(tuple([i,j]))

word="XMAS"
ans = 0

#this algorithm would work for any word, not just XMAS (this is not true for part B)
for row in range(len(grid)):
    for col in range(len(grid[0])):
        for inc_row, inc_col in directions:
            found = True
            for i in range(len(word)):
                r, c = row + i * inc_row, col + i * inc_col
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != word[i]: 
                #exclude the bounds, and check if current letter matches the target word's equivalent
                    found = False
                    break
            if found:
                ans += 1

print(ans)