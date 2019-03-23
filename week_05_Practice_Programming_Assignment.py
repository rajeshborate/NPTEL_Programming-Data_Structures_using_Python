# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:25:50 2019

@author: Rajesh D Borate
"""

def gradetonum(grade):
    if grade == 'A':
        return(10)
    elif grade == 'AB':
        return(9)
    elif grade == 'B':
        return(8)
    elif grade == 'BC':
        return(7)
    elif grade == 'C':
        return(6)
    elif grade == 'CD':
        return(5)
    elif grade == 'D':
        return(4)
    else:
        return(0)
                   
rollname = {}
gradepoint = {}
coursecount = {}

nextline = input().strip()
while nextline.find("Courses") < 0:
    nextline = input().strip()

# Read course data
while nextline.find("Students") < 0:
    nextline = input().strip()
    # Course data is irrelevant

nextline = input().strip()
# Read students data
while nextline.find("Grades") < 0:
    fields = nextline.split('~')
    roll=fields[0]
    name=fields[1]
    rollname[roll] = name
    gradepoint[roll] = 0
    coursecount[roll] = 0
    nextline = input().strip()

nextline = input().strip()
# Read grades data
while nextline.find("EndOfInput") < 0:
    fields = nextline.split('~')
    roll=fields[3]
    grade=fields[4]
    gradepoint[roll] += gradetonum(grade)
    coursecount[roll] += 1
    nextline = input().strip()

for roll in sorted(rollname.keys()):
    if coursecount[roll] > 0:
        gpa = round(gradepoint[roll]/coursecount[roll],2)
    else:
        gpa = 0
    print(roll,rollname[roll],gpa,sep='~',end='\n' )
