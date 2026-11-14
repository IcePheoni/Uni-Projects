import matplotlib
import math

#create graph
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plot1 = []
for n in range(3, 100):
    plot1.append(math.sqrt(n**4 + 3 * n**2) - math.sqrt(n**4 - 81))

plot2 = []
an = 1
for _ in range(150):
    an = math.sqrt(1 + an)
    plot2.append(an)
    print(an)



n_values_1 = range(3, 100)
n_values_2 = [0.01 * i for i in range(150)]
#plt.plot(n_values_1, plot1, marker='', linestyle='-')
#plt.plot(n_values_2, plot2, marker='', linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Convergence test')
plt.grid(True)
plt.show()

