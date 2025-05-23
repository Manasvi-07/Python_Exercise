# 1st ----------------

n=5
for i in range(n):
    for j in range(n):
        if i/2 == 1 or j/2 == 1 or i-2 == j or j-2 == i:
            print("_", end=" ")
        elif j == n-1 or i==0:
            print("*", end=" ")
        elif i==j:
            print("_", end=" ")
        else:
            print("*", end =" ")
    print()

# 2nd -------------------


n=5
for i in range(n):
    for j in range(n):
        if i/2 == 1 or j/2 == 1 or i-2 == j or j-2 == i:
            print("*", end=" ")
        elif j == n-1 or i==0:
            print("_", end=" ")
        elif i==j:
            print("*", end=" ")
        else:
            print("_", end =" ")
    print()

# 3rd-----------------------

n=5
for i in range(n+1):
    for j in range(i):
        if i == n or j == 0 or j == i-1 :
            print("*", end = " ")
        else:
            print("_", end = " ")
    print()

# 4th ---------------------

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*", end = " ")
        else:
            print("_", end = " ")
    print()

# 5th --------------------------

n=5 
num = 1
for i in range(1,n+1):
    for j in range(1, i+1):
        print(num, end = " ")
        num += 1
    print()
