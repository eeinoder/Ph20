""" Ph 20 assignment 1
By: Nicolae Einoder
Date: 4/11/2016
"""

import math
import sys
import numpy as np
import matplotlib.pyplot as plt


# Generate ASCII text files for 2)
def trigFunc1 (a, b, c, d, p):
    """ computes sequences:
            X(t) = a cos(2pi b t)
            Y(t) = c sin(2pi d t + p)
            Z(t) = X(t) + Y(t)
        for n time-steps of size t
    """
    t = 0.1
    n = 10
    
    f1 = open('x_file.txt', 'w')
    f2 = open('y_file.txt', 'w')
    f3 = open('z_file.txt', 'w')
    f4 = open('xyz_file.txt', 'w')
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
    for i in range(len(ylist_x)):
        f4.write('%f \t\t %f \t\t %f \n' % (ylist_x[i], ylist_y[i], ylist_z[i]))
    
    
    
# Generate Lissajous curves for 3a) and 3b)    
def trigFunc2 (a, b, c, d, p):
    t = 0.01
    n = 100
    
    x = np.arange(n+1)
    X = a * np.cos(2 * np.pi * b * t * x)
    Y = c * np.sin(2 * np.pi * d * t * x + p)
    
    plt.plot(X, Y)
            
    x_label = 'X(t) = %f * cos(2pi * %f * t)' % (a, b)
    y_label = 'Y(t) = %f * sin(2pi * %f * t + %f)' % (c, d, p)
    # title = 'b:d Ratio = %f : %f' % (b, d)
    title = 'Z(t) where b:d is %f : %f' % (b, d)
    # for imagename, assumming 'abc' is distinct permutation from other
    # imagenames to be saved to directory
    imagename = 'func2_pic%d%d%d.png' % (a,b,c)
    # b:d is equivalent to fx:fy
            
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(imagename)



# Observe relation between phi and curve shape when fx=fy for 3c)
# Assuming fx=fy and p=0, or anything between 0 and pi/4
def trigFunc3 (a, b, c, d, p):
    t = 0.01
    n = 100
    
    phis = np.arange(p,7,np.pi/4)
    aprx = ['0','$\pi/4$','$\pi/2$','$3\pi/4$','$\pi$','$5\pi/4$','3$\pi/$2',
    '$7\pi/4$','$2\pi/$']
    x = np.arange(n+1)
    X = a * np.cos(2 * np.pi * b * t * x)
    
    for i, phi  in enumerate(phis):
        Y = c * np.sin(2 * np.pi * d * t * x + phi)
        plt.plot(X, Y, label=str(phi) + '  ~  ' + aprx[i])
            
    x_label = 'X(t) = %f * cos(2pi * %f * t)' % (a, b)
    y_label = 'Y(t) = %f * sin(2pi * %f * t + $\phi$)' % (c, d)
    title = 'Lissajous figures: $\phi$ vs. curve shape'
    imagename = 'func3_pic.png'
            
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.savefig(imagename)




# 
def trigFunc4(a, b, c, d, p):
    """ computes sequences:
            X(t) = a cos(2pi b t)
            Y(t) = c sin(2pi d t + p)
            Z(t) = X(t) + Y(t)
        for n time-steps of size t
    """
    t = 0.01
    n = 10000
    
    x = np.arange(n+1)
    X = a * np.cos(2 * np.pi * b * t * x)
    Y = c * np.sin(2 * np.pi * d * t * x + p)
    Z = X + Y
    # these lists will be the y-coordinates of each sequence, 
    # X, Y, and Z, respectively, across time n*t
    
    
    #Q = a * np.cos(np.pi * (b+d) * t * x) # waveform with avg. freq.
    #R = a * np.cos(np.pi * 2 * (b-d) * t * x) # waveform w/ diff. freq.
    #S = a * np.cos(np.pi * (b-d) * t * x) # waveform w/ diff. freq. over 2
    # plt.plot(x, Q)
    
    # the first is an example of a carrier freq., the second a modulation
    # freq.
    
    plt.plot(x, X)
    plt.plot(x, Y)
    plt.plot(x, Z)
    # this is what we plot for 4
            
    x_label = 'X(t) = %f * cos(2pi * %f * t)' % (a, b)
    y_label = 'Y(t) = %f * sin(2pi * %f * t + %f)' % (c, d, p)
    # title = 'b:d Ratio = %f : %f' % (b, d)
    title = 'Beat frequencies, b:d is %f : %f' % (b, d)
    # b:d is equivalent to fx:fy
    imagename = 'func4_pic%d.png' % ((d/b) * 100)
            
            
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(imagename)
    
    
    

def main():
    # assume command line arguments are correct
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = float(sys.argv[4])
    p = float(sys.argv[5])
    
    # Either 1, 2, 3, or 4. 
    # 1 calls trigFunc1 and produces X,Y,Z ascii files.
    # 2 calls trigFunc2 and produces various plots. Etc.
    key = int(sys.argv[6])
    
    if(key == 1):
        trigFunc1(a,b,c,d,p)
    elif(key == 2):
        trigFunc2(a,b,c,d,p)
    elif(key == 3):
        trigFunc3(a,b,c,d,p)
    elif(key == 4):
        trigFunc4(a,b,c,d,p)
        
            
if __name__ == '__main__':
  main()
        
        
        