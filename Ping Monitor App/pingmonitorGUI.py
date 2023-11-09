import subprocess
from datetime import datetime, timedelta
import time
from tkinter import*
import ipaddress
import re


def start_ping():
    startevent = int()
    global status

    input_IP = ipaddr.get()
    pcommand = 'ping -n 1 '+ input_IP
    deviceName = device.get()
    fileName    = f"{deviceName.upper()}_ping_test.txt" 
    minutes = duration.get() 
    ip_check = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",input_IP)
    url_check = re.match(r"^.+\..+",input_IP)
    url2_check = re.match(r"^.+\..+\..+",input_IP)
    min_check = re.match(r"[0-9]{1,4}",minutes)
    
    if(deviceName and input_IP and minutes):
        if (ip_check or url_check or url2_check): 
            if min_check:
                tlog = open(fileName,"w")
                tlog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + f": Ping Test for {deviceName.upper()} - IP/URL [{input_IP}] : Started" + '\n\n') 
                tlog.close()
                endTime = datetime.now() + timedelta(minutes=int(minutes))
                while(datetime.now() <= endTime): 
                    result = subprocess.run(pcommand,capture_output=True, text=True)
                    
                    remainTime = endTime-datetime.now()
                    statusbar.configure(text=str(remainTime)[:-7] + ' (time remaining...)')
                    root.update()

                    if result.returncode == 1 and startevent == 0:
                        tlog = open(fileName,"a")
                        tlog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S' + f": Disconnected") + '\n')
                        tlog.close() 
                        start_time = time.time()
                        startevent = 1
                    elif result.returncode == 1 and startevent == 1:
                        pass
                    elif result.returncode == 0 and startevent == 1:  
                        end_time = time.time() -start_time
                        tlog = open(fileName,"a")
                        tlog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + f": Connected back after {int(end_time)} seconds" + '\n') 
                        tlog.close()
                        startevent = 0
                    elif result.returncode == 0 and startevent == 0:  
                        time.sleep(1)
                        pass

                statusbar.configure(text='Program Ended')
                tlog = open(fileName,"a")
                tlog.write('\n'+ datetime.now().strftime('%Y-%m-%d %H:%M:%S') + f": Ping Test for {deviceName.upper()} - IP/URL [{input_IP}] : Ended" + '\n')
                tlog.close()
                root.update()
            else:
                statusbar.configure(text='Invalid duration')    
        else:
            statusbar.configure(text='Invalid IP')
    elif (not deviceName):
        statusbar.configure(text='Enter device name')
    elif (not input_IP):
        statusbar.configure(text='Enter IP')
    elif (not minutes):
        statusbar.configure(text='Enter duration')
    pass

def abort_ping():
    pass


root = Tk()
root.title("Ping Monitor by School of Iris")

label_1 = Label(root,font = "Arial",text="Enter IP or URL",anchor=W)
label_1.grid(row=0,column=0)

ipaddr = Entry(root,font = "Arial", width=30, borderwidth=2)
ipaddr.grid(row=0,column=1, columnspan=2)

label_2 = Label(root,font = "Arial",text="Enter Device Name",anchor=W)
label_2.grid(row=1,column=0)

device = Entry(root,font = "Arial", width=30, borderwidth=2)
device.grid(row=1,column=1, columnspan=2)

label_3 = Label(root,font = "Arial",text="Enter Duration (minutes)",anchor=W)
label_3.grid(row=2,column=0)

duration = Entry(root,font = "Arial", width=30, borderwidth=2)
duration.grid(row=2,column=1,columnspan=2)



button_start = Button(root,font = "Arial",text="START",padx=50, command=start_ping)
#button_abort= Button(root,font = "Arial",text="Abort",padx=20,command=abort_ping)
# buton_exit = Button(root,font = "Arial", text="Exit",padx=20,command=root.quit)
button_start.grid(row=3,column=0,columnspan=3)
#button_abort.grid(row=3,column=1)
# buton_exit.grid(row=3,column=2)
statusbar = Label(root, text="Click START for monitoring",bd=1,relief=SUNKEN,anchor=W)
# sticky will span the status bar from east to west
statusbar.grid(row = 5,column=0,sticky=W+E,columnspan=3)

root.mainloop()
