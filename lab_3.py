import pygame
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Draws cylinder with slices
def draw_cylinder(radius, height, num_slices):
    r = radius
    h = height
    n = float(num_slices)

    circle_pts = []
    for i in range(int(n) + 1):
        angle = 2 * math.pi * (i/n)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)

    glBegin(GL_TRIANGLE_FAN)#drawing the back circle
    glColor(1, 0, 0)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)#drawing the front circle
    glColor(0, 0, 1)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = -h/2.0
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)#draw the tube
    glColor(0, 1, 0)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
        glVertex(x, y, -z)
    glEnd()

glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowPosition(10, 10)
glutInitWindowSize(900, 600)
window = glutCreateWindow("OpenGL")
glutDisplayFunc(renderScene)
glutReshapeFunc(changeSize)
glEnable(GL_DEPTH_TEST)
glutMainLoop()
rotation = 0.0

while True:
    rotation += 1.0
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, float(width)/height, 1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -50)#move back far enough to see this object 
    glRotate(rotation, 0, 0, 0)#NOTE: this is applied BEFORE the translation due to OpenGL multiply order

    draw_cylinder(5, 10, 20)
    pygame.display.flip()
    clock.tick(60)