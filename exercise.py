
#  1st Question ----

# num = int(input("Enter Num : "))

# if num % 5 == 0 and num % 7 == 0 and num % 10 == 0 and num % 56 == 0:
#     print(f"{num} is multiple number 5, 7, 10 and 56")
# else :
#     print(f"{num} is not multiple number 5, 7, 10, and 56")



# 2nd Question ----- 

# def factorial(n):
#     if n == 1:
#         return 1
#     else :
#         return (n*factorial(n-1))

# num = int(input("Enter num : "))
# print(factorial(num))


# 3rd Question ---

# matrix = [[1,2,3,4],
#           [5,6,7,8],
#           [9,10,11,12]]

# mat = [[row[i] for row in matrix]
#        for i in range(len(matrix[0]))]
# print(mat)

# 4th Question ----

# num = [1,2,3,4,5]

# ans = [i * 2 for i in num if i % 2 == 0]
# print(ans)

# ans1 = list(map(lambda x : x * 2, filter(lambda x : x % 2 == 0, num)))
# print(ans1)

# 5th Question ----

# num = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

# ans = []
# for n in num:
#        if n == n:
#               ans.append(n)

# print(ans)


# 6th Question ----

# num = [[1,2,3],[4,5,6],[7,8,9]]

# ans = []
# n = 0
# for i in num:
#        for n in i:
#               ans.append(n)
# print(ans)

# 7th Question 

# num = [[8, 14, -6],
#        [12,7,4],
#        [-11,3,21]]

row = int(input("enter num of row : "))
mat = []
for _ in range(row):
       num = list(map(int, input("enter val : "). split()))
       mat.append(num)

last_sum = [num[-1] for num in mat]
ans = sum(last_sum)

print(ans)














