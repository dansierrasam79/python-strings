# find chars in lexicographical order
init_string = "thomson"
init_string2 = "thompson"
final_list = []
for char in init_string:
    for char2 in init_string2:
        if char == char2:
            final_list.append(char)
print(list(set(final_list)))
