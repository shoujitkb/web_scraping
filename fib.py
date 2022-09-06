def fib(n):
    if n<1:
        return 0
    elif n==1:
        return 1
    elif n==1:
        return 2
    else:
        return fib(n-2)+fib(n-1)

#for i in range(7):
#    print(fib(i))
number=int(input("数字を入力してください:"))
print(fib(number))