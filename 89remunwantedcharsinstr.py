# remove unwanted chars from str
init_string = "Pyth*^on Exercis^es"
final_string = ""
for letter in init_string:
    if letter not in "!@#$%^&*":
        final_string += letter
print(final_string)
