from graphics import *
from math import ceil, floor

def graph_window(il_limit_value, conn_amount):

    global value_point
    global max_min_values
    max_min_values = (0, 6.34, 0, 23.98)
    window_height = 900
    window_width = 1800
    delta_1310 = max_min_values[1] - max_min_values[0]
    delta_1550 = max_min_values[3] - max_min_values[2]

    if delta_1310  > delta_1550:
        max_value = ceil(delta_1310 + max_min_values[0])
        min_value = floor(max_min_values[0])
    else:
        max_value = ceil(delta_1550 + max_min_values[2])
        min_value = floor(max_min_values[2])
    dia_value = max_value - min_value
    test_limit = il_limit_value * conn_amount + min_value

    while (max_value % 5) != 0:
        max_value = max_value + 1
    while(min_value % 5) != 0:
        min_value = min_value -1
    while (min_value % 5) != 0:
        min_value = min_value - 1
    dia_value = max_value - min_value
    grid_step = dia_value / 5
    main_window = GraphWin("Temperature cycling test chart", window_width, window_height)
    main_window.setBackground("white")
    # makes grid
    for x in range(7):
        Temperature_Line = Line(Point(85, x * 150 - 100), Point(1785, x * 150 - 100))
        Temperature_Line.draw(main_window)
    # makes limitline
    limit_line_x = window_height - round((window_height - 150) / dia_value * (test_limit - min_value)) - 100
    IL_Limit_Line = Line(Point(85, limit_line_x), Point(1785, limit_line_x))
    IL_Limit_Line.draw(main_window)
    IL_Limit_Line.setFill("red")
    y = 168
    x = limit_line_x - 8
    txt = "{price:.2f}  dB test limit"
    mes = txt.format(price= test_limit)
    message = Text(Point(y, x), mes)
    message.setFace("arial")
    message.setSize(12)
    message.setStyle("bold")
    message.setFill("red")
    message.draw(main_window)

    x = 65
    y = 1762
    for mes in ("+60 °C", "+40 °C", "+20°C", "  0 °C", "-20 °C", "-40 °C"):
        message = Text(Point(y, x), mes)
        message.setFace("arial")
        message.setSize(12)
        message.setStyle("bold")
        message.draw(main_window)
        x = x + 150
    y = 38
    x = 50
    for z in range(6):
        txt = "{price:.2f}  dB"
        mes = txt.format(price= max_value)
        print(mes)
        max_value = max_value - grid_step
        message = Text(Point(y, x), mes)
        message.setFace("arial")
        message.setSize(12)
        message.setStyle("bold")
        message.draw(main_window)
        x = x + 150

    main_window.getMouse()  # pause for click in window
    main_window.close()


graph_window(0.1, 48)
