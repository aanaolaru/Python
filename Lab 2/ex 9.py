# Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium 
# and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game.
# A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied.
# All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.

def spectators(heights: list):
    res = []
    for col in range(0, len(heights[0])):
        max_height = heights[0][col]
        for row in range(1, len(heights)):
            if heights[row][col] <= max_height:
                res.append((row, col))
            else:
                max_height = heights[row][col]
    return res

print(spectators([[1, 2, 3, 2, 1, 1],
                   [2, 4, 4, 3, 7, 2],
                   [5, 5, 2, 5, 6, 4],
                   [6, 6, 7, 6, 7, 5]]))