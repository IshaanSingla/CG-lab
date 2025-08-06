import glfw
from OpenGL.GL import *
import numpy as np

def main():
    # Initialize GLFW
    if not glfw.init():
        raise Exception("GLFW can't be initialized")

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "OpenGL with GLFW", None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window can't be created")

    # Make the window's context current
    glfw.make_context_current(window)

    # Set up the triangle vertices
    triangle = np.array([
        [-0.6, -0.4, 0.0],
        [ 0.6, -0.4, 0.0],
        [ 0.0,  0.6, 0.0]
    ], dtype=np.float32)

    # Main loop
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)  # Red
        glVertex3f(*triangle[0])
        glColor3f(0.0, 1.0, 0.0)  # Green
        glVertex3f(*triangle[1])
        glColor3f(0.0, 0.0, 1.0)  # Blue
        glVertex3f(*triangle[2])
        glEnd()

        glfw.swap_buffers(window)

    # Clean up
    glfw.terminate()

if __name__ == "__main__":
    main()
