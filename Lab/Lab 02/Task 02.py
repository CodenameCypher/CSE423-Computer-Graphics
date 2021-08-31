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


# method to find zone - eight way symmetry begins from here
def findZone(sx, sy, ex, ey):
    dx = ex - sx
    dy = ey - sy
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 'zone 0'
        elif dx < 0 and dy > 0:
            return'zone 3'
        elif dx < 0 and dy < 0:
            return'zone 4'
        elif dx > 0 and dy < 0:
            return'zone 7'
    else:
        if dx >= 0 and dy >= 0:
            return'zone 1'
        elif dx < 0 and dy > 0:
            return'zone 2'
        elif dx < 0 and dy < 0:
            return'zone 5'
        elif dx > 0 and dy < 0:
            return'zone 6'


# method to map any point to zone 0
def convertToZone0(x, y, sourceZone):
    if sourceZone == 'zone 1':
        rx = y
        ry = x
        return (rx, ry)
    elif sourceZone == 'zone 2':
        rx = y
        ry = (-1) * x
        return (rx, ry)
    elif sourceZone == 'zone 3':
        rx = (-1)*x
        ry = y
        return (rx, ry)
    elif sourceZone == 'zone 4':
        rx = (-1)*x
        ry = (-1)*y
        return (rx, ry)
    elif sourceZone == 'zone 5':
        rx = (-1)*y
        ry = (-1)*x
        return (rx, ry)
    elif sourceZone == 'zone 6':
        rx = (-1)*y
        ry = x
        return (rx, ry)
    elif sourceZone == 'zone 7':
        rx = x
        ry = (-1)*y
        return (rx, ry)


# method to map zone 0 point to any other zone
def convertToOriginal(x, y, destinationZone):
    if destinationZone == 'zone 1':
        rx = y
        ry = x
        return (rx, ry)
    elif destinationZone == 'zone 2':
        rx = (-1) * y
        ry = x
        return (rx, ry)
    elif destinationZone == 'zone 3':
        rx = (-1)*x
        ry = y
        return (rx, ry)
    elif destinationZone == 'zone 4':
        rx = (-1)*x
        ry = (-1)*y
        return (rx, ry)
    elif destinationZone == 'zone 5':
        rx = (-1)*y
        ry = (-1)*x
        return (rx, ry)
    elif destinationZone == 'zone 6':
        rx = y
        ry = (-1)*x
        return (rx, ry)
    elif destinationZone == 'zone 7':
        rx = x
        ry = (-1)*y
        return (rx, ry)


# midpoint algo
def midpoint(sx, sy, ex, ey):
    dy = ey-sy
    dx = ex-sx

    d_init = (2*dy) - dx
    d = d_init

    points = []
    if sx == ex:
        while(sy != ey):
            points.append((sx, sy))
            sy += 1
    elif sy == ey:
        while(sx != ex):
            points.append((sx, sy))
            sx += 1
    else:
        while(sx != ex and sy != ey):
            points.append((sx, sy))
            if d > 0:
                sx += 1
                sy += 1
                d += 2*(dy - dx)
            else:
                sx += 1
                d += 2*dy
    points.append((ex, ey))
    return points


def drawLine(sx, sy, ex, ey):
    glBegin(GL_POINTS)
    zone = findZone(sx, sy, ex, ey)

    if zone == 'zone 0':
        points = midpoint(sx, sy, ex, ey)
        for point in points:
            glVertex2f(point[0], point[1])
    else:
        startingPointsConverted = convertToZone0(sx, sy, zone)
        endingPointConverted = convertToZone0(ex, ey, zone)
        points = midpoint(
            startingPointsConverted[0], startingPointsConverted[1], endingPointConverted[0], endingPointConverted[1])
        for (x, y) in points:
            original = convertToOriginal(x, y, zone)
            glVertex2f(original[0], original[1])
    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 1, 0)
    glPointSize(5)

    # outer border
    drawLine(200, 100, 450, 100)
    drawLine(200, 100, 200, 400)
    drawLine(450, 100, 450, 400)

    # hood
    drawLine(150, 400, 500, 400)
    drawLine(150, 400, 325, 500)
    drawLine(325, 500, 500, 400)

    # door
    drawLine(280, 100, 280, 250)
    drawLine(370, 100, 370, 250)
    drawLine(280, 250, 370, 250)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 750)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 02 - 19101414")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
