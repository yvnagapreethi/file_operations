# woking.py

import os

path = "C:\\Users\\Venkata_Naga_Preethi\\Desktop\\All PY Practise\\File operations\\"

text_files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            text_files.append(file)

print(text_files)

with open("Target_file.txt", "w") as target_file:
    for new_file in text_files:
        if new_file != "something.txt" and new_file != "Target_file.txt":
            print(new_file)
            target_file.write("Source: {} \n".format(new_file))
            with open(new_file, "r") as f:
                for line in f.readlines():
                    target_file.write(line)
            with open("something.txt", "r") as file:
                for line in file.readlines():
                    target_file.write(line)

# with open("Target_file.txt", "r") as f:
#     for line in f.readlines():
#         print(line)
