# count vals in string
init_string = 'The%$quickbr2ownfox5jumps3over&the*lazydoG'
count_digit, count_lower, count_upper, count_special = 0,0,0,0
final_list = []
for letter in init_string:
    if letter.isdigit():
        count_digit += 1
    elif letter.islower():
        count_lower += 1
    elif letter.isupper():
        count_upper += 1
    elif letter in "!@#$%^&*":
        count_special +=1
final_list.append(count_digit)
final_list.append(count_lower)
final_list.append(count_upper)
final_list.append(count_special)
print(final_list)
