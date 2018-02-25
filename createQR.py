'''
Tab Link QR Generator

File: Generate the QR code as image using first 10 links
'''

import pyqrcode
import os

a1=''
count=0
noLinks=10
file1 = open("data.txt","r+") 
for i in file1.readlines():
	a1+=i[:-1]
	if count < noLinks:
		count+=1
	else:
		break
print a1


u1 = unicode(a1, "utf-8")
img = pyqrcode.create(u1)

img.png('img1.png', scale=5)
