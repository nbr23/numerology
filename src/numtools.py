#! /usr/bin/python3.4
import sys

def isort(s):
    l = []
    for c in s:
        c = int(c)
        i = 0
        while i < len(l) and l[i] <= c:
            i += 1
        l.insert(i, c)
    return l

def lcopy(l):
    nl = []
    for i in range(0, len(l)):
        nl.insert(i, l[i])
    return nl

def lex_perm(l, b):
    l = lcopy(l)
    x = -1
    y = -1
    ll = len(l)
    lr = []
    for i in range(0, ll - 1):
        if (l[i] < l[i + 1]):
            x = i
    if x == -1:
        return

    for i in range(0, ll):
        if l[x] < l[i]:
            y = i
    l[x],l[y] = l[y],l[x]

    i = 0
    while i <= x:
        lr.append(l[i])
        i += 1

    for i in range(0, ll - x - 1):
        lr.append(l[ll - 1 - i])
    b.append(lr)
    lex_perm(lr, b)

def group(l):
    gr = []
    for i in range(0, len(l)):
        base = 0
        for j in range(0, i + 1):
            base = base * 10 + l[j]
        groups = group(l[i + 1:])
        if len(groups) < 1:
            gr.append([base])
        else:
            for j in range(0, len(groups)):
                groups[j].insert(0, base)
                gr.append(groups[j])
    return gr
