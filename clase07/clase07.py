#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
temp = []
final = []
a = text.split('&')

# capitalize
for i in a:
    b = i.capitalize()
    final.append(b)

# add dots
for i in range(len(final)):
    if i == 0:
        b = final[i].split()
        b.append('...')
    else:
        b = final[i].split()
        b.append('.')
        b.insert(0,'-')
    temp.append(b)

# clear final
final.clear()

# recreate list
for i in range(len(temp)):
    # remove whitespace between final word and dot/s
    a = temp[i][-2], temp[i][-1]
    b = ''.join(a)
    temp[i].remove(temp[i][-1])
    temp[i].remove(temp[i][-1])
    temp[i].append(b)

    # actually recreate list
    final.append(' '.join(temp[i]))


# use title on given names
names = ['joe castiglione','troop']
for i in final:
    if names[0] in i:
        loc = final.index(i)
        a = i.replace(names[0],names[0].title())
        final.remove(i)
        final.insert(loc,a)
    elif names[1] in i:
        loc = final.index(i)
        a = i.replace(names[1],names[1].title())
        final.remove(i)
        final.insert(loc,a)

# final print
for i in final:
    print(i)

