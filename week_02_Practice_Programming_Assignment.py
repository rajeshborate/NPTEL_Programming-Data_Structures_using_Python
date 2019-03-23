# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:22:13 2019

@author: Rajesh D Borate
"""

def intreverse(n):
  ans = 0
  while n > 0:
    (d,n) = (n%10,n//10)
    ans = 10*ans + d
  return(ans)

def matched(s):
  nested = 0
  for i in range(0,len(s)):
    if s[i] == "(":
       nested = nested+1
    elif s[i] == ")":
       nested = nested-1
       if nested < 0:
          return(False)    
  return(nested == 0)

def factors(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist = factorlist + [i]
  return(factorlist)

def isprime(n):
  return(factors(n) == [1,n])


def sumprimes(l):
  sum = 0
  for i in range(0,len(l)):
    if isprime(l[i]):
      sum = sum+l[i]
  return(sum)

import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "intreverse":
   arg = parse(farg)
   print(intreverse(arg))
elif fname == "matched":
   arg = parse(farg)
   print(matched(arg))
elif fname == "sumprimes":
   arg = parse(farg)
   print(sumprimes(arg))
else:
   print("Function", fname, "unknown")

