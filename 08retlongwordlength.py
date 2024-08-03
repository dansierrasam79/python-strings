# return longer word and length
init_list = ["The","quick","brown","fox","jumps","over","the","lazy","doggies"]
max_len_word = ""
max_len = 0
for item in init_list:
    word_len = len(item)
    if word_len>max_len:
        max_len = word_len
        max_len_word = item
print(max_len_word, max_len)
