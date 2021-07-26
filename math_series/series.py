def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

    

def lucas(n):

    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return lucas(n-1) + lucas(n-2)
   
def sum_series(n, l = 0, c = 1):
    
 
    if l == 0 and c == 1:
        return fibonacci(n)
    elif  l == 2 and c == 1:
        return lucas(n)
    else:
        return n - 1 + n - 2
    