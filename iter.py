def Factorial(n):
    if n < 1:
        return 1
    else:
        return n * Factorial(n-1)

num = 10
print("Factroial(",num,")=", Factorial(num))
num = 4
print("Factroial(",num,")=", Factorial(num))
num = 8
print("Factroial(",num,")=", Factorial(num))
num = int(input(":"))
print("Factroial(",num,")=", Factorial(num))