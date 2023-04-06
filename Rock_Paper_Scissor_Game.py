#Rock: R; Paper: P; Scissor: S
p1 = 0
p2 = 0
# Accept moves for 5 rounds of the game
for i in range(0, 5):
    print("Round: ", i+1)
    x = input("Player 1: Enter the move: ")
    y = input("Player 2: Enter the move: ")
    print("\n")

# TIES
    if(x == 'R' and y == 'R'):
        i = i-1
    elif(x == 'S' and y == 'S'):
        i = i-1
    elif(x == 'P' and y == 'P'):
        i = i-1
# WINS
    if(x == 'R' and y == 'S'):
        p1 += 1
    elif(x == 'R' and y == 'P'):
        p2 += 1
    elif(x == 'P' and y == 'S'):
        p2 += 1
    elif(x == 'P' and y == 'R'):
        p1 += 1
    elif(x == 'S' and y == 'P'):
        p1 += 1
    elif(x == 'S' and y == 'R'):
        p2 += 1
print("Final Score:\nPlayer 1: ",p1,"\nPlayer 2: ",p2)
# Winner Player Display
if(p1 > p2):
    print("Player 1 won")
elif(p2 > p1):
    print("Player 2 won")