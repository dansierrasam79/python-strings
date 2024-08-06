#find first repeated word in string
init_string = 'the quick brown dog jumps over the lazy dog'
init_list = init_string.split(" ")
for word in init_list:
    count = 0
    for word2 in init_list:
        if word == word2:
            count += 1
    if count >= 2:
        print("First repeated word: ",word)
        break;
