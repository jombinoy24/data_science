print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
matOne = []
print("Enter Elements for First Matrix:")
for i in range(3):
    matOne.append([])
    for j in range(3):
        num = int(input())
        matOne[i].append(num)

matTwo = []
print("Enter Elements for Second Matrix:")
for i in range(3):
    matTwo.append([])
    for j in range(3):
        num = int(input())
        matTwo[i].append(num)

matThree = []
for i in range(3):
    matThree.append([])
    for j in range(3):
        matThree[i].append(matOne[i][j] + matTwo[i][j])

print("\nAddition Result of Two Given Matrices is:")
for i in range(3):
    for j in range(3):
        print(matThree[i][j], end=" ")
    print()
