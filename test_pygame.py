import pygame
from pygame.locals import *
from OpenGL.GL import *  # ✅ This imports glClearColor, glClear, etc.

def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClearColor(0.1, 0.2, 0.3, 1.0)  # ✅ Set clear color
        glClear(GL_COLOR_BUFFER_BIT)     # ✅ Clear the screen

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
