import unittest


# Given a string and a non-negative int n, return a larger string
# that is n copies of the original string.

def string_times(string, n):
<<<<<<< HEAD:jeanmarc-sevin/Lesson1/exo_cc_lesson_01.py
    larger_string = string*n
    return larger_string
=======
    return n* string
>>>>>>> 400e12cf20fb33bb00c46c851129b3750a12a0d6:_Lessons_Exercices/cc_1.py

# Given an array of ints, return True if one of the first 4 elements
# in the array is a 9. The array length may be less than 4.
def array_front9(nums):
    test = False
    for el in nums[:4]:
        if el == 9:
            test = True
            break            
    return test
    #longueur=min(len(nums) & 4)
<<<<<<< HEAD:jeanmarc-sevin/Lesson1/exo_cc_lesson_01.py
=======
    length = nums.length
    for i in range(0,length):
      if i <=3 and nums[i] == 9:
        return True
    return False

>>>>>>> 400e12cf20fb33bb00c46c851129b3750a12a0d6:_Lessons_Exercices/cc_1.py

# Given a string, return the count of the number of times
# that a substring length 2 appears in the string and also as
# the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(string):
<<<<<<< HEAD:jeanmarc-sevin/Lesson1/exo_cc_lesson_01.py
    derniers_caracteres = string[-2:]
    compteur = 0
    for i in range(0,len(string) - 2):
        if string[i:i+2] == derniers_caracteres:
            compteur += 1
    return compteur
=======
  if string.length < 2:
    return
  pattern = string[-2:]
  count = 0
  for i in range(0,string.length - 3):
    if string[i:i+2] == pattern:
      count += 1
  return


def toto(x):
  return x.length
>>>>>>> 400e12cf20fb33bb00c46c851129b3750a12a0d6:_Lessons_Exercices/cc_1.py

#Write a program that maps a list of words into a list of
#integers representing the lengths of the correponding words.
def length_words(array):
<<<<<<< HEAD:jeanmarc-sevin/Lesson1/exo_cc_lesson_01.py
    return [len(word) for word in array]
=======
  return map(array, lambda x: x.length)
>>>>>>> 400e12cf20fb33bb00c46c851129b3750a12a0d6:_Lessons_Exercices/cc_1.py

#write fizbuzz programm
def fizbuzz():
    return

#Write a function that takes a number and returns a list of its digits.
def number2digits(number):
<<<<<<< HEAD:jeanmarc-sevin/Lesson1/exo_cc_lesson_01.py
    return [int(str(number)[i]) for i in range(0, len(str(number)))]
=======
  
  return [x for x in str(number)]
>>>>>>> 400e12cf20fb33bb00c46c851129b3750a12a0d6:_Lessons_Exercices/cc_1.py

#Write function that translates a text to Pig Latin and back.
#English is translated to Pig Latin by taking the first letter of every word,
#moving it to the end of the word and adding 'ay'
def pigLatin(text):
<<<<<<< HEAD:jeanmarc-sevin/Lesson1/exo_cc_lesson_01.py
    words = text.split()
    return " ".join([word[1:]+word[0]+"ay" for word in words])
=======
  return ' '.join([ x[1:] + x[0]+'ay' for x in text.split(' ') ])
>>>>>>> 400e12cf20fb33bb00c46c851129b3750a12a0d6:_Lessons_Exercices/cc_1.py

#Write a proramm that returna dictionary of occurences of the alphabet for a given string.
# Test it with the Lorem upsuj
#"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
def occurences(text):
  result = {}
  #[result[i]  if i in result else result[i] = 1 for i in text]
  return result

# Here's our "unit tests".
class Lesson1Tests(unittest.TestCase):
    fizbuzz()
    def testArrayFront9(self):
        self.assertEqual(array_front9([1, 2, 9, 3, 4]) , True)
        self.assertEqual(array_front9([1, 2, 3, 4, 9]) , False)
        self.assertEqual(array_front9([1, 2, 3, 4, 5]) , False)
        self.assertEqual(array_front9("toto" , -1)

    def testStringTimes(self):
        self.assertEqual(string_times('Hel', 2),'HelHel' )
        self.assertEqual(string_times('Toto', 1),'Toto' )
        self.assertEqual(string_times('P', 4),'PPPP' )

    def testLast2(self):
        self.assertEqual(last2('hixxhi') , 1)
        self.assertEqual(last2('xaxxaxaxx') , 1)
        self.assertEqual(last2('axxxaaxx') , 2)
        self.assertEqual(last2('a') , 0)

    def testLengthWord(self):
        self.assertEqual(length_words(['hello','toto']) , [5,4])
        self.assertEqual(length_words(['s','ss','59fk','flkj3']) , [1,2,4,5])
        self.assertEqual(length_words(9) , [1,2,4,5])

    def testNumber2Digits(self):
        self.assertEqual(number2digits(8849) , [8,8,4,9])
        self.assertEqual(number2digits(4985098) , [4,9,8,5,0,9,8])

    def testPigLatin(self):
        self.assertEqual(pigLatin("The quick brown fox") , "Hetay uickqay rownbay oxfay")



def main():
    unittest.main()

if __name__ == '__main__':
    main()

