from random import choice as random
from sys import setrecursionlimit
from math import fabs as modul

import easyend

setrecursionlimit(100000)
way = {}

def maze(x, y, lenght, high):
    a = [0, 1, 2, 3]
    while len(a):
        b = random(a)
        a.remove(b)
# a[0] == x + 1
        if b == 0:
            if x + 1 < lenght and way.get((x + 1, y)) == None:
                way.setdefault((x, y), []).append((x + 1, y))
                maze(x + 1, y, lenght, high)
# a[1] == x - 1
        if b == 1:
            if x - 1 >= 0 and way.get((x - 1, y)) == None:
                way.setdefault((x, y), []).append((x - 1, y))
                maze(x - 1, y, lenght, high)
# a[2] == y + 1
        if b == 2:
            if y + 1 < high and way.get((x, y + 1)) == None:
                way.setdefault((x, y), []).append((x, y + 1))
                maze(x, y + 1, lenght, high)
# a[3] == y - 1
        if b == 3:
            if y - 1 >= 0 and way.get((x, y - 1)) == None:
                way.setdefault((x, y), []).append((x, y - 1))
                maze(x, y - 1, lenght, high)
        if len(a) == 0:
            if way.get((x, y)) == None:
                way[(x, y)] = "Stop!"
    return way


def trans(x, y, lenght, high, koef, plus, plusx, plusy):

    #maze (x, y, lenght, high)
    a = []
    keys = way.keys()
    for key in keys:
        if type(way[key]) == list:
            for value in way[key]:
                b = []
                b.extend(list(key))
                b.extend(list(value))
                a.append(b)
        else:
            b = []
            b.extend(list(key))
            b.extend(list(key))
            a.append(b)
    for i in range(len(a)):
        a[i] = [x * koef + plus for x in a[i]] #кожен х + 9, y + 16

    a = [(x[0] + plusx, x[1] + plusy, x[2] + plusx, x[3] + plusy) for x in a]
    return a

def chose_final(koef, plus, plusx, plusy):
    b = [] #список з ключів "тупіків"
    keys = way.keys()
    for key in keys: #перебирає всі ключі з way
        if way[key] == "Stop!": #вибирає з них тільки ті, які зайшли в тупік
            b.append(key) #додає в б ключ, який зайшов в тупік
    c = random(b)
    c = (c[0] * koef + plusx + plus, c[1] * koef + plusy + plus)
    return tuple(c)

def dotway(c):

    dots = []

    for x in c:
        if x[0] == x[2] and x[1] != x[3]:
            dots.append((x[0], x[1]))
            dots.append((x[0], modul(x[1] - x[3]) / 5 + min(x[1], x[3])))
            dots.append((x[0], modul(x[1] - x[3]) / 5 * 2 + min(x[1], x[3])))
            dots.append((x[0], modul(x[1] - x[3]) / 5 * 3 + min(x[1], x[3])))
            dots.append((x[0], modul(x[1] - x[3]) / 5 * 4 + min(x[1], x[3])))
            dots.append((x[2], x[3]))

        if x[1] == x[3] and x[0] != x[2]:
            dots.append((x[0], x[1]))
            dots.append((modul(x[0] - x[2]) / 5 + min(x[0], x[2]), x[1]))
            dots.append((modul(x[0] - x[2]) / 5 * 2 + min(x[0], x[2]), x[1]))
            dots.append((modul(x[0] - x[2]) / 5 * 3 + min(x[0], x[2]), x[1]))
            dots.append((modul(x[0] - x[2]) / 5 * 4 + min(x[0], x[2]), x[1]))
            dots.append((x[2], x[3]))

    return dots

x_dict = {}

def x_dict_gen(mazea):

    for point in mazea:
        if point[0] not in x_dict.keys():
            x_dict[point[0]] = None

    for dot in dotway(mazea):
        if dot[0] in x_dict.keys():
            if x_dict[dot[0]] == None:
                x_dict[dot[0]] = [dot]
            elif dot not in x_dict[dot[0]]:
                x_dict[dot[0]].append(dot)
    return x_dict

y_dict = {}

def y_dict_gen(mazea):
    for point in mazea:
        if point[1] not in y_dict.keys():
            y_dict[point[1]] = None

    for dot in dotway(mazea):
        if dot[1] in y_dict.keys():
            if y_dict[dot[1]] == None:
                y_dict[dot[1]] = [dot]
            elif dot not in y_dict[dot[1]]:
                y_dict[dot[1]].append(dot)
    return y_dict

#def y_dict(c):
    #f = {}
    #for i in recmaze.dotway(easy.a):
    #    if i[1] not in f.keys():
   #         f[i[1]] = [i]
    #    elif i[1] in f.keys():
  #          f[i[1]].append(i)
   # return f

