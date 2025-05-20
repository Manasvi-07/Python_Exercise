numbers = [2,5,6,1,3,8,9,10]
n = len(numbers)
for i in range(n-1):
    for j in range(n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)


# --------------------------------

for i in range(n-1):
    min_Index = i 
    for j in range(i+1, n):
        if numbers[j] < numbers[min_Index]:
            min_Index = j 
        numbers[i],numbers[min_Index]= numbers[min_Index], numbers[i]

print(numbers)

