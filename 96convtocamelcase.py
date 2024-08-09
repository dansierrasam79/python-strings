#convert to camelcase
init_string = "foobar"
center_pt = int(len(init_string)/2)
final_string = ""
for i in range(0, len(init_string)):
    if i != center_pt:
        final_string += init_string[i]
    else:
        final_string += init_string[i].capitalize()
print(final_string)
