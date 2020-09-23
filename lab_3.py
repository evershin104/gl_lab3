from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
# Func for window
def changeSize(w, h):
    if h == 0:
        h = 1
    ratio = w * 1.0 / h
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, w, h)
    gluPerspective(45, ratio, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)

# Renders scene with pyramid and cube
def renderScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # gluLookAt(0, -8, 5, 0, 0, 0, 0, -1, 0)
    gluLookAt(17, 0, 14, 0, 0, 3.5, -1, 0, 2)
    cylinder()
    glutSwapBuffers()


def cylinder():
    radius = 4.5
    h = 7
    # number_of_slices
    n = 30
    # Init list of circle points
    circle_pts = []
    for i in range(0, n + 1):
        angle = 2 * math.pi * i / n
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)

    # Draw the upper circle
    glBegin(GL_TRIANGLE_FAN)
    # Center
    glColor(0, 0, 1)
    glVertex(0, 0, h)
    for (x, y) in circle_pts:
        z = h
        glColor(1, 0, 0)
        glVertex(x, y, z)
    glEnd()

    # Draw the lower circle
    glBegin(GL_TRIANGLE_FAN)
    glColor(1, 0, 0)
    # Center
    glVertex(0, 0, 0)
    for (x, y) in circle_pts:
        glVertex(x, y, 0)
    glEnd()

    # Draw the tube
    glBegin(GL_TRIANGLE_STRIP)
    glColor(0, 1, 0)
    for (x, y) in circle_pts:
        glColor(1, 1, 0)
        glVertex(x, y, h)
        glColor(0, 1, 0)
        glVertex(x, y, 0)
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
