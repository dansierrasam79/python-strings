#replace words with length > 5 with hash signs
init_str = "Count the lowercase letters in the said list of words:"
init_list = init_str.split(" ")
final_list = []
final_str = ""
for word in init_list:
    if len(word) < 5:
        final_list.append(word)
    else:
        final_list.append('#'*len(word))
final_str = ' '.join(final_list)
print(final_str)
