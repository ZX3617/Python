def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
num=998
result = factorial(num)
print(f'The factorial of {num} is:{result}')