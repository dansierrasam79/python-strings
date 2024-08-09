# remove duplicate words from string
init_string = "Python Exercises Practice Solution Exercises"
init_list = init_string.split(" ")
final_list = []
for word in init_list:
    if word not in final_list:
        final_list.append(word)
print(final_list)
final_string = ' '.join(final_list)
print(final_string)
