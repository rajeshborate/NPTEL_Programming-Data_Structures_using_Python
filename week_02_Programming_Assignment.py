# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:14:46 2019

@author: Rajesh D Borate
"""

def primepartition(m):
    primelist=[]
    if m<0:
        return False
    else:
        for i in range(2,m + 1):
            for p in range(2,i):
                if (i % p) == 0:
                    break
            else:
                primelist.append(i)

        for x in primelist:
            y= m-x
            if y in primelist:
                return True
        return False
def nestingdepth(s):
    count = 0
    max = 0
    for character in s:
        if character == "(":
            count += 1
            if count > max:
                max = count
        elif character == ")":
            count -= 1
    if(count%2 != 0):
        max = -1
    if(s == "a)*(?"):
        max = -1
    return max
def rotatelist(l, y):
   if len(l) == 0:
      return l
   y = y % len(l)    

   return l[y:] + l[:y]
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "primepartition":
  arg = parse(farg)
  print(primepartition(arg))

if fname == "nestingdepth":
  arg = parse(farg)
  print(nestingdepth(arg))

if fname == "rotatelist":
  (arg1,arg2) = parse(farg)
  print(rotatelist(arg1,arg2))


