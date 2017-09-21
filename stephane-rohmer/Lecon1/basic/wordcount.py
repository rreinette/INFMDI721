#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# fonction helper opens a file, and return a dictionary of the word in lower case and its occurence in the file 

def helper(filename):
  with open(filename) as f:
    read_data =  f.read()
  f.closed  
    
  inventaireMot = read_data.split()       # creer la liste de chaque mot du texte pour utiliser 
                                          # les fonctions de listes
  dict_mot = {'':0}                       # initialise le dictionnaire
    
  for word in inventaireMot:              # populate the dictionnary 
   if word.lower() not in dict_mot:
     dict_mot[word.lower()]=inventaireMot.count(word)

  return dict_mot


def print_words(filename):

  dict_mot = helper(filename)

  for item in sorted(dict_mot):           # parse mot 1 a 1 dans le dictionnaire dans l'ordre alphabétique
    print (item," ",dict_mot[item])       # pour chaque mot dans l'ordre alfabetique, affiche son occurence

  return dict_mot


def print_top(filename):
  dict_mot = helper(filename)
  top_word_dict = {}

  biggest_occurence_list = sorted(dict_mot.values(), reverse = True)[:20]
                                        # crée une liste avec les 20 plus grandes valeurs dans le dictionnaire de mot
  
  for k,v in dict_mot.items():          # creer un dictionnaire tempon pour stoker les mots/occurences des 20 élément
    if v in biggest_occurence_list:
      top_word_dict[k]=v

  print (top_word_dict)

  for i in range(20):                   # a optimiser, on balaye 20x le dictionnaire de 20 mots...
    for k,v in top_word_dict.items():   # scan le dictionnaire de mot. si la valeur correspond à la valeur de la liste 
      if v == biggest_occurence_list[i]:  # ordonné, alors fait l'affichage
        print (k,v)
  
  return

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
