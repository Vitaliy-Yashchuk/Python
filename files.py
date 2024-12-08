# ----------- write file
with open("./assets/words.txt", "a") as f:
    f.write("New text...")
    # auto close

# ----------- read file
file1 = open("./assets/words.txt", "rt")

print(f"Content: {file1.read()}")

file1.close()
