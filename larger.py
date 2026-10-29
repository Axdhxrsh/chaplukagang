numbers=[15,17,20,35,35,600,76,4,3678]

largest=numbers[0]
smallest=numbers[0]

for num in numbers:
    if num >largest:
       largest=num

    if num < smallest:
       smallest=num

print("largest element: ",largest)
print("Smallest element: ",smallest)
