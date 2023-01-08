import numpy as np
import matplotlib.pyplot as plt
from colorsys import hls_to_rgb


pi = np.pi
e = np.exp(1)

def sin(z):
    return (e**(1j*z) - e**(-1j*z))/2j

def cos(z):
    return (e**(1j*z) + e**(-1j*z))/2


def reduce(n):
    while n >= 1:
        n /= 3
    return n*0.8

def mult(z, n):
    mult = 1
    for _ in range(n):
        mult *= z
    return mult

# from https://stackoverflow.com/a/20958684/17091581
def hls_dc(z):
    h = (np.angle(z) + pi)  / (2 * pi) + 0.5
    l = np.vectorize(reduce)(np.abs(z))**1.1
    s = 1
    c = np.vectorize(hls_to_rgb)(h,l,s)
    c = np.array(c)  # -->  array of (3,n,m) shape, but need (n,m,3)
    c = c.transpose(2,1,0)
    return c

def check_modulus(a, limit, scaling_factor):
    if a > limit or str(a) == "nan":
        return 1
    elif a > 0.01:
        segmentation = [eps for eps in np.arange(0,1, 1/100)]
        return segmentation[int((np.log(a)/np.log(scaling_factor)) % 100)]


class ComplexFunction :
    
    def __init__(self, shape, f, **kwargs):
        self.minRe, self.maxRe, self.minIm, self.maxIm = shape
        self.f = f
        
        if "N" in kwargs.keys():
            self.N = kwargs["N"]
        else:
            self.N = 1000
        if "iters" in kwargs.keys():
            self.iters = kwargs["iters"]
        else:
            self.iters = 5
        if "limit" in kwargs.keys():
            self.limit = kwargs["limit"]
        else:
            self.limit = 50
        if "scaling_factor" in kwargs.keys():
            self.scaling_factor = kwargs["scaling_factor"]
        else:
            self.scaling_factor = 99/100
        if "cmap" in kwargs.keys():
            self.cmap = kwargs["cmap"]
        else:
            self.cmap = plt.get_cmap("cool")
        
        x,y = np.ogrid[self.minRe:self.maxRe:self.N*1j, self.minIm:self.maxIm:self.N*1j]
        self.z = x + 1j*y

    def julia(self, z):
        """Compute the `iters` first iterations of the function on itself.

        Args:
            z (array-like) complex number

        Returns:
            _type_: array-like complex numbers
        """
        z0 = z
        for _ in range(self.iters):
            z0 = self.f(z0)
        return z0
    
    def show_with_julia(self, save=False, coloring=hls_dc):
        """Show the function, and a version of itself iterated `iters` number of times.

        Args:
            save (bool, optional): Whether to save the figure or not. Defaults to False.
        """
        N, minRe, maxRe, minIm, maxIm = self.N, self.minRe, self.maxRe, self.minIm, self.maxIm 
        f, z = self.f, self.z
        fig = plt.figure()
        axf = plt.subplot2grid((1,2),(0,0))
        axj = plt.subplot2grid((1,2),(0,1))
        axf.imshow(coloring(f(z)))
        axf.set_xticks([N*i/4 for i in range(5)], [np.round(minRe + 2*k*maxRe,2) for k in np.arange(0,1.1,1/4)])
        axf.set_yticks([N*i/4 for i in range(5)], [np.round(minIm + 2*k*maxIm,2) for k in np.arange(0,1.1,1/4)])
        axj.imshow(coloring(self.julia(z)))
        axj.set_xticks([N*i/4 for i in range(5)], [np.round(minRe + 2*k*maxRe,2) for k in np.arange(0,1.1,1/4)])
        axj.set_yticks([N*i/4 for i in range(5)], [np.round(minIm + 2*k*maxIm,2) for k in np.arange(0,1.1,1/4)])
        plt.show()
        if type(save) == str:
            fig.savefig(f"{save}.png", dpi=int(N*1.5), format="png")
        elif save:
            fig.savefig("julia.png", dpi=int(N*1.5), format="png")

    def show(self, save=False):
        """Show the function.

        Args:
            save (bool, optional): Whether to show the function or not. Defaults to False.
        """
        N, minRe, maxRe, minIm, maxIm = self.N, self.minRe, self.maxRe, self.minIm, self.maxIm 
        f, z = self.f, self.z
        fig, ax = plt.subplots()
        ax.imshow(hls_dc(f(z)))
        ax.set_xticks([N*i/4 for i in range(5)], [np.round(minRe + 2*k*maxRe,2) for k in np.arange(0,1.1,1/4)])
        ax.set_yticks([N*i/4 for i in range(5)], [np.round(minIm + 2*k*maxIm,2) for k in np.arange(0,1.1,1/4)])
        plt.show()
        if type(save) == str:
            fig.savefig(f"{save}.png", dpi=int(N*1.5), format="png")
        elif save:
            fig.savefig("function.png", dpi=int(N*1.5), format="png")
          
        
    def modulus_limited_cmap_dc(self, z):
        a = np.abs(z)
        c = np.vectorize(check_modulus)(a, self.limit, self.scaling_factor)
        c = [self.cmap(cmap_value) for cmap_value in c]
        c = np.array(c)
        c = c.transpose(1,0,2)
        return c

