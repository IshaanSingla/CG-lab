import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# Grid size
grid_size = 10
clicked_points = []

def bresenham(x1, y1, x2, y2):
    """Return list of grid intersection points the Bresenham line passes through."""
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1

    if dy <= dx:
        err = dx // 2
        while x != x2:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
        points.append((x, y))  # add last point
    else:
        err = dy // 2
        while y != y2:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
        points.append((x, y))  # add last point

    return points

def plot_grid():
    plt.clf()
    ax = plt.gca()
    ax.set_xticks(np.arange(0, grid_size + 1, 1), minor=False)
    ax.set_yticks(np.arange(0, grid_size + 1, 1), minor=False)
    ax.grid(which='both', color='lightgray', linestyle='-', linewidth=0.5)
    ax.set_xlim(-1, grid_size)
    ax.set_ylim(-1, grid_size)
    ax.set_aspect('equal')
    ax.set_title("Click two points to draw a Bresenham line")

    # Re-plot previously clicked points
    for i, (x, y) in enumerate(clicked_points):
        plt.plot(x, y, 'bo', markersize=6)
        plt.text(x + 0.2, y + 0.2, f'P{i+1}', fontsize=9, color='blue')

    plt.draw()

def onclick(event):
    if event.xdata is None or event.ydata is None:
        return

    x = int(round(event.xdata))
    y = int(round(event.ydata))

    if 0 <= x < grid_size and 0 <= y < grid_size:
        clicked_points.append((x, y))
        print(f"Clicked: ({x}, {y})")

        plot_grid()  # update plot with new point

        if len(clicked_points) == 2:
            x1, y1 = clicked_points[0]
            x2, y2 = clicked_points[1]

            # Get Bresenham points
            line_points = bresenham(x1, y1, x2, y2)

            # Plot Bresenham points as red dots
            for px, py in line_points:
                plt.plot(px, py, 'ro', markersize=4)

            # Connect them with lines
            xs, ys = zip(*line_points)
            plt.plot(xs, ys, 'r-', linewidth=1)

            plt.draw()
            clicked_points.clear()

# Setup plot
plt.figure(figsize=(8, 8))
plot_grid()
plt.connect('button_press_event', onclick)
plt.show()
