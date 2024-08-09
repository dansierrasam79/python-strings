#convert hexadecimal color to RGB
init_string = "FF0000"
red = init_string[:2]
green = init_string[2:4]
blue = init_string[4:]
red_dec = int(red,16)
green_dec = int(green,16)
blue_dec = int(blue,16)
rgb_val = (red_dec,green_dec,blue_dec)
print(rgb_val)
