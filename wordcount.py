#! /usr/bin/python
import sys
import os
filename=sys.argv[1]
# New comment
f1 = open(filename,'r')
ls= f1.read().split(' ')
ls =sorted(ls)
print ls
prev=ls[0]
count =0
flag=1
d={}
for i in ls[:len(ls)-1]:
 current =i
 if count > 0:
  if prev == current:
    flag = flag + 1
  d[prev]=flag
 prev=i
 count = count + 1
print d
