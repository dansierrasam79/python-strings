#decapitalize first letter of str
init_string = "Java Script"
final_string = ""

for i in range(0,len(init_string)):
    if i == 0:
        final_string += init_string[i].lower()
    else:
        final_string += init_string[i]
print(final_string)
