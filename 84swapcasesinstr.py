#swap cases in str
init_string = "Constantinople"
final_string = ""
if init_string[0].isupper() and init_string[-1].islower():
    final_string = init_string[0].lower() + init_string[1:-1] + init_string[-1].upper()
    
print(final_string)
