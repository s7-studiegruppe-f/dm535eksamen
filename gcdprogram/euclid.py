#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import call
from latex import *
import sys

def makeGcdTable(i, r, q):
    rows = []
    row0 = makeGcdRow(0, r[0], "-") + "Start værdier \\\\"
    rows.append(row0)
    x = 1
    while x < i:
        row = makeGcdRow(x, r[x], q[x]) 
        row += "Da ${} = {} \cdot {} + {}$ \\\\".format(r[x-1], q[x],
            r[x], r[x + 1])
        rows.append(row)
        x += 1
    return "\n".join(rows)

def makeGcdRow(i, r, q):
    return "${}$ & ${}$ & ${}$ & ".format(i, r, q) 
        
def gcd(a, b):
    r = []
    q = []
    i = 0
    while True:
        if i == 0:
            r.append(a)
            q.append(None)
        elif i == 1:
            r.append(b)
            q.append(a / b)
        else:
            r.append(r[i-2] % r[i-1])
            if r[i] == 0:
                break
            q.append(r[i-1] / r[i])
        i += 1
    return(i, r, q)

def extendedGcd(i, r, q):
    s = [0, 1]
    t = [1, 0]
    x = 2
    while (x < i):
        print x - 1, x
        s.append(s[x - 2] - q[x] * s[x - 1])
        t.append(s[x - 2] - q[x] * t[x - 1])
        x += 1
    return (s, t)

if len(sys.argv) < 2:
    print "python %s tal1 tal2" % sys.argv[0]
    print "\tKør programmet med to tal som argumenter for at få"
    print "\tlatex dokument hvor deres gcd bliver beregnet og forklaret."
    exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])

file = open("output.tex", "w")
(i, r, q) = gcd(a, b)
gcdTable = makeGcdTable(i, r,  q)
coprime = "Da $gcd({}, {}) = 1$ er de også indbyrdes primiske.".format(a, b)
if r[i - 1] != 1:
    coprime = ""

formatDict = { 
    'a': a,
    'b': b,
    'gcdtable': gcdTable,
    'lasti': i - 1,
    'lastr': r[i - 1],
    'coprime': coprime
    }

(s, t) = extendedGcd(i, r, q)
# for s, t in extendedGcd(i, r, q):
#     print "%d %d" % (s, t)
file.write(latexDoc.format(**formatDict))


