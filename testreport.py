# Calculates MAX and MIN insertion loss DATA at both wavelengths 1310nm and 1550nm
# makes chart output with series IL@1310nm and IL@1550nm
# across temperature changing

#  import os
from graphics import *
import tkinter as Tk


def select_file(window_message: str):
    # taking current directory  todo use tkinter for system wide file opening dialog
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
    win = GraphWin(window_message, 400, 24)  # todo 3rd choose as just draw new graph
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


def select_connector_amount():
    """ graphical window to select quantity of connectors on tested product
    12F (24) 24F (48) 48F (96) 96F(192)
    returns number of connectors as INT"""

    return 24


def choose_il_limit():
    """ choose limit graph window with input IL limit for one connector
    return limit as float"""

    return 0.08


def graph_output(result_values, max_min_values, il_limit=0.08, amount_of_connectors=24):
    """
    Outputs graphical windows with measures IL graph during temperature change sequence from -40 to +60 degree
    window size 900 x 1500, limit for 1 connect IL change 0,08dB
    :param result_values:  list of tuples with IL@1310nm, IL@1550nm, temperature in C
    :param max_min_values: tuple with list of min and max values in order IL@1310_MIN,
                                                                                IL@1310MAX, IL@1550MIN, IL@1550MAX
    :param il_limit 0,08dB as default  todo make function to choose limit
    :param amount_of_connectors = 24 as default  todo make graphical input for amount of connectors
    :return: none
    """
    if max_min_values[0] < max_min_values[2]:  # selecting minimum IL value
        min_value = max_min_values[0]
    else:
        min_value = max_min_values[2]
    if max_min_values[1] > max_min_values[3]:  # selecting maximum IL value
        max_value = max_min_values[1]
    else:
        max_value = max_min_values[3]
    point_dB = round(max_value - min_value)/800  # 800 points active chart area  point_dB = dB value for 1 point
    limit_1310_line_x = round((max_min_values[0] + amount_of_connectors * il_limit) / point_dB)
    limit_1550_line_x = round((max_min_values[2] + amount_of_connectors * il_limit) / point_dB)
    print(point_dB)
    print("il 1310 limit line at : ", limit_1310_line_x)
    print("il 1550 limit line at : ", limit_1550_line_x)



def main():
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

    il_file_name = select_file('Select Insertion Loss Log File')
    il_data_file = open(il_file_name, "r")  # file with IL data
    temp_file_name = select_file('Select Temperature Log File')
    temp_data_file = open(temp_file_name, "r")  # file with TEMP data
    if os.path.exists("results.txt"):
        answer = file_exist_warning('results.txt')
        if answer == 0:
            os.remove("results.txt")
            result_data_file = open("results.txt", "a")  # results file
        else:
            quit()

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

                # print(count_il, temp_f_count, il_date, temp_date, il_time, temp_time, il_1310wavelength_v_string,
                #      il_1550wavelength_v_string, temp_value)
                result_line = format(count_il) + " " + format(temp_f_count) + " " + il_date + " " + temp_time + " " + \
                    il_1310wavelength_v_string + " " + il_1550wavelength_v_string + " " + temp_value + "\n"
                # result_data_file.write(result_line)
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
    result_data_file.close()
    print(len(result_values))
    il_limit_value = 0.08
    graph_output(result_values, max_min_values, il_limit_value)


main()
