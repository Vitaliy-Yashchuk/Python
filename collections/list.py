# ------ list: dynamic size, can modify
colors = ["red", "green", "darkblue", "yellow", "darkcyan"]

for c in colors:
    print(c)

colors[0] = "yellow"

if "purple" not in colors:
    colors.append("purple")

# ---- shallow copy
shallowList = colors
colors[1] = "superpuperwhite"

# ---- deep copy
deepList = colors.copy()
colors[2] = "blablacolor"

print(f"Colors: {colors}")
print(f"Shallow: {shallowList}")
print(f"Deep: {deepList}")

# --- deleting
colors.pop(3)   # remove fourth
colors.pop()    # remove last
colors.pop(-1)  # remove last

if "black" in colors:
    colors.remove("black")

colors.extend(["darkblack", "darksuperblack", "megadark"])

darks = filter(lambda x: "dark" in x, colors)

print("------ Dark colors ------")
for x in darks:
  print(x)


mixed = [23, "red", True, [1, 2, 3], lambda x: x * x, 343.5, { 1, 2, 3 }]

