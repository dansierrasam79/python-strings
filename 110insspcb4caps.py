# insert space before caps
init_string = "PythonExercises"
final_string = ""
for i in range(0, len(init_string)):
    if i != 0 and init_string[i].isupper():
        final_string += " " + init_string[i]
    else:
        final_string += init_string[i]
print(final_string)
