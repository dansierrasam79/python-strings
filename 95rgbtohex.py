# convert from rgb color to hexadecimal format
init_rgb_tup = (192, 192, 192)
red_comp = hex(init_rgb_tup[0])
green_comp = hex(init_rgb_tup[1])
blue_comp = hex(init_rgb_tup[2])
print(red_comp[2:] + green_comp[2:] + blue_comp[2:])
