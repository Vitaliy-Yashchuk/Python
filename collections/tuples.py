# ------ tuple: fixed size, cannot modify
coord = (1, 10)

# coord[0] += 1 - error

location = (12.564564, 10.45454, "Rivne", "Ukraine")

print("Country: " + location[3])

lon, lat, city, country = location

print("City: " + city)
