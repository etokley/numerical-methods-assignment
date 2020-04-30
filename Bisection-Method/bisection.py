'''
This function will approximate the root of
an equation using bisection methods
....elton...
'''
#import math

def elt_bisect(func,a,b,tol):
    n = 1
    criteria = abs(b-a)
    ''' This is the stopping criteria. The approximate answer
        is given when criteria is less than the error tolerance.'''
    while criteria > tol:
        if func(a)*func(b) > 0:
            print('No root in [{} {}] @ n = {}\n'.format(a,b,n))
            break
        else:
            c = (a+b)/2
            if func(a)*func(c) == 0:
                print('Solution found : root = {}, @ n = {} current interval [{} {}]\n'.format(c,n,a,b))
                break
            else:
                if func(a)*func(c) > 0:
                    a = c
                    print('Interval : @ n = {} current interval [{} {}]\n'.format(n,c,a,b))
                else:
                    b = c
                    print('Interval : @ n = {} current interval [{} {}]\n'.format(n,c,a,b))
        n = n + 1
    criteria = abs(b-a)
    if criteria < tol:
        print('Criterion met : root = {}, @ n = {} current interval [{} {}]\n'.format(n,c,a,b))

#Let's hope this works.... XD.. :)...;)
print('|||||||  ||||   ||| ||||||| ||||||| ||||    ||| ||||||| ||||||||| ||||||    x ')
print('  |||    |||||| ||| |||       |||   ||||||  |||   |||      |||    |||      xxx')
print('  |||    ||| |||||| |||||     |||   |||  ||||||   |||      |||    ||||||    x ')
print('  |||    |||  ||||| |||       |||   |||   |||||   |||      |||    |||      xxx')
print('|||||||  |||   |||| |||     ||||||| |||    |||| |||||||    |||    ||||||    x ')
def func(x):
    ans = x**3 + 4*x**2 - 10
    return ans

if __name__ == '__main__':
    elt_bisect(func,1,2,0.01)
