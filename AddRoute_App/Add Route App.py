import csv
import os
import subprocess
import PySimpleGUI as sg


# import re


def printRoute():
    # os.system('route print')
    # output = subprocess.check_output('route print', shell=True)
    # add new function to refine the output
    output = subprocess.check_output(
        'route print', stderr=subprocess.STDOUT, text=True)
    # output = subprocess.run('dir',shell=True)
    # text1 = output.find('Persistent Routes:') # find() outputs -1 value if the string is not found
    # text2 = output.find('=', text1)
    # index() throw error if the string is not found
    text1 = output.index("Persistent Routes:")
    text2 = output.index("=", text1)
    # print(output.count("Routes"))
    op_str_split = output[text1: text2].split()
    op_iter = iter(op_str_split)
    op_len = len(op_str_split)
    print(f"{next(op_iter)} {next(op_iter)}")
    print("=================================================================")
    print(f"{next(op_iter)} {next(op_iter):<12}{next(op_iter):>12}\t{next(op_iter)} {next(op_iter):>9}\t{next(op_iter):^9}")
    print("=================================================================")
    for i in range((op_len-8)//4):
        print(
            f"{next(op_iter):>12}\t{next(op_iter):>16}\t{next(op_iter):>16}\t{next(op_iter):^10}")

    print("=================================================================")
    # print(output[text1: text2])
    # print(str(output))
    # if 'Persistent Routes:' in output:
    #    print("string is present")


def createRoute(IP, site):
    routeCommand = 'route -p add ' + IP + '.0.0 mask 255.255.0.0 ' + IP + '.40.254'
    # os.system(routeCommand) # this will simply send the string as command to cmd prompt
    # output = subprocess.check_output(routeCommand, shell=True)
    output = subprocess.check_output(
        routeCommand, stderr=subprocess.STDOUT, text=True)
    # text=True will make the output into string format
    # print(output)
    if output.find("OK!") != -1:
        # print("Persistent Route for {} is created!".format(site))
        # this method is using fstring, add f infront of
        print(f"Persistent Route for {site} is created!")
        # quotes
    elif output.find("The route addition failed") != -1:
        # print("Persistent Route for {} already exist!".format(site))
        print(f"Persistent Route for {site} already exist!")


def deleteRoute(IP, site):
    routeCommand = 'route -p delete ' + IP + \
        '.0.0 mask 255.255.0.0 ' + IP + '.40.254'
    # os.system(routeCommand)
    # output = subprocess.check_output(routeCommand, shell=True)
    output = subprocess.check_output(
        routeCommand, stderr=subprocess.STDOUT, text=True)
    # print(output)
    if output.find("OK!") != -1:
        print("Persistent Route for {} is deleted!".format(site))
    elif output.find("The route deletion failed") != -1:
        print("Persistent Route for {} doesn't exist!".format(site))


def clearAllRoute():
    output = subprocess.check_output(
        'route print', stderr=subprocess.STDOUT, text=True)  # text=True will change the
    # datatype of output from bytes to string

    text1 = output.find('Default')
    text2 = output.find('=', text1)
    Proutes = output[text1 + 9:text2]
    Sroute = Proutes.split()
    # leave start index and stop index blank and give step size of 4
    Qroute = Sroute[::4]
    # print(Proutes)
    # print(Qroute)
    for q in Qroute:
        routeCommand = 'route -p delete ' + str(q)
        subprocess.run(routeCommand)
    print("All additional routes cleared!")


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
    [sg.Text('Select Site Name'), sg.DropDown([l[0]
                                               for l in IPscheme], key='-SITE-', default_value=IPscheme[0][0])],
    [sg.Button('Create Route'), sg.Button(
        'Delete Route'), sg.Button('Print Route')],
    [sg.Button('Clear All Route'), sg.Button('Cancel')],
    [sg.Multiline("", size=(80, 20), autoscroll=True,
                  reroute_stdout=True, reroute_stderr=True, key='-OUTPUT-')]
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
        createRoute(prefix, values["-SITE-"])
    elif event == 'Delete Route':
        deleteRoute(prefix, values["-SITE-"])
    elif event == 'Print Route':
        printRoute()
    elif event == 'Clear All Route':
        clearAllRoute()

window.close()
