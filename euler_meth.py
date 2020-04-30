'''
This function will solve O.D.E's using Euler's method
'''

#import math

def euler_met(func,x,y,h,n):

    for i in range(0,int(n)+1):
        print(i)

        print("The ith iterations @ {}".format(i))

        y = y + h*func(x,y)
        print("The solution at {}th iteration is {}".format(i,y))
        x = x + h

        print("x at {}th iteration in {}\n".format(i,x))


def func(x,y):
    ans = (-2.2067*(10**-12))*(y**4 -81*10**8)
    return ans

#Let's hope this works.... XD.. :)...;)
print('|||||||  ||||   ||| ||||||| ||||||| ||||    ||| ||||||| ||||||||| ||||||    x ')
print('  |||    |||||| ||| |||       |||   ||||||  |||   |||      |||    |||      xxx')
print('  |||    ||| |||||| |||||     |||   |||  ||||||   |||      |||    ||||||    x ')
print('  |||    |||  ||||| |||       |||   |||   |||||   |||      |||    |||      xxx')
print('|||||||  |||   |||| |||     ||||||| |||    |||| |||||||    |||    ||||||    x ')

if __name__ == '__main__':
    n = input("Enter the value on n: ")
    euler_met(func,0,1200,240,n)
