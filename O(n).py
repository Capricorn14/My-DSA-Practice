#O(n)
def print_items(n):
    for i in range(n):   # Prints a number n times... so basically this line runs n times. Thus it is O(n)
        print(i)

print_items(10)

#O(2n) = O(n)
def print_items2(n):
    for i in range(n):  #Runs this line 10 times so O(n)
        print(i)
    
    for j in range(n):  #Runs this line 10 times too so O(n) again
        print(j)
    
print_items2(10)        #In all, this will be O(n+n) = O(2n) but we drop constants so this will be O(n)