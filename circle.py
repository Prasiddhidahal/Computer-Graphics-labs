import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def midPointCircleDraw(x_centre, y_centre, r):
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
    gluOrtho2D(-width / 2, width / 2, -height / 2, height / 2)

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glPointSize(1)

    x = r
    y = 0
    P = 1 - r

    clock = pygame.time.Clock()
    running = True

    while x > y:
        glBegin(GL_POINTS)
        glVertex2f(x + x_centre, y + y_centre)
        glVertex2f(-x + x_centre, y + y_centre)
        glVertex2f(x + x_centre, -y + y_centre)
        glVertex2f(-x + x_centre, -y + y_centre)
        glEnd()

        y += 1
        if P <= 0:
            P += 2 * y + 1
        else:
            x -= 1
            P += 2 * y - 2 * x + 1

        if x < y:
            break

        glBegin(GL_POINTS)
        glVertex2f(x + x_centre, y + y_centre)
        glVertex2f(-x + x_centre, y + y_centre)
        glVertex2f(x + x_centre, -y + y_centre)
        glVertex2f(-x + x_centre, -y + y_centre)
        glEnd()

        if x != y:
            glBegin(GL_POINTS)
            glVertex2f(y + x_centre, x + y_centre)
            glVertex2f(-y + x_centre, x + y_centre)
            glVertex2f(y + x_centre, -x + y_centre)
            glVertex2f(-y + x_centre, -x + y_centre)
            glEnd()

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    # To draw a circle of radius 3 centered at (0, 0)
    midPointCircleDraw(100, 100, 130)

