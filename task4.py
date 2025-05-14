# ---------- n-th fibonacci number using Recursion 

def fibonacci(n, num={}):
    if n in num:
        return num[n]
    if n <= 2:
        return 1
    return fibonacci(n-1, num) + fibonacci(n-2, num)
   
n = int(input("Enter number : "))
print("Fibonacci number : ", fibonacci(n))    


# ------- Number of sum using Recursion

def sum_Number(Number):
    if not Number:
        return 0
    return Number[0] + sum_Number(Number[1:])

Number = [23,44,5,67,1,1,2,4,5]
print("Sum of Number : ", sum_Number(Number))

