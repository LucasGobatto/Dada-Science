import numpy as np
import sdeint
import matplotlib.pyplot as plt

r = 1.0
alfa = 0.8
tspan = np.linspace(0.0, 5.0, 5001)
x0 = 0.5

def f(x, t):
    return r*x

def g(x, t):
    return alfa*x

result = sdeint.itoint(f, g, x0, tspan)
plt.plot(tspan, result)
plt.show()
