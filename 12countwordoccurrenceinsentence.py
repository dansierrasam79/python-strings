# count word occurence in sentence
from collections import Counter as cnt
sentence = "The quick brown fox jumps over the lazy doggies".lower()
sentence_list = sentence.split(" ")
cnt_values = cnt(sentence_list)
print(cnt_values)
