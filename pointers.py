num1 = 11               #num1 stores 11 in the memory somewhere
num2 = num1

print("Before num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("\n num1 points to:" , id(num1))          #140710536995944
print("num2 points to: ", id(num2))             #140710536995944

num2 = 22

print("After num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("\n num1 points to:" , id(num1))         #140710536995944 
print("num2 points to: ", id(num2))            #140710536996296



dict1 = {
    'value': 11
}

dict2 = dict1

print("Before dict2 value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\n dict1 points to:" , id(dict1))       #2059060855104  
print("dict2 points to: ", id(dict2))          #2059060855104

dict2['value'] = 22

print("After dict2 value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\n dict1 points to:" , id(dict1))       #2252635521344  
print("dict2 points to: ", id(dict2))          #2252635521344
