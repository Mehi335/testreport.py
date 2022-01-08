
from tkinter.filedialog import askopenfile


def open_file():
    file = askopenfile(mode='r', filetypes=[('TEXT files', 'txt')])
    if file is not None:
        filename = format(file).split("'")
        filename = filename[1].split("/")
        return filename[len(filename)-1]
    else:
        exit()


il_file_name = open_file()
print(il_file_name)
il_data_file = open(il_file_name, "r")
temp_file_name = open_file()
print(temp_file_name)
temp_data_file = open(temp_file_name, "r")

