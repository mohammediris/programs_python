import subprocess
import os
def printRoute():
    # os.system('route print')
    # output = subprocess.check_output('route print', shell=True)
    # add new function to refine the output
    output = subprocess.check_output('route print', stderr=subprocess.STDOUT, text=True)
    # output = subprocess.run('dir',shell=True)
    # text1 = output.find('Persistent Routes:') # find() outputs -1 value if the string is not found
    # text2 = output.find('=', text1)
    text1 = output.index("Persistent Routes:")  # index() throw error if the string is not found
    text2 = output.index("=", text1)
    # print(output.count("Routes"))
    print(output[text1: text2])
    # print(str(output))
    # if 'Persistent Routes:' in output:
    #    print("string is present")


def createRoute(IP, site):
    routeCommand = 'route -p add ' + IP + '.0.0 mask 255.255.0.0 ' + IP + '.40.254'
    # os.system(routeCommand) # this will simply send the string as command to cmd prompt
    # output = subprocess.check_output(routeCommand, shell=True)
    output = subprocess.check_output(routeCommand, stderr=subprocess.STDOUT, text=True)
    # text=True will make the output into string format
    # print(output)
    if output.find("OK!") != -1:
        # print("Persistent Route for {} is created!".format(site))
        print(f"Persistent Route for {site} is created!")  # this method is using fstring, add f infront of
        # quotes
    elif output.find("The route addition failed") != -1:
        # print("Persistent Route for {} already exist!".format(site))
        print(f"Persistent Route for {site} already exist!")


def deleteRoute(IP, site):
    routeCommand = 'route -p delete ' + IP + '.0.0 mask 255.255.0.0 ' + IP + '.40.254'
    # os.system(routeCommand)
    # output = subprocess.check_output(routeCommand, shell=True)
    output = subprocess.check_output(routeCommand, stderr=subprocess.STDOUT, text=True)
    # print(output)
    if output.find("OK!") != -1:
        print("Persistent Route for {} is deleted!".format(site))
    elif output.find("The route deletion failed") != -1:
        print("Persistent Route for {} doesn't exist!".format(site))


def clearAllRoute():
    output = subprocess.check_output('route print', stderr=subprocess.STDOUT, text=True) # text=True will change the
    # datatype of output from bytes to string

    text1 = output.find('Default')
    text2 = output.find('=', output.find('Default'))
    Proutes = output[text1 + 9:text2]
    # Proutes = output[output.find('Default') + 9:output.find('=', output.find('Default'))]
    Sroute = Proutes.split()
    Qroute = Sroute[::4]  # leave start index and stop index blank and give step size of 4
    # print(Proutes)
    # print(Qroute)
    for q in Qroute:
        routeCommand = 'route -p delete ' + str(q)
        subprocess.run(routeCommand)
    print("All additional routes cleared!")

