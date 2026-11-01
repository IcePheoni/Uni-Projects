import matplotlib.pyplot as plt

# Square path in 3D meow
x = [0, 1, 1, 0, 0]
y = [0, 0, 1, 1, 0]
z = [0, 0, 0, 0, 0]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Square')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.show()
