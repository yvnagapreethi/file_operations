with open("with_file.txt", "w") as f:
    f.write("Very first line\n")
    f.write("Very second line\n")
    f.writelines("Very third line\n")
    f.write("Very fourth line\n")

with open("with_file.txt", "r") as f:
    for line in f.readlines():
        print(line)
