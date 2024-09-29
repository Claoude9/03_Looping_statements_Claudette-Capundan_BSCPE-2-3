size = int(input("Enter the size of the array: "))

elements = input("Enter the elements separated by space: ").split()

for i in range(size):
    elements[i] = int(elements[i])

print("\nCube of each elements:")
for element in elements:
    cube = element ** 3  
    print(cube)
