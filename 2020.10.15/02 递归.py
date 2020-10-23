import time
#斐波那契数列
def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)
start = time.time()
print(f(40))
end = time.time()
print(end - start)
