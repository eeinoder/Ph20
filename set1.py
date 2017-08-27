""" Ph 20 assignment 1
By: Nicolae Einoder
Date: 4/11/2016
"""

import math
import sys
import numpy as np
import matplotlib.pyplot as plt


def trigFunc1 (a, b, c, d, p, t, n):
    """ computes sequences:
            X(t) = a cos(2pi b t)
            Y(t) = c sin(2pi d t + p)
            Z(t) = X(t) + Y(t)
        for n time-steps of size t
    """
    
    f1 = open('x_file', 'w')
    f2 = open('y_file', 'w')
    f3 = open('z_file', 'w')
    # files to be written to; will contain y-coordinates of 
    # X(t), Y(t), and Z(t), respectively
    
    
    xlist = []
    # this list will be the x-coordinates
    
    ylist_x = []
    ylist_y = []
    ylist_z = []
    # these lists will be the y-coordinates of each sequence, 
    # X, Y, and Z, respectively, across time n*t
    
    for i in range(n+1):
        x = a * math.cos(2 * math.pi * b * t * i)
        y = c * math.sin(2 * math.pi * d * t * i + p)
        z = x + y
        
        ylist_x.append(x)
        ylist_y.append(y)
        ylist_z.append(z)
            
        xlist.append(i)
        
        
    # Note: this part is not necessary if we were to directly write items of
    # X, Y, and Z to respective files as they are calculated in for loop above.
        
    for item in ylist_x:
        f1.write('%f\n' % item)
    for item in ylist_y:
        f2.write('%f\n' % item)
    for item in ylist_z:
        f3.write('%f\n' % item)
    
    
    
def trigFunc2 (a, b, c, d, p, t, n):
    """ computes sequences:
            X(t) = a cos(2pi b t)
            Y(t) = c sin(2pi d t + p)
            Z(t) = X(t) + Y(t)
        for n time-steps of size t
    """
    
    x = np.arange(n+1)
    X = a * np.cos(2 * np.pi * b * t * x)
    Y = c * np.sin(2 * np.pi * d * t * x + p)
    # Z = X + Y
    # these lists will be the y-coordinates of each sequence, 
    # X, Y, and Z, respectively, across time n*t
    
    
    # Q = a * np.cos(np.pi * (b+d) * t * x) # waveform with avg. freq.
    R = a * np.cos(np.pi * 2 * (b-d) * t * x) # waveform w/ diff. freq.
    # S = a * np.cos(np.pi * (b-d) * t * x) # waveform w/ diff. freq. over 2
    # plt.plot(x, Q)
    
    # the first is an example of a carrier freq., the second a modulation
    # freq.
    
            
    # plt.plot(X, Y)
    # this is what we plot for 3
            
    plt.plot(x, X)
    plt.plot(x, Y)
    # plt.plot(x, Z)
    # this is what we plot for 4
    
    plt.plot(x, R)
    # plt.plot(x, S)
            
    x_label = 'X(t) = %f * cos(2pi * %f * t)' % (a, b)
    y_label = 'Y(t) = %f * sin(2pi * %f * t + %f)' % (c, d, p)
    # title = 'b:d Ratio = %f : %f' % (b, d)
    title = 'Z(t) where b:d is %f : %f' % (b, d)
    # b:d is equivalent to fx:fy
            
            
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    
    

def main():
    # assume command line arguments are correct
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = float(sys.argv[4])
    p = float(sys.argv[5])
    
    t = float(sys.argv[6])
    n = int(sys.argv[7])
    
    trigFunc1(a,b,c,d,p,t,n)
    trigFunc2(a,b,c,d,p,t,n)
        
            
if __name__ == '__main__':
  main()


# For 4. in set1

'''
The period of the beat is the time between two successive 
destructive/constructive interferences, when the two waves 
are completely out of / in phase.
This occurs with frequency f1 - f2. With a frequency of 
(f1-f2) / 2, we would get two beat envelopes, which 
is double the beat length, or half the beat frequency.
'''
        
        
        
        
        
        
        