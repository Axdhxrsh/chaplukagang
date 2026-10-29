numbers=[]
for i in range(10):
    num=int(input("Enter the numbers: "))
    numbers.append(num)

unique=[]

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates",unique)
