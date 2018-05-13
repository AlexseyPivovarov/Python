file = open("test.txt")
lib = open("lib.py", "w")
lib.write("vocabulary = {")
lib.write("".join({"'" + word.strip() + "': '', " for word in file}))
lib.write("}\n")
file.close()
lib.close()

