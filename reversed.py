numbers=[]
for i in range(10):
      numb=int(input("enter the given number: "))
      numbers.append(numb)

reversed_list=[]

for num in numbers:
     reversed_list.insert(0,num)

          

print("Orginal List: ", numbers)
print("Reversed List: ", reversed_list)
