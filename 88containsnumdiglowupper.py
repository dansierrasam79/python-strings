#check if str contain caps,lower,min len and digit
init_string = "Constantin0ple"
init_list = []
if len(init_string) > 3:
    init_list.append(1)
for letter in init_string:
    if letter.isdigit():
        init_list.append(1)
    elif letter.islower():
        init_list.append(1)
    elif letter.isupper():
        init_list.append(1)
if len(init_list) < 4:
    print("Invalid String")
else:
    print("Valid String")
