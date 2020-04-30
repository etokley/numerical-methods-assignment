'''
This function will approximate the solution to an O.D.E. using
Heun's method
'''

def heuns_met(func,x,y,h,n):

    k1 = func(x,y)
    print("This is the initial k1: {}".format(k1))

    k2 = func(x+h,y+(k1*h))
    print("This is th initial k2: {}".format(k2))

    for i in range(0,int(n)+1):
        print(i)

        y = y + (0.5*k1 + 0.5*k2)*h
        print("This is the solution @ 1={} : {}".format(i,y))

        x = x + h
        print("New x value: {}".format(x))

        k1 = func(x,y)
        print("New k1: {}".format(k1))

        k2 = func(x+h, y+(k1*h))
        print("New k2: {}\n".format(k2))

def func(x,y):

    ans = x*2.718281825**(3*x)-2*y
    return ans

#Let's hope this works.... XD.. :)...;)
print('|||||||  ||||   ||| ||||||| ||||||| ||||    ||| ||||||| ||||||||| ||||||    x ')
print('  |||    |||||| ||| |||       |||   ||||||  |||   |||      |||    |||      xxx')
print('  |||    ||| |||||| |||||     |||   |||  ||||||   |||      |||    ||||||    x ')
print('  |||    |||  ||||| |||       |||   |||   |||||   |||      |||    |||      xxx')
print('|||||||  |||   |||| |||     ||||||| |||    |||| |||||||    |||    ||||||    x ')

if __name__ == '__main__':
    n = input("please enter you desired n: ")
    heuns_met(func,0,0,0.5,n)
