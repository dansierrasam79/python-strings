# delete all occurence of char in str
init_string = 'thequickbrownfoxjumpsoverthelazydog'
init_char = "o"
final_string = ""
for letter in init_string:
    if letter != init_char:
        final_string += letter
print(final_string)
