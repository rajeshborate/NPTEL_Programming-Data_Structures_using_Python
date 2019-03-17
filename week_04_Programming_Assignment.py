# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:17:26 2019

@author: Rajesh D Borate
"""

def rainaverage(l):
    sum = dict()
    count = dict()
    for (k, v) in l:
        sum[k] = sum.get(k, 0) + v
        count[k] = count.get(k, 0) + 1
    for k in sum:
        sum[k] /= count[k]
    return sorted(list(sum.items()))
  
def flatten(alist):
    rv = []
    for val in alist:
        if isinstance(val, list):
            rv.extend(flatten(val))
        else:
            rv.append(val)
    return rv
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "rainaverage":
  arg = parse(farg)
  print(rainaverage(arg))

if fname == "flatten":
  arg = parse(farg)
  print(flatten(arg))

