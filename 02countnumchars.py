#count num of chars
from collections import Counter as cnt
init_str = 'google.com'
init_list = [letter for letter in init_str]
print(init_list)
count_letters = cnt(init_list)
print(count_letters)
