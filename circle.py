import pygame
from OpenGL.GL import *

class CircleDrawer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.radius = 200  # Set default radius
        pygame.init()
        pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
        glOrtho(-width/2, width/2, -height/2, height/2, -1, 1)

    def draw_circle(self):
        glBegin(GL_POINTS)
        x = 0
        y = self.radius
        d = 1 - self.radius
        while x <= y:
            glVertex2f(x, y)
            glVertex2f(-x, y)
            glVertex2f(x, -y)
            glVertex2f(-x, -y)
            glVertex2f(y, x)
            glVertex2f(-y, x)
            glVertex2f(y, -x)
            glVertex2f(-y, -x)
            if d < 0:
                d += 2 * x + 3
            else:
                d += 2 * (x - y) + 5
                y -= 1
            x += 1
        glEnd()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            glClear(GL_COLOR_BUFFER_BIT)
            glColor3f(1.0, 1.0, 1.0)
            glPointSize(2.0)
            self.draw_circle()
            pygame.display.flip()
        pygame.quit()

def main():
    drawer = CircleDrawer(500, 600)
    drawer.run()

if __name__ == "__main__":
    main()
