def print_items(n):
	for i in range(n):#Runs this line n times so O(n)
		for j in range(n):  	#Runs this line n times so O(n)
			print(i, j)
			   
print_items(10)             		#Together it runs O(n * n) = O(n^2)


#O(n^2 + n) = O(n^2) as we drop non dominants
def print_items2(n):
	for i in range(n):          #Runs this line n times so O(n)
		for j in range(n):      #Runs this line n times so O(n)
			print(i, j)
	for k in range(n):          #Runs this line n times so O(n)
		print(k)

print_items2(10)                #Together this line runs O(n^2 + n) times 

#We drop non dominants so O(n^2 + n) = O(n^2)