# remove odd index values in string
init_string = "constantinople"
final_string = ""

for i in range(0, len(init_string)):
    if i % 2 != 0:
        continue;
    else:
        final_string += init_string[i]
print(final_string)
