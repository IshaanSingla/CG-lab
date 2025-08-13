import matplotlib.pyplot as plt
import numpy as np
import math

# Grid size
grid_size = 10
clicked_points = []

def symmetrical_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Calculate steps as next power of 2
    steps = max(abs(dx), abs(dy))
    k = 0
    while (1 << k) < steps:
        k += 1

    total_steps = 1 << k  # 2^k
    x_inc = dx / total_steps
    y_inc = dy / total_steps

    # Use virtual center of pixel
    x = x1 + 0.5
    y = y1 + 0.5
    points = []

    for _ in range(total_steps + 1):
        points.append((int(x), int(y)))  # Use int(x), int(y) to map to grid cell
        x += x_inc
        y += y_inc

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
    ax.set_title("Click two points to draw a Symmetrical DDA line")

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

            # Use symmetrical DDA
            line_points = symmetrical_dda(x1, y1, x2, y2)

            # Plot DDA points as red dots
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
