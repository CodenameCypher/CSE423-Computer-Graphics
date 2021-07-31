global x_min, y_min, x_max, y_max


def outcode(x, y):
    bit0 = ''
    bit1 = ''
    bit2 = ''
    bit3 = ''
    if x < x_min:
        bit0 = 1
    else:
        bit0 = 0
    if x > x_max:
        bit1 = 1
    else:
        bit1 = 0
    if y < y_min:
        bit2 = 1
    else:
        bit2 = 0
    if y > y_max:
        bit3 = 1
    else:
        bit3 = 0
    code = str(bit3)+str(bit2)+str(bit1)+str(bit0)
    return code


def convertBinaryToDecimal(s):
    n = int(s)
    decimalNumber = 0
    i = 0
    remainder = None
    while(n != 0):
        remainder = n % 10
        n /= 10
        decimalNumber += remainder*pow(2, i)
        i += 1
    return int(decimalNumber)


def cohen(x1, y1, x2, y2):
    oc1 = outcode(x1, y1)
    oc2 = outcode(x2, y2)
    m = (y2-y1)/(x2-x1)
    print("m", m)
    x_1 = x1
    y_1 = y1
    x_2 = x2
    y_2 = y2
    while(True):
        dec1 = convertBinaryToDecimal(oc1)
        dec2 = convertBinaryToDecimal(oc2)
        print(oc1, ' ', oc2)
        if oc1 == oc2 and oc1 == "0000":
            print(x_1, " ", y_1, " , ", x_2, " ", y_2)
            break
        elif((dec1 & dec2) != 0):
            print("point completely outside")
            break
        else:
            x = x1, y = y1
            if(oc1 != "0000"):
                if(oc1[0] == '1'):
                    y = y_max
                    x = round(x1 + 1/m*(y_max - y1))
                elif(oc1[1] == '1'):
                    y = y_min
                    x = round(x1 + 1/m*(y_min - y1))
                elif(oc1[2] == '1'):
                    x = x_max
                    y = round(y1 + m*(x_max - x1))
                elif(oc1[3] == '1'):
                    x = x_min
                    y = round(y1+m*(x_min-x1))
                oc1 = outcode(x, y)
                x_1 = x
                y_1 = y

            elif(oc2 != "0000"):
                x = x1, y = y1
                if(oc2[0] == '1'):
                    y = y_max
                    x = round(x2 + 1/m*(y_max - y2))
                elif(oc2[1] == '1'):
                    y = y_min
                    x = round(x2 + 1/m*(y_min - y2))
                elif(oc2[2] == '1'):
                    x = x_max
                    y = round(y2 + m*(x_max - x2))
                elif(oc2[3] == '1'):
                    x = x_min
                    y = round(y2+m*(x_min-x2))
                oc2 = outcode(x, y)
                x_2 = x
                y_2 = y

            print(x_1, " ", y_1, " , ", x_2, " ", y_2)
        continue


if __name__ == "__main__":
    x_min, y_min = map(int, input("X Y Min Points:").split())
    x_max, y_max = map(int, input("X Y Max Points:").split())

    x1, y1 = map(int, input("Line Starting:").split())
    x2, y2 = map(int, input("Line Ending:").split())

    cohen(x1, y1, x2, y2)
