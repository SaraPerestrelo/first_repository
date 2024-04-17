# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 19:12:31 2023

@author: frede

van der pol euler
"""


"""
# Van der Pol Equation:
x''(t) - (1 - x^2(t)) * x'(t) + x(t) = 0

# Van der Pol System:
x'(t) = y(t)
y'(t) = -x + (1 - x^2(t)) * y(t) = F(x, y) = (x'(t), y'(t))   (vector field/campo de velocidades)
"""
# PACKAGES:
import matplotlib.pyplot as plt
from IPython.display import display

# PARAMETERS:

dt = 0.25 # time increment
x0 = 1 # initial x
y0 = 1 # initial y
N = 1000
x_win = 5 # x window plot
y_win = 5 # y window plot


# FUNCTIONS:

def F(x, y):
    """
    Van der Pol oscillator
    """
    return (y, -x + (1 - x**2) * y)


def Euler(x0, y0, dt, n):
    """
    input: initial point time increment and n iterations
    output: list of points
    """
    L = [ (x0, y0) ]
    
    x_old = x0
    y_old = y0
    
    for i in range(n):
        x_new = x_old + dt * F(x_old, y_old)[0]
        y_new = y_old + dt * F(x_old, y_old)[1]        
        L.append( (x_new, y_new) )
        (x_old, y_old) = (x_new, y_new)
    
    return L

Points = Euler(x0, y0, dt, N) 
#print(Points)



fig = plt.figure(figsize=(6,6))

ax = fig.add_subplot(111)
#plt.tick_params(left = False, right = False , labelleft = False ,
                #labelbottom = False, bottom = False)

ax.set_xlim([-x_win, x_win])
ax.set_ylim([-y_win, y_win])

ax.grid(True, which='both')

# set the x-spine
ax.spines['bottom'].set_position('zero')
# set the y-spine:
ax.spines['left'].set_position('zero')


# turn off the right spine/ticks
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()

# turn off the top spine/ticks
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()



# Add points to figure:  
px = [p[0] for p in Points]
py = [p[1] for p in Points]
ax.plot(px, py, "o", c='b', markersize=1)


display(fig)
fig.savefig('van_der_pol{}.png'.format(N))   



















