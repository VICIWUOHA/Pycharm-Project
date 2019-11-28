import numpy as np
import matplotlib.pyplot as plt

axes_values = np.arange(-200, 200, 20)

dx, dy = np.meshgrid(axes_values, axes_values)

function = 2*dx + 3*dy
function2 = np.cos(dx) + np.cos(dy)


print(function)

plt.imshow(function2)
plt.title('plot of dy* dx plot')
plt.colorbar()
plt.savefig('second_plot.png')
