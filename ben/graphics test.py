import numpy as np
import matplotlib.pyplot as plt


coordinates=[[0,5],[1,2],[5,6]]

# Plotting the circles
radius=0
for point in range(len(coordinates)):
    if np.sqrt(coordinates[point][0]**2+coordinates[point][1]**2)>radius:
        radius=np.sqrt(coordinates[point][0]**2+coordinates[point][1]**2)  
fig, ax = plt.subplots()
print(radius)
bounding_circle = plt.Circle((0, 0),radius + 0.5, color='r', fill=False)
ax.add_artist(bounding_circle)

for point in range(len(coordinates)):
    circle = plt.Circle((coordinates[point][0],coordinates[point][1]), 0.5, color='b', fill=False)
    ax.add_artist(circle)

ax.set_xlim(-2*radius+1, 2*radius+1)
ax.set_ylim(-2*radius+1, 2*radius+1)
ax.set_aspect('equal')
plt.show()
