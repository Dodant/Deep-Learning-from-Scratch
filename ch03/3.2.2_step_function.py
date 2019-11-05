import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

def step_function_2(x):
    y = x > 0
    return y.astype(np.int)

def step_function_3(x):
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function_3(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)
plt.show()
