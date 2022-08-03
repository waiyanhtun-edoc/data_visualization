import matplotlib.pyplot as plt

from random_wall import RandomWalk

#Keep Making new walks, as long as the program is active
while True:

    #Make the random walk
    rw = RandomWalk()
    rw.fill_walk()

    #Plot the points in the walk
    plt.style.use('seaborn-dark-palette')
    fig , ax = plt.subplots()
    points_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=points_number, cmap=plt.cm.Blues ,
                edgecolors='none',s=15)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)
    plt.show()

    keep_running = input ("Make another walk? (y/n):")
    if keep_running == 'n':
        break