import os
from graphics import *

il_file_name = ''
temp_file_name = ''


def select_file(window_message: str):
    # taking current directory
    os.chdir(os.path.dirname(__file__))
    # List all files in a directory using os.listdir
    file_names = list()
    point_coordinates = list()
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
    win.close()
    xy_click = str(click_point)
    point_coordinates = xy_click.split()
    y_coordinate_temp =  point_coordinates[1]
    y_coordinate = y_coordinate_temp .rstrip(')')
    y_coordinate_n = int(float(y_coordinate) // 24)
    return(file_names[y_coordinate_n])


il_file_name = select_file('Select Insertion Loss Log File')
temp_file_name = select_file('Select Temperature Log File')

print(il_file_name)
print(temp_file_name)