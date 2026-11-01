import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# creating the plot where the circle will be drawn
# what does fig and ax mean? fig is the whole thing, ax the coordinates and the graph
fig, ax = plt.subplots(figsize=(6, 6))

# setting the limits of the plot
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# coordinate labels and titles
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Cartesian Circle')

# creating the grid for the plot
# what does alpha=0.6 mean? opacity of the grid lines
ax.grid(True, linestyle='--', alpha=0.6)

# make the grid unit squares
# what does this do? x-y equal spacing
ax.set_aspect('equal')

# creating the legend for the plot
ax.legend()

# create the square
x = [-2, 2, 2, -2, -2]
y = [-2, -2, 2, 2, -2]

# draw the square
ax.plot(x, y, color='crimson', linewidth=2, label='Square', marker='o', markersize=8)

#draw the circle
theta = np.linspace(0, 2*np.pi, 100)

# function to plot the circle
def plot_circle(r, angle):
    x_circle = r * np.cos(angle)
    y_circle = r * np.sin(angle)
    return x_circle, y_circle

# draw circle theta
# why line, ?
r = 3
x_circle, y_circle = plot_circle(r, theta)
line, = ax.plot(x_circle, y_circle , color='blue', linewidth=2, label=f'Circle (R={r})', marker='o', markersize=1)

# add room add teh bottom
plt.subplots_adjust(bottom=0.25)

# slider coordinates and slider
ax_r = plt.axes([0.25, 0.1, 0.5, 0.03], facecolor='lightgoldenrodyellow')
slider_r = Slider(ax=ax_r, label='Radius', valmin=0.5, valmax=5, valinit=r)

# update function
def update(val):
    current_r = slider_r.val
    new_x, new_y = plot_circle(current_r, theta)
    line.set_data(new_x, new_y)
    fig.canvas.draw_idle()
slider_r.on_changed(update)


# display the window
plt.show()