from easygui import *
from math import ceil, floor

def graph_window(il_limit_value, conn_amount):
    global value_point
    global max_min_values
    max_min_values = (0, 6.34, 0, 23.98)
    window_height = 900
    window_width = 1800
    delta_1310 = max_min_values[1] - max_min_values[0]
    delta_1550 = max_min_values[3] - max_min_values[2]

    if delta_1310 > delta_1550:
        max_value = ceil(delta_1310 + max_min_values[0])
        min_value = floor(max_min_values[0])
    else:
        max_value = ceil(delta_1550 + max_min_values[2])
        min_value = floor(max_min_values[2])
    dia_value = max_value - min_value
    test_limit = il_limit_value * conn_amount + min_value

    while (max_value % 5) != 0:
        max_value = max_value + 1
    while (min_value % 5) != 0:
        min_value = min_value - 1
    while (min_value % 5) != 0:
        min_value = min_value - 1
    dia_value = max_value - min_value
    grid_step = dia_value / 5




graph_window(0.08, 48)
