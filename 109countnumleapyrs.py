leap_yr = [1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
init_str = "2000-2020"
frm_yr = int(init_str[:4])
to_yr = int(init_str[5:])
count_lpyr = 0
for lpyr in leap_yr:
    if lpyr >= frm_yr and lpyr <= to_yr:
        count_lpyr += 1
print(count_lpyr)
