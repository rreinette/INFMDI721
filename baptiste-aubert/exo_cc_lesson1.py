import unittest


# Given a string and a non-negative int n, return a larger string
# that is n copies of the original string.

def string_times(string, n):
    return string * n

# Given an array of ints, return True if one of the first 4 elements
# # in the array is a 9. The array length may be less than 4.
def array_front9(nums):
    for i in range(0,len(nums)):
        if (i<=3 and nums[i]==9):
            return True
    return False



# # Given a string, return the count of the number of times
# # that a substring length 2 appears  in the string and also as
# # the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(string):
    look = string[-2:]
    count =0
    for i in range(0, len(string)-4, 1):
        if (string[i:i+2]==look):
            count +=1
    return count




# #Write a program that maps a list of words into a list of
# #integers representing the lengths of the correponding words.
def length_words(array):
    return list(map(lambda x : len(x), array))

#
# #write fizbuzz programm
def fizbuzz():
    result=[]
    for i in range(0,100):
        if i%3==0:
            result.append("fizz")
        elif i%5==0:
            result.append("buzz")
        else:
            result.append(i)
    print (result)



# #Write a function that takes a number and returns a list of its digits.
def number2digits(number):
    text=str(number)
    result=[]
    for it in text:
        result.append(int(it))
    return result


# #Write function that translates a text to Pig Latin and back.
# #English is translated to Pig Latin by taking the first letter of every word,
# #moving it to the end of the word and adding 'ay'
def pigLatin(text):
    return ' '.join(x[1:]+x[0]+ 'ay' for x in text.split(' ')).capitalize()

# #Write a proramm that returna dictionary of occurences of the alphabet for a given string.
# # Test it with the Lorem upsuj
# #"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
def occurences(text):
    to_ret = {}
    for word in text.split(' '):
        to_ret[word]=to_ret.get(word,0)+1
    return to_ret

print (occurences("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"))

fizbuzz()
# Here's our "unit tests".
class Lesson1Tests(unittest.TestCase):

    def testArrayFront9(self):
        self.assertEqual(array_front9([1, 2, 9, 5, 8]) , True)
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
