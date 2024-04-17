# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:03:05 2023

@author: frede

# COUPLED VAN DER POL OSCILLATORS
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
import numpy as np

# PARAMETERS:

x10 = -0.1 # initial x
y10 = -0.1 # initial y
x20 = 0.1
y20 = 0.1
N = 10000
dt = 1/N # time increment
x_win = 8 # x window plot
y_win = 8 # y window plot


# FUNCTIONS:

def F1(x, y, z, t):
    """
    Van der Pol oscillator
    """
    return (y, -x + (1 - 0.5 * x**2) * y + 6 * np.tanh(3*x - 2*z)  + 1 * np.cos(t)) 


def F2(x, y, z, t):
    """
    Van der Pol oscillator
    """
    return (y, -x + (1 - 0.5 * x**2) * y + + 8 * np.arctan(2*x - 1*z) - 1 * np.cos(t)) #


def Euler(x10, y10, x20, y20, dt, n, F1, F2):
    """
    input: initial point time increment and n iterations
    output: list of points
    """
    L1 = [ (x10, y10) ]
    L2 = [ (x20, y20) ]
    
    x1_old = x10
    y1_old = y10
    x2_old = x20
    y2_old = y20
    
    t = 0
    for i in range(n):
        
        x1_new = x1_old + dt * F1(x1_old, y1_old, x2_old, t)[0]
        y1_new = y1_old + dt * F1(x1_old, y1_old, x2_old, t)[1]    
        L1.append( (x1_new, y1_new) )
        (x1_old, y1_old) = (x1_new, y1_new)
        
        x2_new = x2_old + dt * F2(x2_old, y2_old, x1_old, t)[0]
        y2_new = y2_old + dt * F2(x2_old, y2_old, x1_old, t)[1] 
        L2.append( (x2_new, y2_new) )
        (x2_old, y2_old) = (x2_new, y2_new)
        
        t = t + dt
    
    return L1, L2


def RunCounter(filename, reset=False):

    f = open("run_counter_{}.txt".format(filename), "a+")
    
    if reset == True:
        f.truncate(0)

    f.seek(0)
    lines = f.readlines()
    if len(lines) == 0:
        f.write("0")
        f.seek(0)
        lines = f.readlines()
    else:
        f.write("\n1")
        f.seek(0)
        lines = f.readlines()
    f.close()
    
    return len(lines)














Points1, Points2 = Euler(x10, y10, x20, y20, dt, N, F1, F2)
#print(Points)



fig = plt.figure(figsize=(6,6))

ax = fig.add_subplot(111)
#plt.tick_params(left = False, right = False , labelleft = False ,
                #labelbottom = False, bottom = False)

ax.set_xlim([- x_win, x_win])
ax.set_ylim([- y_win, y_win])

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

plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

plt.xlabel(r"$u$", loc = 'right', fontsize=20, rotation=0)
plt.ylabel(r"$u'$", loc = 'top', fontsize=20, rotation=0)


# Add points to figure:  
px1 = [p[0] for p in Points1]
py1 = [p[1] for p in Points1]
ax.plot(px1, py1, "o", c='b', markersize=1)

px2 = [p[0] for p in Points2]
py2 = [p[1] for p in Points2]
ax.plot(px2, py2, "o", c='r', markersize=1)

# legend:
plt.legend(["vdp 1", "vdp 2"], loc ="upper left", fontsize=16, markerscale=10)


run_count = RunCounter("van_der_pol", True) # number of times program as run
print(run_count)

#display(fig)
fig.savefig('van_der_pol{}.png'.format(run_count))   








