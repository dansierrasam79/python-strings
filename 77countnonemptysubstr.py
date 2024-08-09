#count number of substrs in string
init_string = 'thequickbrownfoxjumpsoverthelazydog'
substr_list = []
for i in range(0,len(init_string)):
    substr_list.append(init_string[0:i+1])
print(len(substr_list))
