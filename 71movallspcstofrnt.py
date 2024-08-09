#move spaces to front of str
init_string = 'the quickbrown  foxjumpsoverthelazy dog '
final_str_list = []
for char in init_string:
    if char == " ":
        final_str_list.insert(0,char)
    else:
        final_str_list.append(char)
final_str = "".join(final_str_list)
print(final_str)
