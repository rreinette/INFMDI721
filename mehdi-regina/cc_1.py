#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:39:07 2017

@author: mehdiregina
"""
import unittest
import string


# Given a string and a non-negative int n, return a larger string
# that is n copies of the original string.

def string_times(string, n):
    #se rappeler qu'on peut multiplier un str
    return n*string 

# Given an array of ints, return True if one of the first 4 elements
# in the array is a 9. The array length may be less than 4.
def array_front9(nums):
    #longueur=min(len(nums) & 4)
    test=False 
    for i in range(0,min(len(nums),4)-1) :
        if(nums[i]==4):
            test=True
            
    return test


# Given a string, return the count of the number of times
# that a substring length 2 appears  in the string and also as
# the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(string):
    if len(string)<2:
        return 0
    #je prends des 2 derniers à la fin
    substring=string[-2:]
    count=0
    for i in range(0,len(string)-3):
        if(string[i:i+2]==substring):
            count+=1
    return count


#Write a program that maps a list of words into a list of
#integers representing the lengths of the correponding words.
def length_words(array):
     # ! ou voir fonction map : Apply function to every item of iterable and return a list of the results !
     
     #meth1 list comprehension
     liste1=[len(mot) for mot in array]
     
     #meth2 map function (définir une fonction via lambda, préciser l'élément à itérer)
     liste2=list(map(lambda mot:len(mot),array))
     
     return liste2

#write fizbuzz programm
def fizbuzz():
    #bien comprendre la structure d'une boucle conditionnelle
   for i in range(0,100):
       if(i%3==0 and i%5==0):
           print("fizzbuzz")
       elif(i%5==0):
           print("buzz")
       elif(i%3==0):
           print("fizz")
       else:
           print(i)
                   

#Write a function that takes a number and returns a list of its digits.
def number2digits(number):      
    return [int(digit) for digit in str(number)]

#Write function that translates a text to Pig Latin and back.
#English is translated to Pig Latin by taking the first letter of every word,
#moving it to the end of the word and adding 'ay'
def pigLatin(text):
    liste_mot=text.split()
    for i,mot in enumerate(liste_mot):
        liste_mot[i]=mot[1:]+mot[0].lower()+"ay"
        
    return " ".join(liste_mot)

#Write a proramm that returna dictionary of occurences of the alphabet for a given string.
# Test it with the Lorem upsuj
#"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
def occurences(text):
    dico_lettre=dict((lettre,0) for lettre in list(string.ascii_lowercase))
    #je supprime les espaces dans le texte via ces transformations
    for lettre in "".join(text.lower().split()):
        try:
            dico_lettre[lettre]+=1
        except(KeyError):
            #s'il y a une erreur de clé ce n'est pas une lettre de l'alphabet donc je l'ignore via pass !
            pass
        return dico_lettre

# Here's our "unit tests".
class Lesson1Tests(unittest.TestCase):
    fizbuzz()
    def testArrayFront9(self):
        self.assertEqual(array_front9([1, 2, 9, 3, 4]) , True)
        self.assertEqual(array_front9([1, 2, 3, 4, 9]) , False)
        self.assertEqual(array_front9([1, 2, 3, 4, 5]) , False)

    def testStringTimes(self):
        self.assertEqual(string_times('Hel', 2),'HelHel' )
        self.assertEqual(string_times('Toto', 1),'Toto' )
        self.assertEqual(string_times('P', 4),'PPPP' )

    def testLast2(self):
        self.assertEqual(last2('hixxhi') , 1)
        self.assertEqual(last2('xaxxaxaxx') , 1)
        self.assertEqual(last2('axxxaaxx') , 2)

    def testLengthWord(self):
        self.assertEqual(length_words(['hello','toto']) , [5,4])
        self.assertEqual(length_words(['s','ss','59fk','flkj3']) , [1,2,4,5])

    def testNumber2Digits(self):
        self.assertEqual(number2digits(8849) , [8,8,4,9])
        self.assertEqual(number2digits(4985098) , [4,9,8,5,0,9,8])

    def testPigLatin(self):
        self.assertEqual(pigLatin("The quick brown fox") , "Hetay uickqay rownbay oxfay")



def main():
    unittest.main()

if __name__ == '__main__':
    main()

