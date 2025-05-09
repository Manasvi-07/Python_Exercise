numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3] 

print("Choose an option")
print("A, length of the list")
print("B, Display first 3 number")
print("C, Display sum of odd number")
print("D, Display number of duplicate number")
print("E, Display list without duplicate number")

choice = input("Enter your choice (A/B/C/D/E): ").upper()

if choice == "A":
    print("numbers of length : ", len(numbers))
elif choice == "B":
    print("First 3 number : ", numbers[:3])
elif choice == "C":
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    print("Sum of odd number : ", odd_sum)
elif choice == "D":
    duplicate = set([i for i in numbers if numbers.count(i)> 1])
    print("Print Duplicate number : ", duplicate)
    print("Print duplicate number length : ", len(duplicate))
elif choice == "E":
    unique = set([i for i in numbers if numbers.count(i) >= 1])
    unique_num = []
    for num in numbers:
        if num not in unique_num:
            unique_num.append(num)
    print("Display unique number : ", unique)
    print("Display unique number : ", unique_num)
