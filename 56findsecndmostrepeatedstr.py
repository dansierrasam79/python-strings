# find second most repeated string in sentence
from collections import Counter as cnt
init_string = 'the quick brown the dog jumps over the lazy dog'
init_list = init_string.split(" ")
count_words = cnt(init_list).most_common()
final_count_dict = dict(count_words)
final_count_list = list(final_count_dict.keys())
print("Second most repeated string: ", final_count_list[1])
