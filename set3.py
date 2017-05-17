# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:13:42 2017

@author: nicolaeeinoder
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Expresses graphically motion of a mass on a spring, modeled by explicit
Euler method. Takes initial conditions for position and velocity, x0 and v0,
respectively, and plots x_i and v_i against time at sufficiently small time
steps t_i = t0 + ih, i = 1, ..., N.
All arguments are floating point numbers.
"""
def oscillate(x_i, v_i, h):

    # Steps from 0 to t with step size h; period in time steps
    t = 30
    t_steps = np.arange(0, t, h)
    period = 2 * np.pi / h

    # Declare arrays for x and v to be plot; initially just have initial
    # conditions as values
    x_expl = np.array([x_i] * len(t_steps))
    x_impl = np.array([x_i] * len(t_steps))
    v_expl = np.array([v_i] * len(t_steps))
    v_impl = np.array([v_i] * len(t_steps))
    # For Part 2
    x_symp = np.array([x_i] * len(t_steps))
    v_symp = np.array([v_i] * len(t_steps))


    # For 1.1, 1.2, 1.3, 1.4, 2.1: explicit euler method
    for i in range(len(t_steps) - 1):
        x_expl[i+1] = x_expl[i] + h * v_expl[i]
        v_expl[i+1] = v_expl[i] - h * x_expl[i]

    # For 1.5, 2.1: implicit euler method
    # constant evaluated from system of equations
    H = 1 / (1 + np.power(h, 2))
    for i in range(len(t_steps) - 1):
        x_impl[i+1] = H * (x_impl[i] + h * v_impl[i])
        v_impl[i+1] = H * (v_impl[i] - h * x_impl[i])
        
    # For 2.2: symplectic euler method
    for i in range(len(t_steps) - 1):
        x_symp[i+1] = x_symp[i] + h * v_symp[i]
        v_symp[i+1] = H * (v_symp[i] - h * x_symp[i])


    # For our derived equations, k/m = 1, so omega = omega^2 = 1. For our
    # initial conditions, phi = 0. Let A = 1.
    # x = cos(t), v = -sin(t)
    x = np.cos(t_steps)
    v = -np.sin(t_steps)


    # For 1.1
    #plt.plot(x_expl)
    #plt.plot(v_expl)

    #x_label = 'Steps, where 1 cycle = 2pi * (1/h) = %f steps' % period
    #y_label = 'Relative Displacement (Blue) and \nVelocity (Green)'
    #title = 'Oscillatory motion of mass on a string: \n' \
    #'Plots x and v, displacment and velocity, against time steps'

    # For 1.2
    #x_err = np.absolute(x - x_expl)
    #v_err = np.absolute(v - v_expl)
    #max_err = np.max([np.max(x_err), np.max(v_err)])
    # the above, max_err, is to give a reasonable scale to the y-axis

    #plt.axis([0, len(t_steps), 0, 2 * max_err])
    #plt.plot(np.absolute(x - x_expl))
    #plt.plot(np.absolute(v - v_expl))

    #x_label = 'Steps, where 1 cycle = 2pi * (1/h) = %f steps' % period
    #y_label = 'Global error in Displacement (Blue) and \nVelocity (Green)'
    #title = 'Oscillatory motion of mass on a string, Part 2'


    # For 1.3, 1.5
    #x_err = np.absolute(x - x_expl)
    #return np.max(x_err)

    # For 1.4
    #energy_approx = np.power(x_approx, 2) + np.power(v_approx, 2) - 1
    #energy = np.power(x, 2) + np.power(v, 2) - 1
    #plt.plot(energy_approx)
    #plt.plot(energy)
    # we replace x_approx and v_approx with x_expl and v_expl, and x_impl
    # and v_impl for 1.4 1.5, respectively

    #x_label = 'Steps, where 1 cycle = 2pi * (1/h) = %f steps' % period
    #y_label = 'Total energy (Green) and Approximate form (Blue)'
    #title = 'Approx. Energy evolution vs. Global Errors in x and v'
    
    
    
    # For 1.5
    # global errors for implicit euler approximation
    #x_impl_err = np.absolute(x - x_impl)
    #v_impl_err = np.absolute(v - v_impl)
    #max_err = np.max([np.max(x_impl_err), np.max(v_impl_err)])
    
    #plt.axis([0, len(t_steps), 0, 2 * max_err])
    #plt.plot(x_impl_err, label='Displacement')
    #plt.plot(v_impl_err, label='Velocity')
    
    #x_label = 'Steps, where 1 cycle = 2pi * (1/h) = %f steps' % period
    #y_label = 'Global error in Displacement'
    #title = 'Oscillatory motion of mass on a string, \nImplicit Euler method'
    #plt.legend()
    
    # Energy evolution: explicit vs. implicit
    #E_expl = np.power(x_expl, 2) + np.power(v_expl, 2)
    #E_impl = np.power(x_impl, 2) + np.power(v_impl, 2)
    
    #plt.plot(E_expl, label='Explicit Euler')
    #plt.plot(E_impl, label='Implicit Euler')
    
    #x_label = 'Steps, where 1 cycle = 2pi * (1/h) = %f steps' % period
    #y_label = 'Energy'
    #title = 'Energy evolution: Explicit vs. Implicit'
    #plt.legend()
    
    
    
    # For 2.1
    plt.plot(x,v, label='Real')
    plt.plot(x_expl, v_expl, label='Expl approx')
    plt.plot(x_impl, v_impl, label='Impl approx')
    
    x_label = 'x, displacement'
    y_label = 'v, velocity'
    title = 'Phase space, h = %f' % h
    plt.legend()
    
    # For 2.2
    #plt.plot(x_symp, v_symp, label='Symp approx')
    
    #x_label = 'x, displacement'
    #y_label = 'v, velocity'
    #title = 'Phase space, h = %f' % h
    #plt.legend()
    
    # For 2.3
    #E_symp = np.power(x_symp, 2) + np.power(v_symp, 2)
    #E = np.power(x, 2) + np.power(v, 2)
    #plt.plot(E_symp, label='Symplectic approx')
    #plt.plot(E, label='Analytic')
    
    #x_label = 'steps'
    #y_label = 'Energy'
    #title = 'Energy evolution, h = %f' % h
    #plt.legend()
    
    # For 1.1, 1.2, 1.4, 1.5
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    
    

"""
Calculate relationship between truncation error and h.
Plot max x_err against different values of h:
h0 (argument), h0/2, h0/4, h0/8, and h0/16
"""
def trunc_err(h):
    x_err = np.zeros(5)
    h_vals = h * np.power(.5, range(5))


    for i in range(5):
        x_err[i] = oscillate(1.0, 0.0, h_vals[i])

    plt.plot(h_vals, x_err)

    x_label = 'h values where h0 = %f' % h
    y_label = 'Max Error in x for different values of h'
    title = 'Relationship between truncation error in x and h.'

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
