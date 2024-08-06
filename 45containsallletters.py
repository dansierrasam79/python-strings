# contains all letters of alphabet
alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                 'p','q','r','s','t','u','v','w','x','y','z']
init_string = 'thequickbrownfoxjumpsoverthelazydog'
init_string2 = "howareyou"
final_list = []
for letter in init_string2:
    for alphabet in alphabet_list:
        if letter.lower() == alphabet and letter not in final_list:
            final_list.append(letter)
if len(final_list) == 26:
    print("All letters exist")
else:
    print("Not all letters exist")
