# first repeating char in string
from collections import Counter as cnt
init_string = "constantinople"
count_dict = dict(cnt(init_string))
final_list = []
print(count_dict)
for key,value in count_dict.items():
    if value > 1:
        final_list.append(key)
print("First repeated char in str: ", final_list[0])
