import os
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import messagebox


def open_file(message):
    dialog_title = message
    fo_get_window = Tk()
    fo_get_window.withdraw()
    fo_get_window.title('TestGraph')
    file = askopenfile(mode='r', filetypes=[('TEXT files', 'txt')], title=dialog_title)
    if file is not None:
        filename = format(file).split("'")
        basepath = filename[1]
        filename = filename[1].split("/")
        filename = filename[len(filename) - 1]
        basepath = basepath[0:(len(basepath) - len(filename))]
    else:
        exit()
    fo_get_window.destroy()
    return filename, basepath


def il_get_value():
    """
    return float value
    """
    il_get_window = Tk()
    il_get_window.title('TestGraph')
    il_string = StringVar()
    number_float = 0

    def getvalue():
        try:
            number_float = float(il_string.get())
            il_get_window.destroy()
        except:
            messagebox.showerror("Not a number!", "Decimal number format should be 0.00")

    Label(il_get_window, text="IL limit for 1 connector (0.08 by default) : ").grid(row=0, sticky=W)  # label
    Entry(il_get_window, textvariable=il_string).grid(row=0, column=1, sticky=E)  # entry textbox
    WSignUp = Button(il_get_window, text="Apply", command=getvalue).grid(row=0, column=4, sticky=W)  # button

    il_get_window.mainloop()

    if len(il_string.get()) == 0:
        return 0.08
    else:
        return float(il_string.get())


def parse_files(il_file_name, temp_file_name, result_file_name, ):
    """
    takes 2 files as parameters, parses these and return tuple list as
    values across temperature changing, max and min values for IL at both wavelengths,
    :param il_data_file: Insertion loss log file
    :param temp_data_file: temperature changing log file
    :return: list of tuples [il@1310nm, il@1550nm, tempvalue],
                            max_min_values[min@1310nm, max@1310nm, min@1550nm,max@1550nm]
    """
    # variables
    il_data_line = temp_data_line = " "
    count_il = temp_f_count = 0  # counted source lines
    count_il_1310 = count_il_1550 = count_total = 0  # counted result lines
    il_time = il_date = temp_date = temp_time = temp_value = ""  # temporary strings to divide line apart
    il_line_parsed_to_list = temp_line_parsed_to_list = temp_line_time_part_list = il_line_time_part_list = list()
    il_1310wavelength_v_string = il_1550wavelength_v_string = ""
    result_line = ""
    temperature_hour = temperature_minute = il_minute = il_hour = ""  # temp ann il time strings
    pair_results = success = 0  # flags
    result_values = list()
    value_point = (0, 0, 0)
    max_min_values = (0, 0, 0, 0)  # min_il_1310_value, max_il_1310_value, min_il_1550_value, max_il_1550_value

    # opening files

    il_data_file = open(il_file_name, "r")  # File with IL log data
    temp_data_file = open(temp_file_name, "r")  # File with temperature log data
    if len(result_file_name) > 1:
        result_data_file = open(result_file_name, "a")
        saveresults = True

    while il_data_line != "":
        il_data_line = il_data_file.readline()
        count_total = count_total + 1
        if count_total >= 5 and len(il_data_line) > 1:   # result lines in IL data log file started from 5,
            il_line_parsed_to_list = il_data_line.split()
            count_il = count_il + 1
            if il_line_parsed_to_list[6] == "1310nm":
                count_il_1310 = count_il_1310 + 1
                il_1310wavelength_v_string = il_line_parsed_to_list[10]
            elif il_line_parsed_to_list[6] == "1550nm":
                count_il_1550 = count_il_1550 + 1
                il_1550wavelength_v_string = il_line_parsed_to_list[10]
                pair_results = 1
            if pair_results == 1:  # both of IL results loaded
                pair_results = 0
                il_date = il_line_parsed_to_list[0]
                il_line_time_part_list = il_line_parsed_to_list[1].split(":")
                il_hour = int(il_line_time_part_list[0])
                il_minute = int(il_line_time_part_list[1])
                if il_line_parsed_to_list[2] == "PM":
                    if il_hour < 12:
                        il_hour = il_hour + 12
                elif il_hour == 12:
                    il_hour = 0
                il_time = format(il_hour) + ":" + format(il_minute)  # making control value
                # try to get right temperature value from temperature log file
                while temp_data_line != "":  # not eof yet
                    try:
                        temp_data_line = temp_data_file.readline()
                        temp_f_count = temp_f_count + 1  # temp file line number
                        temp_line_parsed_to_list = temp_data_line.split()
                        temp_date = temp_line_parsed_to_list[0]
                        temp_time = temp_line_parsed_to_list[1]
                        temp_value = temp_line_parsed_to_list[2]
                        temp_line_time_part_list = temp_time.split(":")
                        temperature_hour = int(temp_line_time_part_list[0])
                        temperature_minute = int(temp_line_time_part_list[1])
                        if temperature_hour == il_hour and temperature_minute == il_minute:
                            # print(il_date, count_1550, temp_f_count,count_total, il_hour, t_hour,   il_min,  t_min)
                            break
                    except:
                        break

                print(count_il, temp_f_count, il_date, temp_date, il_time, temp_time, il_1310wavelength_v_string,
                      il_1550wavelength_v_string, temp_value)
                result_line = format(count_il) + " " + format(temp_f_count) + " " + il_date + " " + temp_time + " " + \
                    il_1310wavelength_v_string + " " + il_1550wavelength_v_string + " " + temp_value + "\n"
                if saveresults:
                    result_data_file.write(result_line)
                value_point = float(il_1310wavelength_v_string), float(il_1550wavelength_v_string), float(temp_value)
                # max and min values to be stored for both wavelengths
                # min_il_1310_value, max_il_1310_value, min_il_1550_value, max_il_1550_value

                if value_point[0] < max_min_values[0]:  # min_il_1310_value
                    max_min_values = value_point[0], max_min_values[1], max_min_values[2], max_min_values[3]
                elif value_point[0] > max_min_values[1]:  # max_il_1310_value
                    max_min_values = max_min_values[0], value_point[0], max_min_values[2], max_min_values[3]
                if value_point[1] < max_min_values[2]:  # min_il_1550_value
                    max_min_values = max_min_values[0], max_min_values[1], value_point[1],  max_min_values[3]
                elif value_point[1] > max_min_values[3]:  # max_il_1550_value
                    max_min_values = max_min_values[0], max_min_values[1], max_min_values[2], value_point[1]
                result_values.append(value_point)

    print("1310 nm IL delta = ", max_min_values[1] - max_min_values[0])
    print("1550 nm IL delta = ", max_min_values[3] - max_min_values[2])
    print("sum of 1310 lines:", count_il_1310)
    print("sum of 1550 lines:", count_il_1550)
    print("usable sum of lines:", count_il)
    print("total sum of lines:", count_total)
    # result_data_file.close()
    # print(len(result_values))


