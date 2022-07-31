from shutil import which
import matplotlib.pyplot as plt


# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 2]

plt.style.use('seaborn-darkgrid')
plt.style.use('dark_background')

fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
ax.scatter(2,4, s=200)


#Set the chart title name
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=18)
ax.set_ylabel("Square of Value", fontsize=18)

#Set size of tick label
ax.tick_params(axis='both',which='major', labelsize=10)

plt.show()
