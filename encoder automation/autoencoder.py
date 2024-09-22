"""LIBRARIES"""

import pandas as pd
import telnetlib3
import re
import asyncio
import sys

"""FUNCTIONS"""

async def telnet_client_printconfig(encoderIP,port):
    try:
        reader, writer = await telnetlib3.open_connection(encoderIP, port)
        print("Telnet connection successful")
        
        response = await reader.read(100000)
        print(f"{response}")
        op = f"{response}"
        while not re.search('Save Settings',op): # loop to verify main menu
            writer.write('p\n') 
            response = await reader.read(100000)
        y = input("enter option: ")
        writer.write(y+'\n') 
        response = await reader.read(100000)
        print(f"{response}") 
        y = input("enter option: ")
        writer.write(y+'\n')  
        response = await reader.read(100000)
        print(f"{response}") 
        y = input("enter option: ")
        writer.write(y+'\n') 
        response = await reader.read(100000)
        print(f"{response}") 
        y = input("enter option: ")
        writer.write(y+'\n') 
        response = await reader.read(100000)
        print(f"{response}") 
        y = input("enter option: ")
        writer.write(y+'\n') 
        response = await reader.read(100000)
        print(f"{response}") 
        matchMultiIP = re.findall(r"11.*: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})",response)
        matchMultiPort = re.findall(r"12.*: (\d{1,5})",response)
        print(f"Multicast config for this input is {matchMultiIP[0]}:{matchMultiPort[0]}")
        writer.close()
    except (OSError, ConnectionRefusedError) as e:
        print(f"Failed to connect to {encoderIP}:{port} - {e}")
    except asyncio.TimeoutError:
        print(f"Connection to {encoderIP}:{port} timed out.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the writer is properly closed if it exists
        if 'writer' in locals():
            writer.close()
            

async def telnet_batchConfiguration(Encoders,port):
    for encoderIP in Encoders.keys():
        
        print(f"\nStart telnet connection to Encoder - {encoderIP}:{port}") 
        telnet_test(Encoders[encoderIP])  # dummy function to telnet
        print(f"Close telnet connection to Encoder - {encoderIP}:{port}\n") 
    

def readFromExcel(fileName):
    df = pd.read_excel(fileName)
    Encoders = {}

    for index, row in df.iterrows():
        if row.iloc[2] == 'S1708e':
            if row.iloc[3] not in Encoders:
                Encoders[row.iloc[3]] = {}
            Encoders[row.iloc[3]][row.iloc[1]] = {'multiIP' : row.iloc[4],'multiPort' : row.iloc[5]} 

    # for keys,values in Encoders.items():
    #     print(keys)
    #     for key, value in values.items():
    #         print(key, value)
            
    return Encoders

def telnet_test (encoder):
    print("call loop to check main menu")
    # response = await reader.read(100000)  
    # op = f"{response}"
    # while not re.search('Save Settings',op): # loop to verify main menu
    #     writer.write('p\n') 
    #     response = await reader.read(100000)
    print("enter option 6 for advanced menu")
    # writer.write('6\n') 
    # response = await reader.read(100000)
    print("enter option 6 input menu")
    # writer.write('6\n') 
    # response = await reader.read(100000)
    for encInput, multicastDetails in encoder.items():
        print(f"enter input number - {encInput}")
        # writer.write(f'{encInput}\n') 
        # response = await reader.read(100000)
        print("enter option 1 for encoder1 in input menu")
        # writer.write('1\n') 
        # response = await reader.read(100000)
        print("enter option 11 for changing multicast IP")
        # writer.write('11\n') 
        # response = await reader.read(100000)
        print(f"enter new multicast IP - {multicastDetails['multiIP']}")
        # writer.write(f'{multicastDetails['multiIP']}\n') 
        # response = await reader.read(100000)
        print("enter option 12 for changing multicast Port")
        # writer.write('12\n') 
        # response = await reader.read(100000)
        print(f"enter new multicast Port - {multicastDetails['multiPort']}")
        # writer.write(f'{multicastDetails['multiPort']}\n') 
        # response = await reader.read(100000)
        print("enter option p to go back to input menu")
        # writer.write('p\n') 
        # response = await reader.read(100000)
        print("enter option p to go back to advanced menu")
        # writer.write('p\n') 
        # response = await reader.read(100000)
          

"""VARIABLES"""

fileName = 'encoder list.xlsx'
encoderIP = 'localhost'
port = 8023
Encoders = {}
appMenu = ('''
***********************************************************
        Verint 1708 Encoder Multicast Config Tool
***********************************************************
Select from Menu
       1. Print config for single encoder
       2. Print config to excel for list of encoders
       3. Input config from Excel file
       4. Quit
***********************************************************
Enter your option: ''')
optionsMenu_1 = ('''
***********************************************************
        Verint 1708 Encoder Multicast Config Tool
***********************************************************
Select from Menu
       1. Print config for single encoder
       2. Print config to excel for list of encoders
       3. Input config from Excel file
       4. Quit
***********************************************************
You selected option 1
Enter Encoder IP: ''')
optionsMenu_2 = ('''
***********************************************************
        Verint 1708 Encoder Multicast Config Tool
***********************************************************
Select from Menu
       1. Print config for single encoder
       2. Print config to excel for list of encoders
       3. Input config from Excel file
       4. Quit
***********************************************************
You selected option 2
Enter filename of encoder list: ''')
optionsMenu_3 = ('''
***********************************************************
        Verint 1708 Encoder Multicast Config Tool
***********************************************************
Select from Menu
       1. Print config for single encoder
       2. Print config to excel for list of encoders
       3. Input config from Excel file
       4. Quit
***********************************************************
You selected option 3
Enter filename of encoder config: ''')

"""MAIN CODE"""

Option = input (appMenu)
if Option == '1':
    encoderIP = input (optionsMenu_1)
    asyncio.run(telnet_client_printconfig(encoderIP,port))
elif Option == '3':
    fileName = input (optionsMenu_2)
    Encoders = readFromExcel(fileName)
    asyncio.run(telnet_batchConfiguration(Encoders,port))
elif Option == '2':
    pass
else:
    sys.exit(1)




