import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define window boundaries
xmin, ymin = 50, 50
xmax, ymax = 150, 150

# Define a polygon
polygon = [
    (100, 75),
    (120, 100),
    (140, 75),
    (120, 50)
]

# Clip the polygon using Sutherland-Hodgman algorithm
def sutherland_hodgman_polygon_clip(polygon):
    output = polygon[:]
    sides = [
        (xmin, ymin, xmax, ymin),
        (xmax, ymin, xmax, ymax),
        (xmax, ymax, xmin, ymax),
        (xmin, ymax, xmin, ymin)
    ]

    for edge in sides:
        input_polygon = output[:]
        output = []

        (x1, y1), (x2, y2) = edge[0:2], edge[2:4]
        for i in range(len(input_polygon)):
            p1 = input_polygon[i]
            p2 = input_polygon[(i + 1) % len(input_polygon)]

            inside_p1 = (x2 - x1) * (p1[1] - y1) > (y2 - y1) * (p1[0] - x1)
            inside_p2 = (x2 - x1) * (p2[1] - y1) > (y2 - y1) * (p2[0] - x1)

            if inside_p1 and inside_p2:
                output.append(p2)
            elif inside_p1 and not inside_p2:
                intersection_x = x1 + (x2 - x1) * (y1 - p1[1]) / (p2[1] - p1[1])
                intersection_y = y1 + (y2 - y1) * (p1[0] - x1) / (x2 - x1)
                output.append((intersection_x, y1))
                output.append((p2[0], intersection_y))
            elif not inside_p1 and inside_p2:
                intersection_x = x1 + (x2 - x1) * (y1 - p1[1]) / (p2[1] - p1[1])
                intersection_y = y1 + (y2 - y1) * (p1[0] - x1) / (x2 - x1)
                output.append((intersection_x, y1))
        output = [p for p in output if p not in [(x1, y1), (x2, y2)]]

    return output

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    gluOrtho2D(0, 500, 0, 500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)  # Red color

        # Draw the polygon with red color
        glBegin(GL_POLYGON)
        for vertex in polygon:
            glVertex2f(*vertex)
        glEnd()

        # Draw the clipping window with green color
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(xmin, ymin)
        glVertex2f(xmax, ymin)
        glVertex2f(xmax, ymax)
        glVertex2f(xmin, ymax)
        glEnd()

        # Perform polygon clipping and draw the result
        clipped_polygon = sutherland_hodgman_polygon_clip(polygon)
        glColor3f(0.0, 0.0, 1.0)  # Blue color for clipped polygon
        glBegin(GL_POLYGON)
        for vertex in clipped_polygon:
            glVertex2f(*vertex)
        glEnd()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
