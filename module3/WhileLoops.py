squares = ["orange", "orange", "purple"]

newSquares = []
i = 0

while(squares[i]=="orange"):
    newSquares.append(squares[i])
    i += 1

for square in newSquares:
    print(square)