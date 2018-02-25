'''
Tab Link QR Generator

File: Storing current links in file 'data.txt'
'''


import re

a1=''
pathToCurrentTabs="/Users/..../Library/Application Support/Google/Chrome/Profile 1/Current Tabs"
file1 = open(pathToCurrentTabs,"r") 
g1=file1.read()
da = g1.split("\x00")
pattern = re.compile(r'https?://(.*?)x0')
pn = re.compile(r'https?://*')
nw = filter(pn.match, da)
st1 = '$\n'.join(nw)
st1 = st1+'$\n'
f = open('data.txt','w')
f.write(st1)
f.close()
