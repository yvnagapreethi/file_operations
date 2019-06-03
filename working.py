# woking.py

import os
from datetime import datetime


def get_current_timestamp():
    date = datetime.now().strftime('%Y_%m_%d %H_%M_%S')
    return str(date)


def copy_file_data():
    end_of_file_string = input("Please enter the string you want to display at the end of each file: ")
    path = input("Please enter the path: ")

    text_files = []

    for root, directory, files in os.walk(path):
        for file in files:
            if '.txt' in file:
                text_files.append(file)

    target_file_name = "Target" + get_current_timestamp() + ".txt"

    with open(target_file_name, "w") as target_file:
        for new_file in text_files:
            target_file.write("\nSource: {} \n".format(new_file))
            with open(new_file, "r") as f:
                for line in f.readlines():
                    target_file.write(line)
            target_file.write(end_of_file_string)


copy_file_data()
