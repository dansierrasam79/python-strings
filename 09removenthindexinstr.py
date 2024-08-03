# remove non-empty string of nth index
init_string =  "constantinople"
final_string = ""
n = 5
for i in range(0, len(init_string)):
    if i == n-1:
        continue;
    else:
        final_string += init_string[i]
print(final_string)
