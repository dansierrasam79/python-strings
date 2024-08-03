#get single str after swap
init_str = "Dan"
init_str2 = "Niks"
final_str = init_str + " " + init_str2
final_str2 = final_str[-2:] + final_str[2:-2] + final_str[:2]
print(final_str2)
