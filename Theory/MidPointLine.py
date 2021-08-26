def midpoint(sx, sy, ex, ey):
    dy = ey-sy
    dx = ex-sx

    d_init = (2*dy) - dx
    d = d_init

    if sx == ex:
        while(sy != ey):
            print('(' + str(sx) + ', ' + str(sy) + ')')
            sy += 1
        print('(' + str(sx) + ', ' + str(sy) + ')')
    elif sy == ey:
        while(sx != ex):
            print('(' + str(sx) + ', ' + str(sy) + ')')
            sx += 1
        print('(' + str(sx) + ', ' + str(sy) + ')')
    else:
        while(sx != ex and sy != ey):
            print('(' + str(sx) + ', ' + str(sy) + ')')
            if d > 0:
                sx += 1
                sy += 1
                d += 2*(dy - dx)
            else:
                sx += 1
                d += 2*dy
        print('(' + str(sx) + ', ' + str(sy) + ')')


if __name__ == '__main__':
    sx, sy = map(int, input("Starting Point: ").split())
    ex, ey = map(int, input("Ending Point: ").split())
    # if (ey-sy)/(ex-sx) < 1 and (ey-sy)/(ex-sx) >= 0:
    midpoint(sx, sy, ex, ey)
    # else:
    # print('slope not between 1 and 0.')
