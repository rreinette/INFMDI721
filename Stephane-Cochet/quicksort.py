# -*- coding: utf-8 -*-

def quicksort(ll):
    """ a sorting function equivalent to sort()"""
    if len(ll) <= 1:
        return ll
    else:
        pivot = ll.pop()
        less = []
        greater = []
        for x in ll:
            if x <= pivot:
                less.append(x)
            else:
                greater.append(x)
        return quicksort(less) + [pivot] + quicksort(greater)




