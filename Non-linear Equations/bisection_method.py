def f(x):
    return x**6 - x - 1

def bisection(a, b, error):
    step = 0
    
    while f(a)*f(b) < 0:
        step += 1
        c = (a+b)/2
        err = abs(b-a)

        if err < error:
            break
            
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c) > 0:
            a = c
        else:
            break

    return c, err, f(c), step

print(bisection(0, 2, 0.1))