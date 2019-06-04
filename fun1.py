from datetime import datetime


def get_current_timestamp():
    date = datetime.now().strftime('%Y_%m_%d %H:%M:%S')
    return str(date)


# target_file_name = "Target" + get_current_timestamp() + ".txt"

with open("Target2019_06_03_13:27:45.txt", "w") as target_file:
    target_file.write("Hanuman")
