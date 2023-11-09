import customtkinter
import socket
import threading
from queue import Queue
import smvalidate # importing custom module for input validation, verify the module is available in the same folder

target = ''
queue = Queue()
port_list = []
open_ports = []
closed_ports = []

def portscan(target,port):
    '''
    This code block will open a tcp socket for the ipv4 address and port specified in the argument
    if connection is success, it will return True, else it will return Error.
    using try-except block, a False boolean is returned when there is a connection fail error.
    '''
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False   
    
def worker():
    '''
    this fuction gets each value from the queue, and calls the portscan fuction
    until the queue is empty
    '''
    while not queue.empty():
        port = queue.get()
        if portscan(target,port):
            print (f'\nport {port} is open')
            open_ports.append(port)
        else:
            print(f'\nport {port} is closed')
            closed_ports.append(port)

def fill_queue(port_list):
    '''
    this function will fill the queue with port numbers in the port_list array.
    worker function will call each value in first come first server order,
    any queue empties the value as soon as it is called.
    we use queue instead of array, to avoid same value being called by 
    multiple 'woker' function running parallely using threading.
    '''
    for port in port_list:
        queue.put(port)

def button_function():
    '''
    This function is executed when the START button is pressed
    '''
    label_status.configure(text="Program Running")
    textbox.delete("0.0", "end")
    app.update()
    global target
    global port_list
    global open_ports
    global closed_ports
    open_ports,closed_ports = [],[]
    target = entry_target_host.get()
    from_port = entry_port_range_from.get()
    to_port = entry_port_range_to.get()
    try:
        if (smvalidate.validate_website_address(target) or smvalidate.validate_ipv4_address(target)): # vaildates if the given input is a website or ipv4 address
            port_list = list(range(int(from_port),int(to_port)))
            fill_queue(port_list)
            '''
            following code will create multiple threads to run the 'worker' function parallely 
            number of threads will depend on the port range specified in the input
            if the port range is exceeding 1000, the thread count will limit to a fixed value of 1000
            '''
            thread_list = []
            if len(port_list) <= 1000:
                thread_count = len(port_list)
            else:
                thread_count = 1000 
            for t in range (thread_count):
                thread = threading.Thread(target=worker)
                thread_list.append(thread)
            for thread in thread_list:
                thread.start()
            for thread in thread_list:
                thread.join()

            open_ports.sort()
            textbox.delete("0.0", "end")
            textbox.insert("0.0", '\n'.join(str(e) for e in open_ports))
            label_status.configure(text="Program Completed")
            app.update()
        else:
            label_status.configure(text="Please verify your inputs")
            app.update()
    except:
        label_status.configure(text="ERROR! Please verify your inputs")
        app.update()
'''
Following is the code for UI elements
Here I have used customTkinter module to make use of the modern UI elements
'''
customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  
app.geometry("350x370")
app.title("Port Scanner - schoolofiris.com")

button_start = customtkinter.CTkButton(master=app, text="START", command=button_function, width=200)
button_start.grid(row=2,column=1,columnspan=3,pady=10)
entry_target_host = customtkinter.CTkEntry(app, placeholder_text="Target host", width=200)
entry_target_host.grid(row=0,column=1,columnspan=4)
label_host_name = customtkinter.CTkLabel(app, text="Target Host", fg_color="transparent", width=100)
label_host_name.grid(row=0,column=0,pady=10)
label_port_range_from = customtkinter.CTkLabel(app, text="Port Range", fg_color="transparent", width=100)
label_port_range_from.grid(row=1,column=0,pady=10,padx=10)
entry_port_range_from = customtkinter.CTkEntry(app, width=85)
entry_port_range_from.grid(row=1,column=1,pady=10)
label_port_range_to = customtkinter.CTkLabel(app, text="To", fg_color="transparent")
label_port_range_to.grid(row=1,column=2,pady=10,padx=5)
entry_port_range_to = customtkinter.CTkEntry(app, width=90)
entry_port_range_to.grid(row=1,column=3,pady=10)
label_port_range_from = customtkinter.CTkLabel(app, text="Open Ports", fg_color="transparent", width=100)
label_port_range_from.grid(row=3,column=0,pady=10,padx=10)
textbox = customtkinter.CTkTextbox(app,height=150)
textbox.grid(row=3,column=1,columnspan=4,pady=10)
textbox.delete("0.0", "end")
label_4 = customtkinter.CTkLabel(app, text="Status", fg_color="transparent", width=100)
label_4.grid(row=4,column=0,pady=10)
label_status = customtkinter.CTkLabel(app, text="Press Start To Run", fg_color="transparent", width=100)
label_status.grid(row=4,column=1,pady=10,columnspan=3)

app.mainloop()