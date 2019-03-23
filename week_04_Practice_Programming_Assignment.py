# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:24:30 2019

@author: Rajesh D Borate
"""

def orangecap(d):
  total = {}
  for k in d.keys():
    for n in d[k].keys():
      if n in total.keys():
        total[n] = total[n] + d[k][n]
      else:
        total[n] = d[k][n]

  maxtotal = -1
  for n in total.keys():
    if total[n] > maxtotal:
      maxname = n
      maxtotal = total[n]

  return(maxname,maxtotal)

def listtodict(poly):
  dpoly = {}
  for term in poly:
    coeff = term[0]
    exp = term[1]
    dpoly[exp] = coeff
  return(dpoly)

def dicttolist(dpoly):
  lpoly = []
  for exp in sorted(dpoly.keys()):
    lpoly.append((dpoly[exp],exp))
  lpoly.reverse()
  return(lpoly)

def dpolyadd (dpoly1,dpoly2):
  sumpoly = {}
  for exp in dpoly1.keys():
    sumpoly[exp] = dpoly1[exp]

  for exp in dpoly2.keys():
    if exp in sumpoly.keys():
      sumpoly[exp] = sumpoly[exp] + dpoly2[exp]
    else:
      sumpoly[exp] = dpoly2[exp]

  return(sumpoly)

def dpolymult (dpoly1,dpoly2):
  multpoly = {}
  for exp1 in dpoly1.keys():
    for exp2 in dpoly2.keys():
      newexp = exp1 + exp2
      newcoeff = dpoly1[exp1] * dpoly2[exp2]
      if newexp in multpoly.keys():
        multpoly[newexp] = multpoly[newexp] + newcoeff
      else:
        multpoly[newexp] = newcoeff
  return(multpoly)

def cleanup(dpoly):
  dpolyclean = {}
  for exp in dpoly.keys():
    if dpoly[exp] != 0:
      dpolyclean[exp] = dpoly[exp]
  return(dpolyclean)

def addpoly(p1,p2):
  d1 = listtodict(p1)
  d2 = listtodict(p2)
  res = dpolyadd(d1,d2)
  return(dicttolist(cleanup(res)))

def multpoly(p1,p2):
  d1 = listtodict(p1)
  d2 = listtodict(p2)
  res = dpolymult(d1,d2)
  return(dicttolist(cleanup(res)))
import ast

def todict(inp):
    inp = ast.literal_eval(inp)
    return (inp)

def topairoflists(inp):
    inp = "["+inp+"]"
    inp = ast.literal_eval(inp)
    return (inp[0],inp[1])

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "orangecap":
   arg = todict(farg)
   print(orangecap(arg))
elif fname == "addpoly":
   (arg1,arg2) = topairoflists(farg)
   print(addpoly(arg1,arg2))
elif fname == "multpoly":
   (arg1,arg2) = topairoflists(farg)
   print(multpoly(arg1,arg2))
else:
   print("Function", fname, "unknown")
  

