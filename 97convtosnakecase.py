# convert to snake case
init_string = "foobar"
final_string = ""
center_pt = int(len(init_string)/2)
for i in range(0,len(init_string)):
    if center_pt != i:
        final_string += init_string[i]
    else:
        final_string += "_" + init_string[i]
print(final_string)
