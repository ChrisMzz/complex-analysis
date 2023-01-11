# Complex Analysis

Hello! This repository contains a few classes and files about complex analysis (so far, I've only written `complex_function`, but I'll update this when I can).


## Complex Functions Display

The `complex_function` file contains the `ComplexFunction` class.
A `ComplexFunction` object is called as follows : 

```py
from complex_function import ComplexFunction

f = ComplexFunction([-2,2,-2,2], lambda z : z**2)

```

where :
- `[-2,2,-2,2]` is the list of verteces of the complex rectangle in which the function is studied (minimum real part, maximum real part, minimum imaginary part, maximum imaginary part).
- `lambda z : z**2` is the complex lambda function.

a `ComplexFunction` also has optional arguments :
- `N` is the width (in pixels/squares drawn) of the image. You can think of it as *resolution* (defaults to `1000`).
- `iters` is the number of iterations done during a julia set render (defaults to `5`).
- `cmap` is a custom `matplotlib` color map to use for some methods (defaults to `matplotlib.pyplot.get_cmap("cool")`).
- `param_f` is a custom parametric function to use when rendering the function's parametric space (defaults to `lambda z,c : f(z)+c`).
- `scaling_factor` is the logarithmic color sequencing factor (works weirdly with this class, defaults to `99/100`).

### Julia render

The `julia()` method returns an iterated version of the function onto itself. The repetitive color sequencing allows you to see where the function stays bounded. **Note that a `nan` value will result in an error in the computation, which conveniently results in a black pixel render, so we don't have to explicitly tell the method to check for values that grow to $+\infty$.**


### Display Methods

There are multiple ways to display the complex function :

#### `show()` and `show_with_julia()`

The `show()` method displays the function using HLS Domain Coloring. 
It takes one optional argument :
- `save`, which defaults to `False`, but can be a string to specify the filename.

---

Examples of `show()` displays :
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/show1.png)
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/isin(e%5Ez).png)

---


The `show_with_julia()` method displays side-by-side renders of the function (left) and its rendered julia set (right). 
It takes multiple optional arguments : 
- `save`, which defaults to `False`, but can be a string to specify the filename.
- `coloring` : the function used to color the render. Defaults to `hls_dc` Hue-Light-Saturation Domain Coloring. Use `modulus_limited_cmap_dc` to color the render using the custom `cmap`.

---

Examples of what `show_with_julia()` displays (last image is a duplicate with custom `cmap`) : 
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/shuriken1000.png)
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/icos(e)hls.png)
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/icos(e).png)

---


#### `show_parametric()` and `show_full_parametric()`

The `show_parametric(c_vector)` displays a 3D grpah of the function where the X and Y axes are the complex plane and the Z axis is the one-dimensional parametric space, determined along a complex curve `c_vector`.
It takes multiple optional arguments : 
- `save`, whether to save the image or not. Defaults to `False`. 
- `show_at_zero`, whether to display the image with slice of the function at $c=0$ or not. Defaults to `False`.
- `show_julia_at_zero`, whether to display the image with slice of the julia render at $c=0$ or not. Defaults to `False`.
- `show`, whether to display or not (pratical for mass rendering). Defaults to `False`.

---

Examples of what `show_parametric(c_vector)` displays.

![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/testingc.png)
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/showparam.png)

---

The `show_full_parametric(c_vector)` displays the same 3D graph, but replaces all optional parameters to `True` except for show, which now becomes a default `False`.

---

Examples of what `show_full_parametric(c_vector)` displays.

![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/showfullparam.png)


It's mainly used to create a parametric spacetime (by using a `gif` generator, for example). Here is an example

```py
from complex_function import *
import matplotlib.pyplot as plt

parametric = lambda z,c : z*sin(e**(2j*cos(z**2))-c)
parameters = [e**(2j*i*pi/128) for i in range(128)]


for i in range(128):
    c = parameters[i]
    f = ComplexFunction([-2,2,-2,2], lambda z : parametric(z,c), N=100, iters=8)
    # the default parametric f_param is : lambda z, lambda parametric(z,c) + lambda
    f.show_full_parametric([np.linspace(-1,1,64)], save=f"dump/{i}", show=False)
```

![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/ztoc.gif)

---






