# ------------ dictionaries ------------

users = { 1200: "Vlad Tm", 555: "Nazar Bla", 9800: "Luda Buda" }


users[555] = "Viktor"

if 555 in users:
    print("Yes")
else: print("No")

for i in users:
    print(f"{i} - {users[i]}")

for key, val in users.items():
    print(f"{key} - {val}")

users.pop(1200)

print(f"Users: {len(users)}")