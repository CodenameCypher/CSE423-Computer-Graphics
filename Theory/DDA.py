def dda(sx, sy, ex, ey):
    try:
        m = (ey-sy)/(ex-sx)  # calculating the scope
    except:
        m = 2e18  # calculating the scope

    if m < 1 and m > -1:  # check if the line is steep
        while(sx != ex):
            print('(' + str(sx) + ', ' + str(round(sy)) + ')')
            sx = sx + 1
            sy = sy + m
    else:
        while(sy != ey):
            print('(' + str(round(sx)) + ', ' + str(sy) + ')')
            sy = sy + 1
            sx = sx + (1/m)
    print('(' + str(ex) + ', ' + str(ey) + ')')


if __name__ == '__main__':
    sx, sy = map(int, input("Starting Point: ").split())
    ex, ey = map(int, input("Ending Point: ").split())

    dda(sx, sy, ex, ey)
