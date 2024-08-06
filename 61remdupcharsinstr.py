# remove duplicate chars from str
init_string = 'thequickbrownfoxjumpsoverthelazydog'
init_list = [letter for letter in init_string]
final_list = list(set(init_list))
print(final_list)
