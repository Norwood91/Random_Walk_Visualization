from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """This class generates random walks"""
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # Walks start at (0, 0) = (x, y) coordinates
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""
        # Keep taking steps until the walk reaches 5000 steps, then the while loop will break
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """Returns a step in the random walk"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step


while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    # Fig represents the entire figure or collection of plots generated
    # Ax represents a single plot in the figure
    # Figsize changes the size of the figure, it takes a tuple
    fig, ax = plt.subplots(figsize=(16, 9))

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input('Would you like to make another walk? (Y/N): ').upper()

    if keep_running == 'N':
        break