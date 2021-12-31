# Calculates MAX and MIN insertion loss DATA at both wavelengths 1310nm and 1550nm
# makes chart output with series IL@1310nm and IL@1550nm
# across temperature changing

#  import os
from graphics import *

# global variables

def select_file(window_message: str):
    # taking current directory
    os.chdir(os.path.dirname(__file__))
    # List all files in a directory using os.listdir
    file_names = list()
    base_path = os.getcwd()
    for entry in os.listdir(base_path):
        if os.path.isfile(os.path.join(base_path, entry)):
            file_names.append(entry)
    win = GraphWin(window_message, 400, len(file_names) * 24)
    line_num = 1
    for file_name in file_names:
        menu_rectangle = Rectangle(Point(2, 24 * line_num - 1), Point(398, 24 * line_num - 22))
        message = Text(Point(200, 24 * line_num - 11), file_name)
        message.setFace("arial")
        message.setStyle("bold")
        menu_rectangle.draw(win)
        message.draw(win)
        line_num += 1
    click_point = win.getMouse()  # pause for click in window
    xy_click = str(click_point)
    point_coordinates = xy_click.split()
    y_coordinate_temp = point_coordinates[1]
    y_coordinate = y_coordinate_temp.rstrip(')')
    y_coordinate_n = int(float(y_coordinate) // 24)
    win.close()

    return file_names[y_coordinate_n]


def file_exist_warning(file_name: str):
    window_message = file_name + " exists, do you wish to overwrite ?"
    win = GraphWin(window_message, 400, 24)
    menu_rectangle_yes = Rectangle(Point(2, 21), Point(198, 3))
    menu_rectangle_no = Rectangle(Point(202, 21), Point(398, 3))
    message_yes = Text(Point(101, 13), "YES")
    message_no = Text(Point(301, 13), "NO")
    message_yes.setFace("arial")
    message_yes.setStyle("bold")
    message_no.setFace("arial")
    message_no.setStyle("bold")
    menu_rectangle_yes.draw(win)
    menu_rectangle_no.draw(win)
    message_yes.draw(win)
    message_no.draw(win)
    click_point = win.getMouse()  # pause for click in window
    xy_click = str(click_point)
    point_coordinates = xy_click.split('(')
    y_coordinate_temp = point_coordinates[1].split('.')
    y_coordinate = int(y_coordinate_temp[0]) // 200
    win.close()
    return y_coordinate

def main():
    # variables
    il_data_line = temp_data_line = " "
    count = temp_f_count = 0  # counted source lines
    count_il_1310 = count_il_1550 = count_total = 0  # counted result lines
    il_time = il_date = temp_date = temp_time = temp_value = ""  # temporary strings to divide line apart
    il_line_parsed_to_list = temp_line_parsed_to_list = temp_line_time_part_list = il_line_time_part_list = list()
    il_1310wavelength_v_string = il_1550wavelength_v_string = ""
    result_line = ""
    temperature_hour = temperature_minute = il_minute = il_hour = ""  # temp ann il time strings
    pair_results = success = 0  # flags

    il_file_name = select_file('Select Insertion Loss Log File')
    il_data_file = open(il_file_name, "r")  # file with IL data
    temp_file_name = select_file('Select Temperature Log File')
    temp_data_file = open(temp_file_name, "r")  # file with TEMP data
    if os.path.exists("results.txt"):
        # todo:  graphical output input
        answer = file_exist_warning('results.txt')
        if answer == 0:
            os.remove("results.txt")
            result_data_file = open("results.txt", "a")  # results file
        else:
            quit()


    while il_data_line != "":
        il_data_line = il_data_file.readline()
        count_total = count_total + 1
        if il_data_line.startswith("8"):  # date number todo : real lines starts from 5
            il_line_parsed_to_list = il_data_line.split()
            count = count + 1
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

                print(count, temp_f_count, il_date, temp_date, il_time, temp_time, il_1310wavelength_v_string,
                      il_1550wavelength_v_string, temp_value)
                result_line = format(count) + " " + format(temp_f_count) + " " + il_date + " " + temp_time + " " + \
                    il_1310wavelength_v_string + " " + il_1550wavelength_v_string + " " + temp_value + "\n"
                result_data_file.write(result_line)

    print("sum of 1310 lines:", count_il_1310)
    print("sum of 1550 lines:", count_il_1550)
    print("usable sum of lines:", count)
    print("total sum of lines:", count_total)
    result_data_file.close()

main()