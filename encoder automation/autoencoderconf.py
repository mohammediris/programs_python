

def displayCurrentConfig (EncoderIP):
    pass

def startTelnet(EncoderIP):
    pass

def closeTelnet():
    pass

def testTelnetPortOpen (EnocderIP):
    pass

def checkForMainMenu ():
    pass

def saveConfiguration ():
    pass

def enterConfig (multiIP, multiPort, videoInput):
    pass

def telnet():

    import getpass
    import telnetlib

    # Replace 'localhost' with the IP address or hostname of your Telnet server
    HOST = "localhost"
    user = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Create a Telnet object and connect to the server
    tn = telnetlib.Telnet(HOST)

    # Login to the server
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    # Send a command to the server
    tn.write(b"ls\n")

    # Read the response from the server
    response = tn.read_all().decode('ascii')
    print(response)

    # Close the connection
    tn.close()
