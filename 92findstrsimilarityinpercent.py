# find str similarity between two strings
init_string = "Python Exercises"
init_string2 = "Python Exercise"
str_length = len(init_string)
count_sim = 0
for i in range(0, len(init_string2)):
    if init_string2[i] == init_string[i]:
        count_sim += 1
print(count_sim/str_length)
