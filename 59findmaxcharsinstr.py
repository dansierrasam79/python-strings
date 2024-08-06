# find max num of chars in string
from collections import Counter as cnt
init_string = 'the quick brown fox jumps over the lazy dog'
count_chars = cnt(init_string).most_common(1)
print(count_chars)