def file_exists_warning(path, file_name="results.txt"):
    """
    takes path and filename as a parameter
    asks about overwrite result file
    if yes, just return 0
    if not, return 1, don't update the result file
    if new file, return full filename including path
    """
    # variables
    filename = list()
    file_exists_window = Tk()
    file_exists_window.withdraw()
    message = file_name + " exists, do you wish to overwrite ? press cancel to skip saving result"
    answer = messagebox.askyesnocancel("TestGraph", message)
    file_exists_window.destroy()
    if answer is True:
        return 0
    elif answer is False:
        save_as_window = Tk()
        save_as_window.title('TestGraph')
        save_as_window.withdraw()
        result_file_name = asksaveasfile(mode='w', filetypes=[('Text Document', '*.txt')], defaultextension='txt')
        filename = format(result_file_name).split("'")
        if result_file_name is not None:
            result_file_name.close()
            file_name = filename[1]
            os.remove(file_name)
            file_name = file_name if ".txt" in file_name else file_name + ".txt"
            return file_name
        else:
            return 1
    elif answer is not None:
        return 1


def main():
    graph_values = list()
    graph_max_min_values = (0, 0, 0, 0)

    il_limit_value = il_get_value()  # get insertion loss limit value for 1 connector,

    """Main window"""
    root = Tk()
    root.title('Temperature cycling test log file parser')
    root.resizable(False, False)
    root.geometry('1800x900')
    il_file_name, file_base_path = open_file("Select Insertion Loss log file")
    il_file_name = file_base_path + il_file_name
    temp_file_name, file_base_path = open_file("Select Temperature log file")
    temp_file_name = file_base_path + temp_file_name

    if os.path.exists("results.txt"):
        answer = file_exists_warning(file_base_path, 'results.txt')
        if answer == 0:
            os.remove("results.txt")
            result_file_name = file_base_path + "results.txt"
            #  # file handling to parse_files
        elif answer == 1:
            result_file_name = ""   # no need to save any results
            quit()
        elif len(answer) > 2:
            print("here should be new result_file_name")
            result_file_name = answer
            print(answer)
    else:
        result_file_name = file_base_path + 'results.txt'

    print(il_file_name, temp_file_name, result_file_name, il_limit_value)
    graph_values, graph_max_min_values = parse_files(il_file_name, temp_file_name, result_file_name)

    root.mainloop()


main()
