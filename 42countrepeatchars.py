# count repeated chars in string
from collections import Counter as cnt
init_string = 'thequickbrownfoxjumpsoverthelazydog'
init_cnt = cnt(init_string)
init_list = init_cnt.most_common()
final_list = []
for tup in init_list:
    if tup[1] > 1:
        final_list.append(tup)
print(final_list)
