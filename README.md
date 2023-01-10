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

The `julia()` method returns an iterated version of the function onto itself. 
__Note that I will update this method to limit the value to a small threshold, thereby rendering a proper approximation of a Julia Set.__


### Display Methods

There are multiple ways to display the complex function :

#### `show()` and `show_with_julia()

The `show()` method takes one optional argument :
- `save`, which defaults to `False`, but can be a string to specify the filename.

---

Examples of `show()` displays :
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/show1.png)
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/isin(e%5Ez).png)

---


The `show_with_julia()` method takes multiple optional arguments : 
- save, which defaults to `False`, but can be a string to specify the filename.
- coloring : the function used to color the render. Defaults to `hls_dc` Hue-Light-Saturation Domain Coloring. Use `modulus_limited_cmap_dc` to color the render using the custom `cmap`.

---

Examples of what `show_with_julia()` displays (last image is a duplicate with custom `cmap`) : 
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/shuriken1000.png)
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/icos(e)hls.png)
![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/icos(e).png)

---


#### `show_parametric()` and `show_full_parametric()`



![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/testingc.png)

![](https://github.com/ChrisMzz/complex-analysis/blob/main/readme_files/ztoc.gif)









