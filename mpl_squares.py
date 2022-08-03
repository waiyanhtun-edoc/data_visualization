from shutil import which
from matplotlib import cm
import matplotlib.pyplot as plt


# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = range(1,5)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-darkgrid')
plt.style.use('dark_background')

fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
ax.scatter(x_values, y_values, c='Blue', s=20)


#Set the chart title name
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=18)
ax.set_ylabel("Square of Value", fontsize=18)

# #Set size of tick label
# ax.tick_params(axis='both',which='major', labelsize=10)
#Set the range for each axis.
ax.axis([0,10,0,100])
plt.show()
