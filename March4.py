import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

from array import array

x=array("i",[1,2,3,4,5,6,7,8,9,10])
y=array("i",[2,3,4,5,6,7,8,9,10,11])

def average(w1,w2):

    list = []
    for i in range(len(x)):
        list.append(((w1*x[i]+w2-y[i])**2))

    return sum(list)/len(list)

w1_list=[]
w2_list=[]
error_list=[]

for i in range(0,11):
    for j in range(0,11):
        w1_list.append(i)
        w2_list.append(j)
        error_list.append(average(i,j))

error_array = np.array(error_list)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(np.array(w1_list).reshape(11, 11),
                np.array(w2_list).reshape(11, 11),
                np.array(error_list).reshape(11, 11),
                cmap='viridis', edgecolor='k')

# Set labels for the axes
ax.set_xlabel('w1_list')
ax.set_ylabel('w2_list')
ax.set_zlabel('error_list')

# Show the plot
plt.show()