#capitalize first letter and lowercase the rest
init_str = "Red Green WHITE"
init_list = init_str.split(" ")
final_list, final_str = [],0
for word in init_list:
    final_list.append(word[0].upper()+word[1:].lower())
final_str = ' '.join(final_list)
print(final_str)
