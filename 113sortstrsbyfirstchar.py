# sort by first letter of strings
init_string = "Red Green Black White Pink"
init_list = init_string.split(" ")
init_list2 = []
final_list2 = []
final_string = []
for item in init_list:
    init_list2.append(item[0])
final_list = sorted(init_list2)
for letter in final_list:
    for word in init_list:
        if letter == word[0]:
            final_list2.append(word)
final_string = ' '.join(final_list2)
print(final_string)
