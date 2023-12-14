import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_ellipse(rx, ry, xc, yc):
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
    gluOrtho2D(-width / 2, width / 2, -height / 2, height / 2)

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glPointSize(1)

    clock = pygame.time.Clock()
    running = True

    x = 0
    y = ry
    a_sqr = rx * rx
    b_sqr = ry * ry
    a_sqr2 = a_sqr * 2
    b_sqr2 = b_sqr * 2
    p10 = b_sqr + a_sqr * 0.25 - a_sqr * ry

    while 2 * b_sqr * x <= 2 * a_sqr * y:
        glBegin(GL_POINTS)
        glVertex2f(x + xc, y + yc)
        glVertex2f(-x + xc, y + yc)
        glVertex2f(x + xc, -y + yc)
        glVertex2f(-x + xc, -y + yc)
        glEnd()

        x += 1
        if p10 < 0:
            p10 += b_sqr2 * x + b_sqr
        else:
            y -= 1
            p10 += b_sqr2 * x - a_sqr2 * y + b_sqr

    p20 = b_sqr * (x + 0.5) * (x + 0.5) + a_sqr * (y - 1) * (y - 1) - a_sqr * b_sqr

    while y >= 0:
        glBegin(GL_POINTS)
        glVertex2f(x + xc, y + yc)
        glVertex2f(-x + xc, y + yc)
        glVertex2f(x + xc, -y + yc)
        glVertex2f(-x + xc, -y + yc)
        glEnd()

        y -= 1
        if p20 > 0:
            p20 += a_sqr - a_sqr2 * y
        else:
            x += 1
            p20 += b_sqr2 * x - a_sqr2 * y + a_sqr

    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    rx = 100  # Radius along x axis
    ry = 150  # Radius along y axis
    xc = 100   # x coordinate of center
    yc = 100   # y coordinate of center
    draw_ellipse(rx, ry, xc, yc)
