# Simple DDA Line Drawing Interactive

## 1. Imports and Setup
```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
```
- **matplotlib.pyplot** — Used for plotting the grid and points.
- **numpy** — Helps with creating coordinate ticks for the grid.
- `matplotlib.use('TkAgg')` — Ensures an interactive backend for mouse click events.

---

## 2. Global Variables
```python
grid_size = 10
clicked_points = []
```
- **grid_size** — Defines the number of squares along each axis of the grid.
- **clicked_points** — Stores the coordinates of points clicked by the user.

---

## 3. The DDA Function
```python
def dda(x1, y1, x2, y2):
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
```
**Purpose:**  
Implements the **DDA algorithm** to find all intermediate pixel/grid coordinates between `(x1, y1)` and `(x2, y2)`.

**Key Steps:**
1. Calculate `dx` and `dy`.
2. Determine `steps` — the number of iterations needed (based on the larger of |dx| or |dy|).
3. Find **increments** `x_inc` and `y_inc` to add in each step.
4. Loop for `steps + 1` times, rounding coordinates to the nearest grid point.
5. Append each point to the list and return.

---

## 4. Drawing the Grid
```python
def plot_grid():
    plt.clf()
    ax = plt.gca()
    ax.set_xticks(np.arange(0, grid_size + 1, 1), minor=False)
    ax.set_yticks(np.arange(0, grid_size + 1, 1), minor=False)
    ax.grid(which='both', color='lightgray', linestyle='-', linewidth=0.5)
    ax.set_xlim(-1, grid_size)
    ax.set_ylim(-1, grid_size)
    ax.set_aspect('equal')
    ax.set_title("Click two points to draw a DDA line")

    for i, (x, y) in enumerate(clicked_points):
        plt.plot(x, y, 'bo', markersize=6)
        plt.text(x + 0.2, y + 0.2, f'P{i+1}', fontsize=9, color='blue')

    plt.draw()
```
**Purpose:**  
Creates a visual grid and plots any points clicked so far.

**Key Points:**
- `plt.clf()` clears the previous frame before redrawing.
- **Ticks** are set at integer positions to align with grid cells.
- **Blue dots** show clicked points with labels (`P1`, `P2`).
- The grid has equal aspect ratio to avoid distortion.

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
        print(f"Clicked: ({x}, {y})")

        plot_grid()

        if len(clicked_points) == 2:
            x1, y1 = clicked_points[0]
            x2, y2 = clicked_points[1]

            line_points = dda(x1, y1, x2, y2)

            for px, py in line_points:
                plt.plot(px, py, 'ro', markersize=4)

            xs, ys = zip(*line_points)
            plt.plot(xs, ys, 'r-', linewidth=1)

            plt.draw()
            clicked_points.clear()
```
**Purpose:**  
Captures the user's mouse click, processes coordinates, and when two points are selected, runs the DDA algorithm to draw the line.

**Key Points:**
1. Ignores clicks outside the axes.
2. Rounds clicked coordinates to nearest integer grid cell.
3. Adds the point to `clicked_points`.
4. Once two points are available:
   - Calls **`dda()`** to get intermediate points.
   - Plots each intermediate point as a **red dot**.
   - Connects them with a **red line**.
   - Clears `clicked_points` to allow new input.

---

## 6. Program Initialization
```python
plt.figure(figsize=(8, 8))
plot_grid()
plt.connect('button_press_event', onclick)
plt.show()
```
**Purpose:**  
Starts the interactive plotting window.

**Key Points:**
- Sets figure size.
- Draws initial empty grid.
- **`plt.connect()`** binds mouse click events to `onclick()`.
- **`plt.show()`** displays the interactive window.

---

## Summary of Flow
1. **User clicks** → Coordinates are recorded.
2. **Two points clicked** → DDA calculates intermediate points.
3. **Line drawn** → Grid is updated visually.
4. **Cycle repeats**.