'''
Libraries
'''

import netmiko
import re
import sys
# from getpass import getpass
# from queue import Queue
# import signal
# signal.signal(signal.SIGFPE,signal.SIG_DFL)
# signal.signal(signal.SIGINT,signal.SIG_DFL)
'''
Function defenitions
'''

'''
Variable declarations
'''
 
device = {
        "ip" :"10.10.10.3",
        "device_type" : "cisco_ios",
        "username" : "cisco",
        "password" : "cisco"
        }
commands_file = "commands"
outputs = []
'''
Main Code
'''

ipaddress = input("Enter IP Address : \n")
username = input("Enter username : \n")
password = input("Enter password : \n")
commands_file = input("Enter filename for commands : \n")
device = {
        "ip" :ipaddress,
        "device_type" : "cisco_ios",
        "username" : username,
        "password" : password
        }
timeout_duration = 60
try:
    print(f'Connecting to device {device["ip"]}')
    connection = netmiko.ConnectHandler(**device) # establishing SSH connection
    connection.send_command('ter len 0')
    hostname = re.search(r"hostname (.+)",connection.send_command('sh run | include hostname'))
    
    with open (commands_file+'.txt','r') as file:
        commands = file.readlines()
        for command in commands:   
            print("\nexecuting command :- "+command+"\n")
            try:
                out = connection.send_command(command,read_timeout=timeout_duration)
                print(out)
                outputs.append(out)
            except (netmiko.exceptions.ReadTimeout) as readout_error:
                print (f"Executing command : {command} takes more than {timeout_duration} seconds. Program returned a Readout Error")
                print ("Saving outputs to file...")
                # sys.exit()
    connection.disconnect()
    with open (hostname.group(1)+'.txt','w') as result:
        result.writelines("ATP Results for " + hostname.group(1))
        result.writelines("\n================================================================================")
        for output in outputs:
            result.writelines("\noutput of command :" + commands[outputs.index(output)]+'\n')   
            result.writelines("--------------------------------------------------------------------------------\n")
            result.writelines(output)
            result.writelines("\n================================================================================")
except (netmiko.exceptions.NetmikoAuthenticationException,
        netmiko.exceptions.NetmikoTimeoutException) as error:
    error_message = re.match(".*",str(error)).group(0)
    print(f'Cannot connect to {device["ip"]} due to {error_message}')
    print('================================================================================') 

