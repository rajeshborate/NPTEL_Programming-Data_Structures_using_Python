# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:15:36 2019

@author: Rajesh D Borate
"""

import math
def progression(l):
  if len(l)==1 or len(l)==2:
    return True
  else:
    if len(l)==3 and l[0]-l[1]==l[1]-l[2]:
      return True
    elif len(l)>3 and l[0]-l[1]==l[len(l)-2]-l[len(l)-1]:
      return True
    else:
      return False

def checkprime(n):
  for i in range(2,int(math.sqrt(n))):
    if n%i==0:
      return False
  return True

def primesquare(l):
  for i in range(len(l)):
    if i%2==0:
      if math.sqrt(l[i])==int(math.sqrt(l[i])):
        continue
      else:
        return False
    else:
      if checkprime(l[i]):
        continue
      else:
        return False
  return True

def matrixflip(l,d):
  m=l.copy()
  if d=='v':
    m.reverse()
    return m
  if d=='h':
    temp=[]
    for i in m:
      f=i.copy()
      f.reverse()
      temp.append(f)
    return temp
  else:
    return m
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "progression":
  arg = parse(farg)
  print(progression(arg))

if fname == "primesquare":
  arg = parse(farg)
  print(primesquare(arg))

if fname == "matrixflip":
  (arg1,arg2) = parse(farg)
  savearg1 = []
  for row in arg1:
    savearg1.append(row[:])
  ans = matrixflip(arg1,arg2)
  if savearg1 == arg1:
    print(ans)
  else:
    print("Side effect")

