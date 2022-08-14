def f(x):
    return x**6 - x - 1

def secant(x0, x1, error):
    while True:
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        delx = abs(x2-x1)
        
        if delx < error:
            return x2, delx
        
        x0 = x1
        x1 = x2

print(secant(0, 2, 1e-6))