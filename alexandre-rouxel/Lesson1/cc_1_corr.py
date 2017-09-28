import unittest


# Given a string and a non-negative int n, return a larger string
# that is n copies of the original string.

def string_times(string, n):

    return (string*n)

# Given an array of ints, return True if one of the first 4 elements
# in the array is a 9. The array length may be less than 4.
def array_front9(nums):
    #longueur=min(len(nums) & 4)
    idx = 0;

    out = False
    for ele in nums :
        idx +=1
        if ele == 9 and  idx < 5 :
            out = True

    return out


# Given a string, return the count of the number of times
# that a substring length 2 appears  in the string and also as
# the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
#def last2(string):
#    words=string.split(' ')
#    count = 0
#    for word in words :
#        if word[:2] == word[-1:-3:-1][::-1] :
#           count +=1
#    return count

def last2(string):
  if len(string) < 2:
    return
  pattern = string[-2:]
  count = 0
  for i in range(0,len(string) - 3):
    if string[i:i+2] == pattern:
      count += 1
  return count

#Write a program that maps a list of words into a list of
#integers representing the lengths of the correponding words.
#def length_words(array) :
#    interger_list=[]
#    for word in array :
#        interger_list.append(len(word))
#    return interger_list
# map returns an iterable that can be cast to list
def length_words(array) :
    return list(map(lambda x : len(x) , array))   #map (array, lambda x: len(x))

#write fizbuzz programm
def fizbuzz(number):
    for i in range(number):
        if i%15 == 0:
            print("fizbuzz")
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)

#Write a function that takes a number and returns a list of its digits.
def number2digits(number):
    return [int(x) if x.isdigit() else 'NaN' for x in str(number)]

#Write function that translates a text to Pig Latin and back.
#English is translated to Pig Latin by taking the first letter of every word,
#moving it to the end of the word and adding 'ay'
def pigLatin(text):
#    text_out=''
#    for word in text.split( ) :
#        lword=list(word)
#        lword[1:].append(lword[0])
#        lword.append('ay')
#        text_out.join(str(lword))
#        text_out.join(' ')
#    return text_out
  return ' '.join([ x[1:] + x[0]+'ay' for x in text.split(' ') ])


#Write a proramm that return a dictionary of occurences of the alphabet for a given string.
# Test it with the Lorem upsuj
#"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
def occurences(text) :
    result = {}
    #[result[i] += 1 if i in result else result[i =1 for i in text]]
    
    return (result)


# Here's our "unit tests".
class Lesson1Tests(unittest.TestCase):
    fizbuzz(100)
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
        self.assertEqual(pigLatin("The quick brown fox") , "heTay uickqay rownbay oxfay")



def main():
    unittest.main()

if __name__ == '__main__':
    main()
