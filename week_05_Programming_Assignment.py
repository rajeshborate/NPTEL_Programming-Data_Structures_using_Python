# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:17:51 2019

@author: Rajesh D Borate
"""

def borrowers_input(b):
    x=input()
    while x!='Checkouts':
        x=x.split('~')
        b.append(x)
        x=input()

def checkouts_input(c):
    x=input()
    while x!='EndOfInput':
        x=x.split('~')
        c.append(x)
        x=input()

def output():
    global books,borrower,checkout
    date=[]
    uname=[]
    name=[]
    Anum=[]
    title=[]
    for i in range(0,len(checkout)):
        date.append(checkout[i][2])

    for i in range(0,len(checkout)):
        uname.append(checkout[i][0])

    for i in range(0,len(uname)):
        for j in range(0,len(borrower)):
            if(uname[i] == borrower[j][0]):
                name.append(borrower[j][1])

    for i in range(0,len(checkout)):
        Anum.append(checkout[i][1])

    for i in range(0,len(Anum)):
        for j in range(0,len(books)):
            if(Anum[i] == books[j][0]):
                title.append(books[j][1])

    final=[]
    for i in range(0,len(checkout)):
        final.append(date[i]+'~'+name[i]+'~'+Anum[i]+'~'+title[i])
    final.sort()
    for i in range(0,len(final)):
        print(final[i])


books=[]
borrower=[]
checkout=[]
x=input()
x=input()
while x!='Borrowers':
    x=x.split('~')
    books.append(x)
    x=input()
borrowers_input(borrower)
borrower.sort()
checkouts_input(checkout)
output()
