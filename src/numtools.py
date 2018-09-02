#! /usr/bin/python3

import sys
import getopt
from datetime import date

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


def get_operators(pretty, mult):
    if mult:
        return [("+", add), ("-", sub), ("×", mul), ("÷", div)] if pretty else [("+", add), ("-", sub), ("*", mul), ("/", div)]
    return [("+", add), ("-", sub)]

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def gen_cal(l, fast, match, operators, depth=0):
    r = []
    if len(l) == 1:
        return [(l[0], str(l[0]))]
    else:
        calcs = gen_cal(l[1:], fast, match, operators, depth + 1)
        for sign,operator in operators:
            for (res, s) in calcs:
                if operator == div and res == 0:
                    continue
                s2 = (str(l[0]) if is_integer(l[0]) \
                        else "(" + str(l[0]) + ")") + sign + \
                        (s if is_integer(s) else "(" + s + ")")
                res = operator(l[0], res)
                if depth == 0:
                    if res == match:
                        r.append((res, s2))
                        if fast:
                            return r
                else:
                    r.append((res, s2))
    return r

def generateMatches(number, match, p_sort, p_lex, p_group, fast, operators):
    if p_sort or p_lex:
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
            cals = gen_cal(element, fast, match, operators)
            for (res, calstr) in cals:
                if res == match and calstr not in c:
                    c.append(calstr)
                    if fast:
                        return c
        l = c
    return l

def printUsage(name):
  print("Usage:\t%s -i input [-slgqa] [-m match]" % name)
  print("\t-i input : input on which to work (numeric string or 'today' for current date)")
  print("\t-m match : number to find/match")
  print("\t-l : performs a lexical generation of permutations (implies -s to be called)")
  print("\t-s : sorts the numbers before processing")
  print("\t-g : generate groups")
  print("\t-q : quick mode, exists on the first match found instead of finding them all")
  print("\t-a : only uses +/- operations (no ×/÷)")
  print("\t-p : pretty print (uses utf-8 operators and displays the result)")

def main():
    sort = False
    number = None
    match = None
    lexical = False
    gen_group = False
    fast = False
    multiplications = True
    pretty = False

    try:
        opt, args = getopt.getopt(sys.argv[1:], "hi:m:lsgqap", ["help"])
    except getopt.GetoptError:
        printUsage(sys.argv[0])
        return 1
    for op, val in opt:
        if op in ("-h", "--help"):
            printUsage(sys.argv[0])
            return 0
        elif op == "-m":
            match = val
        elif op == "-i":
            if val == 'today':
                number = date.today().strftime("%d%m%Y")
            else:
                number = val
        elif op == "-s":
            sort = True
        elif op == "-l":
            lexical = True
        elif op == "-g":
            gen_group = True
        elif op == "-q":
            fast = True
        elif op == "-a":
            multiplications = False
        elif op == "-p":
            pretty = True
    if number:
        matches = generateMatches(number, match, sort, lexical, gen_group,
                fast, get_operators(pretty, multiplications))
        for m in matches:
            if pretty and match:
                print('%s = %s' % (m, match))
            else:
                print(m)
    else:
        printUsage(sys.argv[0])
        return 1

if __name__ == "__main__":
      sys.exit(main())
