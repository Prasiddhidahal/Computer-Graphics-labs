import pygame
from pygame.locals import *
from OpenGL.GL import *
from math import cos, sin, radians

# Initial coordinates of the line in homogeneous coordinates
line = [[-0.5, -0.5, 1], [0.5, -0.5, 1]]
line1 = [[], []]
rotation_angle = 45  # degrees

def draw_line(line, color):
    glBegin(GL_LINES)
    glColor3f(color[0], color[1], color[2])  # Set line color
    glVertex2f(line[0][0] / line[0][2], line[0][1] / line[0][2])
    glVertex2f(line[1][0] / line[1][2], line[1][1] / line[1][2])
    glEnd()

def rotate(line, angle):
    angle_rad = radians(angle)
    rotation_matrix = [
        [cos(angle_rad), -sin(angle_rad), 0],
        [sin(angle_rad), cos(angle_rad), 0],
        [0, 0, 1]
    ]
    new_line = []
    for i in range(len(line)):
        x, y, w = line[i]
        new_coords = [
            rotation_matrix[0][0] * x + rotation_matrix[0][1] * y + rotation_matrix[0][2] * w,
            rotation_matrix[1][0] * x + rotation_matrix[1][1] * y + rotation_matrix[1][2] * w,
            rotation_matrix[2][0] * x + rotation_matrix[2][1] * y + rotation_matrix[2][2] * w
        ]
        new_line.append(new_coords)
    return new_line

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_line(line, [1.0, 1.0, 1.0])  # Original line in white
        line1 = rotate(line, rotation_angle)
        draw_line(line1, [1.0, 0.0, 0.0])  # Rotated line in red

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()