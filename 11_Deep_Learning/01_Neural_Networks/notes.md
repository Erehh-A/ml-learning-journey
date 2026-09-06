Python notes : 
('a') is not tuple but ('a', ) is

Gradient - How the output will change with respect to input change
ex : in the first figure of micrograd.ipynb, if a += h, then what's dG/da

Key to remember : 
For +, the local gradient is always 1 for both inputs.
For *, the local gradient with respect to one input is the value of the other input.

diff or tan(x) = 1 - (tan(x))**2