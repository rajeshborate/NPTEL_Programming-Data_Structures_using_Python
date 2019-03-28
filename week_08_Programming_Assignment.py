# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:13:48 2019

@author: Rajesh D Borate
"""

def longestPalSubstr(string): 
	maxLength = 1

	start = 0
	length = len(string) 

	low = 0
	high = 0

	 
	for i in range(1, length): 
		 
		low = i - 1
		high = i 
		while low >= 0 and high < length and string[low] == string[high]: 
			if high - low + 1 > maxLength: 
				start = low 
				maxLength = high - low + 1
			low -= 1
			high += 1

		 
		low = i - 1
		high = i + 1
		while low >= 0 and high < length and string[low] == string[high]: 
			if high - low + 1 > maxLength: 
				start = low 
				maxLength = high - low + 1
			low -= 1
			high += 1

	 
	 

	print (maxLength)
	print (string[start:start + maxLength])



 
length = input()
string = input()
longestPalSubstr(string)