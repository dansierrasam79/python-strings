#compute sum of digits in string
init_string = 'the1quick2brown3fox4jumps5over6the7lazy8dog'
init_list = [int(val) for val in init_string if val.isdigit()]
print("Sum of digits in str: ",sum(init_list))

