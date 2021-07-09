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


def drawTriangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(100, 300)
    glVertex2f(250, 400)
    glVertex2f(400, 300)
    glEnd()


def drawLine(sx, sy, ex, ey):
    glBegin(GL_LINES)
    glVertex2f(sx, sy)
    glVertex2f(ex, ey)
    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 0, 0)
    glPointSize(10)
    # call the draw methods here
    drawTriangle()

    # outer border
    drawLine(160, 300, 160, 100)
    drawLine(340, 300, 340, 100)
    drawLine(160, 100, 340, 100)
    drawLine(130, 70, 370, 70)
    drawLine(145, 85, 355, 85)
    drawLine(130, 70, 160, 100)
    drawLine(370, 70, 340, 100)

    # window 1 - quad
    drawLine(180, 270, 180, 230)
    drawLine(180, 270, 220, 270)
    drawLine(180, 230, 220, 230)
    drawLine(220, 270, 220, 230)

    # window 2 - quad
    drawLine(320, 270, 320, 230)
    drawLine(280, 270, 320, 270)
    drawLine(280, 230, 320, 230)
    drawLine(280, 270, 280, 230)

    # door
    drawLine(220, 100, 220, 200)
    drawLine(280, 100, 280, 200)
    drawLine(220, 200, 280, 200)

    # door-knob
    glBegin(GL_POINTS)
    glVertex2f(265, 150)
    glEnd()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 02 - 19101414")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
