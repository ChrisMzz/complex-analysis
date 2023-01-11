from complex_function import *
import matplotlib.pyplot as plt


# run is a boolean value used to test certain methods


# ------------------
# example of spacetime parametrisation implementation
run = True
if run:
    parametric = lambda z,c : z*sin(e**(2j*cos(z**2))-c)
    parameters = [e**(2j*i*pi/128) for i in range(128)]
    for i in range(128):
        c = parameters[i]
        f = ComplexFunction([-2,2,-2,2], f=(lambda z : parametric(z,c)), param_f=(lambda z,a : z*sin(e**(2j*cos(z**2))+a-c)), N=100, iters=8, cmap=plt.get_cmap("PuRd"))
        #f.show_parametric([np.linspace(-1,1,32)], save=f"dump/zc/{i}", show_at_zero=True, show_julia_at_zero=True, show=False)    
        f.show_full_parametric([[e**(2j*i*pi/32) for i in range(32)]], save=f"dump/cot/{i}", show=False)




# 







