#!/usr/bin/python
import sys
def count(filename):
    print("Hello")
    word_count = {}
    # Ouverture du fichier
    with open(filename) as textfile:
        lines = textfile.read()
        # On recupère la liste de mots pour chaque ligne
        words = lines.lower().split()
        print(words)
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    if textfile.closed == False:
        textfile.close()
    return word_count


def print_words(filename):
    all_word_appereance = count(filename)
    print('Debut enumeration des mots et de leur frequence')
    for key in all_word_appereance:
        print('le mot ' + key + ' est apparue: %s' % all_word_appereance[key])


def print_top(filename):
    tuple = []
    all_word_appearance = count(filename)
    all_word_sorted_tuple = sorted(all_word_appearance.items(), key=lambda tuple: tuple[1])
    for tuple in all_word_sorted_tuple[-20:]:
        print('le mot ' + tuple[0] + 'est present: ' + tuple[1])


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
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    print(filename)
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ') + option
        sys.exit(1)


if __name__ == '__main__':
    main()
