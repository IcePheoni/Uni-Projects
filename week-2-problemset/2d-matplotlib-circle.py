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

#draw the circle
theta = np.linspace(0, 2*np.pi, 100)

# function to plot the circle
def plot_circle(r, angle,  angle_change_x=0, angle_change_y=0):
    x_circle = r * np.cos(angle + angle_change_x)
    y_circle = r * np.sin(angle + angle_change_y)
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

ax_angle_x = plt.axes([0.25, 0.05, 0.5, 0.03], facecolor='lightgoldenrodyellow')
slider_angle_x = Slider(ax=ax_angle_x, label='Angle Change X', valmin=-np.pi, valmax=np.pi, valinit=0)

ax_angle_y = plt.axes([0.25, 0.01, 0.5, 0.03], facecolor='lightgoldenrodyellow')
slider_angle_y = Slider(ax=ax_angle_y, label='Angle Change Y', valmin=-np.pi, valmax=np.pi, valinit=0)

def show_angle_as_pi(slider):
    def update_label(val):
        slider.valtext.set_text(f'{val / np.pi:.2g}π')

    update_label(slider.val)
    slider.on_changed(update_label)

show_angle_as_pi(slider_angle_x)
show_angle_as_pi(slider_angle_y)

# update function
def update(val):
    current_r = slider_r.val
    new_x, new_y = plot_circle(current_r, theta, slider_angle_x.val, slider_angle_y.val)
    line.set_data(new_x, new_y)
    fig.canvas.draw_idle()
slider_r.on_changed(update)
slider_angle_x.on_changed(update)
slider_angle_y.on_changed(update)


# display the window
plt.show() 