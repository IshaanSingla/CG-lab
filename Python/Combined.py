import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
# Grid size
grid_size = 30
clicked_points = []

def simple_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return [(x1, y1)]
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    points = []
    for _ in range(int(steps) + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    return points

def symmetrical_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    k = 0
    while (1 << k) < steps:
        k += 1
    total_steps = 1 << k  # next power of 2
    x_inc = dx / total_steps
    y_inc = dy / total_steps
    x = x1 + 0.5
    y = y1 + 0.5
    points = []
    for _ in range(total_steps + 1):
        points.append((int(x), int(y)))
        x += x_inc
        y += y_inc
    return points

def bresenham(x1, y1, x2, y2):
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
        points.append((x, y))
    else:
        err = dy // 2
        while y != y2:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
        points.append((x, y))
    return points

def plot_grid():
    plt.clf()
    ax = plt.gca()
    ax.set_xticks(np.arange(0, grid_size + 1, 1))
    ax.set_yticks(np.arange(0, grid_size + 1, 1))
    ax.grid(True, color='lightgray', linestyle='-', linewidth=0.5)
    ax.set_xlim(-1, grid_size)
    ax.set_ylim(-1, grid_size)
    ax.set_aspect('equal')
    ax.set_title("Click two points to draw lines using DDA, Symmetrical DDA & Bresenham")

    # Plot clicked points
    for i, (x, y) in enumerate(clicked_points):
        plt.plot(x, y, 'ko', markersize=7)
        plt.text(x + 0.2, y + 0.2, f'P{i+1}', fontsize=10, color='black')

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

            # Compute points for all algorithms
            dda_points = simple_dda(x1, y1, x2, y2)
            sym_dda_points = symmetrical_dda(x1, y1, x2, y2)
            bres_points = bresenham(x1, y1, x2, y2)

            # Plot points for each algorithm with different colors
            for px, py in dda_points:
                plt.plot(px, py, 'bo', markersize=5, label='Simple DDA')
            for px, py in sym_dda_points:
                plt.plot(px, py, 'ro', markersize=4, label='Symmetrical DDA')
            for px, py in bres_points:
                plt.plot(px, py, 'go', markersize=3, label='Bresenham')

            # Connect points with lines for each algorithm
            dda_xs, dda_ys = zip(*dda_points)
            sym_xs, sym_ys = zip(*sym_dda_points)
            bres_xs, bres_ys = zip(*bres_points)

            plt.plot(dda_xs, dda_ys, 'b-', linewidth=1)
            plt.plot(sym_xs, sym_ys, 'r-', linewidth=1)
            plt.plot(bres_xs, bres_ys, 'g-', linewidth=1)

            # To avoid duplicate legend entries, create custom legend
            from matplotlib.lines import Line2D
            legend_elements = [
                Line2D([0], [0], marker='o', color='w', label='Simple DDA', markerfacecolor='blue', markersize=7),
                Line2D([0], [0], marker='o', color='w', label='Symmetrical DDA', markerfacecolor='red', markersize=7),
                Line2D([0], [0], marker='o', color='w', label='Bresenham', markerfacecolor='green', markersize=7)
            ]
            plt.legend(handles=legend_elements, loc='upper left')

            plt.draw()
            clicked_points.clear()

# Setup plot
plt.figure(figsize=(8, 8))
plot_grid()
plt.connect('button_press_event', onclick)
plt.show()
