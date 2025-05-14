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

def sum_Number(number):
    if not number:
        return 0
    return number[0] + sum_Number(number[1:])

number = [23,44,5,67,1,1,2,4,5]
print("Sum of Number : ", sum_Number(number))

