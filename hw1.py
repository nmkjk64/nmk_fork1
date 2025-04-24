import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)
r  = 1 + np.sin(4*theta)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)

ax.set_title("Line Plot on Polar Axis")
plt.savefig("hw1_plot.pdf", format="pdf") # save the plot here

plt.show()


