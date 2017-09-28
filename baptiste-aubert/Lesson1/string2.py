#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  if len(s)<3:
      return s
  if (len(s)>=3 and s[-3:]=='ing'):
      return s + 'ly'
  elif (len(s)>=3 and s[-3:]!='ing'):
      return s +'ing'



# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  notS = s.find('not')
  bS = s.find('bad')
  if (notS != -1 and bS != -1 and bS > notS):
    s = s[:notS] + 'good' + s[bS+3:]
  return s




# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print (prefix + " got: " + str(got) + " expected: " + str(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ("verbing")
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print ("not_bad")
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

if __name__ == '__main__':
  main()
