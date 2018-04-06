#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

colors = ['red', 'blue', 'green']
print colors[0]    ## red
print colors[2]    ## green
print len(colors)  ## 3

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
  sum += num
print sum  ## 30
