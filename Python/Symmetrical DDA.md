# Symmetrical DDA Line Drawing

## 1. Imports and Setup
```python
import matplotlib.pyplot as plt
import numpy as np
import math
```
- **matplotlib.pyplot** — Used to draw the grid, points, and line.
- **numpy** — Helps generate grid ticks.
- **math** — Not directly used in this script, but often helpful for numerical operations.

---

## 2. Global Variables
```python
grid_size = 10
clicked_points = []
```
- **grid_size** — Size of the drawing grid in cells.
- **clicked_points** — Stores user-selected points (two clicks define a line).

---

## 3. Symmetrical DDA Function
```python
def symmetrical_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    k = 0
    while (1 << k) < steps:
        k += 1

    total_steps = 1 << k  # 2^k
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
```

### Key Steps:
1. **dx, dy** — Find differences in X and Y between the start and end points.
2. **steps** — Choose the maximum of `abs(dx)` and `abs(dy)`.
3. **Find next power of two**:
   ```python
   k = 0
   while (1 << k) < steps:
       k += 1
   total_steps = 1 << k
   ```
   - `(1 << k)` is a bit shift: `1 << k` = $(2^k)$.
   - Loop stops when $(2^k \ge steps)$.
   - Example: if `steps = 6`, smallest power of two ≥ 6 is 8.
4. **x_inc, y_inc** — How much X and Y change each step.
5. **Start from pixel center**: `(x1 + 0.5, y1 + 0.5)`.
6. **Loop** — Append integer pixel positions until the line is complete.

---

## 4. Plotting the Grid
```python
def plot_grid():
    plt.clf()
    ax = plt.gca()
    ax.set_xticks(np.arange(0, grid_size + 1, 1))
    ax.set_yticks(np.arange(0, grid_size + 1, 1))
    ax.grid(which='both', color='lightgray', linestyle='-', linewidth=0.5)
    ax.set_xlim(-1, grid_size)
    ax.set_ylim(-1, grid_size)
    ax.set_aspect('equal')
    ax.set_title("Click two points to draw a Symmetrical DDA line")

    for i, (x, y) in enumerate(clicked_points):
        plt.plot(x, y, 'bo', markersize=6)
        plt.text(x + 0.2, y + 0.2, f'P{i+1}', fontsize=9, color='blue')

    plt.draw()
```

**Purpose:**  
Draws the grid and any points clicked so far.

---

## 5. Handling Mouse Clicks
```python
def onclick(event):
    if event.xdata is None or event.ydata is None:
        return

    x = int(round(event.xdata))
    y = int(round(event.ydata))

    if 0 <= x < grid_size and 0 <= y < grid_size:
        clicked_points.append((x, y))
        plot_grid()

        if len(clicked_points) == 2:
            x1, y1 = clicked_points[0]
            x2, y2 = clicked_points[1]

            line_points = symmetrical_dda(x1, y1, x2, y2)

            for px, py in line_points:
                plt.plot(px, py, 'ro', markersize=4)

            xs, ys = zip(*line_points)
            plt.plot(xs, ys, 'r-', linewidth=1)

            plt.draw()
            clicked_points.clear()
```

**Purpose:**  
- On each mouse click, records the point.  
- When two points are selected, calls `symmetrical_dda()` and plots the result.

---

## 6. Program Start
```python
plt.figure(figsize=(8, 8))
plot_grid()
plt.connect('button_press_event', onclick)
plt.show()
```

---

## Example of Step Calculation
Let’s take `(2, 3)` to `(8, 7)`:

1. `dx = 6`, `dy = 4`, `steps = 6`
2. Find next power of two:
   - 1, 2, 4, **8** → stop (k = 3, total_steps = 8)
3. `x_inc = 6 / 8 = 0.75`
4. `y_inc = 4 / 8 = 0.5`
5. Start: `(2.5, 3.5)`
6. Generate points (int parts):  
   `(2,3) → (3,4) → (4,4) → (4,5) → (5,5) → (6,6) → (7,6) → (7,7) → (8,7)`


