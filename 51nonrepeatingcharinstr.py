# find first non-repeating char
from collections import Counter as cnt
init_string = "constantinople"
count_chars = cnt(init_string)
count_dict = dict(count_chars)
final_list = []

for key,value in count_dict.items():
    if value == 1:
        final_list.append(key)
print("First non-repeating character: ", final_list[0])
