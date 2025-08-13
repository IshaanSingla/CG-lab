import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')

# Grid size
grid_size = 10
clicked_points = []


def bresenham_decision(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1

    if dy <= dx:
        p = 2 * dy - dx
        for _ in range(dx):
            points.append((x, y))
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * (dy - dx)
            x += sx
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            points.append((x, y))
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * (dx - dy)
            y += sy

    points.append((x, y))
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
    ax.set_title("Click two points to draw a Bresenham line (Decision Parameter)")

    # Re-plot previously clicked points
    for i, (x, y) in enumerate(clicked_points):
        plt.plot(x, y, 'bo', markersize=6)
        plt.text(x + 0.2, y + 0.2, f'P{i + 1}', fontsize=9, color='blue')

    plt.draw()


def onclick(event):
    if event.xdata is None or event.ydata is None:
        return

    x = int(round(event.xdata))
    y = int(round(event.ydata))

    if 0 <= x < grid_size and 0 <= y < grid_size:
        clicked_points.append((x, y))
        print(f"Clicked: ({x}, {y})")

        plot_grid()

        if len(clicked_points) == 2:
            x1, y1 = clicked_points[0]
            x2, y2 = clicked_points[1]

            line_points = bresenham_decision(x1, y1, x2, y2)

            for px, py in line_points:
                plt.plot(px, py, 'ro', markersize=4)

            xs, ys = zip(*line_points)
            plt.plot(xs, ys, 'r-', linewidth=1)

            plt.draw()
            clicked_points.clear()


plt.figure(figsize=(8, 8))
plot_grid()
plt.connect('button_press_event', onclick)
plt.show()
