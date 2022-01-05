# 파이썬 망각자의 Languages 교란 작전

# 애너그램
from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)

anagram("abcd3", "3acdb") # True
