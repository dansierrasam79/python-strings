# swap commas and dots
init_string = "32.054,23"
final_string = ""
comma, dot = 0,0
dot = "."
comma = ","
for num in init_string:
    if num == dot:
        final_string += ","
    elif num == comma:
        final_string += "."
    else:
        final_string += num
print(final_string)

