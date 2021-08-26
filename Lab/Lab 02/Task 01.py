from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def midpoint(sx, sy, ex, ey):
    glBegin(GL_POINTS)
    dy = ey-sy
    dx = ex-sx

    d_init = (2*dy) - dx
    d = d_init

    if sx == ex:
        while(sy != ey):
            glVertex2f(sx, sy)
            sy += 1
        glVertex2f(sx, sy)
    elif sy == ey:
        while(sx != ex):
            glVertex2f(sx, sy)
            sx += 1
        glVertex2f(sx, sy)
    else:
        while(sx != ex and sy != ey):
            glVertex2f(sx, sy)
            if d > 0:
                sx += 1
                sy += 1
                d += 2*(dy - dx)
            else:
                sx += 1
                d += 2*dy
        glVertex2f(sx, sy)
    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 1, 0)
    glPointSize(5)

    midpoint(350, 300, 350, 500)
    midpoint(300, 300, 400, 300)
    midpoint(300, 450, 350, 500)

    midpoint(500, 300, 500, 500)
    midpoint(400, 400, 500, 400)
    midpoint(400, 400, 500, 500)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 750)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 01 - 19101414")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
