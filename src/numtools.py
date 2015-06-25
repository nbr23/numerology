#! /usr/bin/python3.4

import sys
import getopt

def isort(s):
    l = []
    for c in s:
        c = int(c)
        i = 0
        while i < len(l) and l[i] <= c:
            i += 1
        l.insert(i, c)
    return l

def toList(s):
    l = []
    for c in s:
        l.append(int(c))
    return l

def lcopy(l):
    nl = []
    for i in range(0, len(l)):
        nl.insert(i, l[i])
    return nl

def lex_perm_i(l):
    b = []
    b.append(lcopy(l))
    l = lcopy(l)
    ll = len(l)
    while True:
        x = -1
        lr = []
        for i in range(0, ll - 1):
            if (l[i] < l[i + 1]):
                x = i
        if x == -1:
            break

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
        l = lcopy(lr)
    return b

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

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a/b

operators = [add, sub, mul, div]
operators_s = ["+", "-", "×", "÷"]

def gen_cal(l, depth, fast, match):
    r = []
    if len(l) == 1:
        return [(l[0], str(l[0]))]
    else:
        calcs = gen_cal(l[1:], depth + 1, fast, match)
        for i in range(0, len(operators)):
            for (res, s) in calcs:
                if operators[i] == div and res == 0:
                    continue
                res = operators[i](l[0], res)
                s2 = str(l[0]) + operators_s[i] + s
                if depth == 0:
                    if res == match:
                        r.append((res, s2))
                        if fast:
                            return r
                else:
                    r.append((res, s2))
    return r

def generateMatches(number, match, p_sort, p_lex, p_group, fast):
    if p_sort:
        l = isort(number)
    else:
        l = toList(number)
    if p_lex:
        l = lex_perm_i(l)
    else:
        l = [l]
    if p_group:
        g = []
        for permutation in l:
            gr = group(permutation)
            for elt in gr:
                g.append(elt)
        l = g
    if match:
        match = int(match)
        c = []
        for element in l:
            cals = gen_cal(element, 0, fast, match)
            for (res, calstr) in cals:
                if res == match and calstr not in c:
                    c.append(calstr)
                    if fast:
                        return c
        l = c
    return l
 

def getMatches(s, match, fast=True, v=False):
    s = isort(s)
    if v:
        print("Sample sorted:")
        print(s)

    b = lex_perm_i(s)
    if v:
        print("Created %i permutations" % len(b))

    g = []
    for perm in b:
        groups = group(perm)
        for elt in groups:
            g.append(elt)
    if v:
        print("Created %i different groupings" % len(g))

    c = []
    lg = len(g)
    tot = 0
    for gr in g:
        calcs = gen_cal(gr, 0, fast, match)
        for (res,cstr) in calcs:
            tot += 1
            if res == match and cstr not in c:
                c.append(cstr)
                if fast:
                    return c
    if v:
        print("Found %i matching calculus from a total of %i " % (len(c), tot))
    return c


