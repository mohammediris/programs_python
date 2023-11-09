import csv
import os

import PySimpleGUI as sg
import guipy_modules

# import re


# IPscheme = [['ZAK','76.80'],['UAD','75.16']]
file_dir = os.path.dirname(os.path.realpath('__file__'))
# file_name = file_dir + '/routes.csv'
# print (file_name)
file = open(file_dir + '/routes.csv')
# type(file)
csvreader = csv.reader(file)
header = next(csvreader)
IPscheme = []
for row in csvreader:
    IPscheme.append(row)
# print(IPscheme)
sg.theme('Default1')  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text('Select Site Name'), sg.DropDown([l[0] for l in IPscheme], key='-SITE-', default_value=IPscheme[0][0])],
    [sg.Button('Create Route'), sg.Button('Delete Route'), sg.Button('Print Route')],
    [sg.Button('Clear All Route'), sg.Button('Cancel')],
    [sg.Multiline("", size=(80, 20), autoscroll=True, reroute_stdout=True, reroute_stderr=True, key='-OUTPUT-')]
]

# Create the Window
window = sg.Window('Static Route', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    # print(event, values[0], values[1], values[2], values[3])
    # print(values["-SITE-"])
    for i in IPscheme:
        if i[0] == values["-SITE-"]:
            prefix = i[2]
    if event == 'Create Route':
        guipy_modules.createRoute(prefix, values["-SITE-"])
    elif event == 'Delete Route':
        guipy_modules.deleteRoute(prefix, values["-SITE-"])
    elif event == 'Print Route':
        guipy_modules.printRoute()
    elif event == 'Clear All Route':
        guipy_modules.clearAllRoute()

window.close()
