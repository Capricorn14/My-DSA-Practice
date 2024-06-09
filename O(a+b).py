def print_items(a, b):
    for i in range(a): #Runs this line a times so O(a)
        print(i)
    for j in range(b):  #Runs this line b times so O(b)
        print(j)

print_items(3, 4)       #So this line runs O(a+b) times