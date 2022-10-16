
def compose(notes, moves, start):
    song=[]
    song.append(notes[start])
    for i in range(0, len(moves)):

        if start + moves[i] > len(notes)-1:
            song.append(notes[(start + moves[i]) % len(notes)])

        else: song.append(notes[start + moves[i]] ) 

        start = start + moves[i]   
    return song


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2, -4, -7], 2))