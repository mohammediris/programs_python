from tkinter import *
import ipaddress
from ipaddress import IPv4Network
import re


def calculate():
    out_netip.delete(0,END)
    out_broadip.delete(0,END)
    out_netmask.delete(0,END)
    out_numaddr.delete(0,END)
    out_startaddr.delete(0,END)
    out_endaddr.delete(0,END)
    input_IP = in_ip.get()
    mask_input = in_mask.get()
    if ipaddress.ip_interface(input_IP):      
        mask_check = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",mask_input)
        octet = mask_input.split('.')
        if (mask_check and 
            0<= int(octet[0]) <= 255 and
            0<= int(octet[1]) <= 255 and
            0<= int(octet[2]) <= 255 and
            0<= int(octet[3]) <= 255 ):   
                hostIP = input_IP + '/' + mask_input
            
        elif re.fullmatch(r"[0-9]{1,2}",mask_input) and 0<=int(mask_input)<=32:
            x,y,z = ['','','']
            list = []
            cidr = []
            for _ in range(int(mask_input)):
                x = x + '1'
            z = x + y.zfill(32-int(mask_input))
            list = re.findall(".{8}",z)
            cidr = [str(int(i,2)) for i in list]
            cidr_op = '.'.join(cidr) 
            hostIP = input_IP + '/' + cidr_op

        network = ipaddress.IPv4Network(hostIP, strict=False)
    else:
        pass

    out_netip.insert(0,str(network.network_address))
    out_broadip.insert(0,str(network.broadcast_address))
    out_netmask.insert(0,str(network.netmask))
    out_numaddr.insert(0,str(network.num_addresses-2))
    out_startaddr.insert(0,str(network.network_address+1))
    out_endaddr.insert(0,str(network.broadcast_address-1))

def clear():
    out_netip.delete(0,END)
    out_broadip.delete(0,END)
    out_netmask.delete(0,END)
    out_numaddr.delete(0,END)
    out_startaddr.delete(0,END)
    out_endaddr.delete(0,END)
    # in_mask.delete(0,END)
    # in_ip.delete(0,END)


root = Tk()

root.title("Subnet Calculator")

label_1 = Label(root,font = "Arial",text="Enter IP Adress",anchor=W)
label_2 = Label(root,font = "Arial", text="Enter Subnet Mask",anchor=W)
label_3 = Label(root,font = "Arial", text="Network Address is: ",anchor=W)
label_4 = Label(root,font = "Arial", text="Broadcast Address is: ",anchor=W)
label_5 = Label(root,font = "Arial", text="Network Mask is: ",anchor=W)
label_6 = Label(root,font = "Arial", text="No of host is: ",anchor=W)
label_7 = Label(root,font = "Arial", text="Starting IP Address is: ",anchor=W)
label_8 = Label(root,font = "Arial", text="Ending Ip Address is: ",anchor=W)


in_ip = Entry(root,font = "Arial", width=40, borderwidth=2)
in_mask = Entry(root,font = "Arial", width=40,borderwidth=2)
out_netip = Entry(root,font = "Arial", width=40, borderwidth=2)
out_broadip = Entry(root,font = "Arial", width=40, borderwidth=2)
out_netmask= Entry(root,font = "Arial", width=40, borderwidth=2)
out_numaddr = Entry(root,font = "Arial", width=40, borderwidth=2)
out_startaddr = Entry(root,font = "Arial", width=40, borderwidth=2)
out_endaddr = Entry(root,font = "Arial", width=40, borderwidth=2)

button_calc = Button(root,font = "Arial",text="Calculate",padx=30, command=calculate)
button_clear = Button(root,font = "Arial",text="Clear",padx=30,command=clear)
buton_exit = Button(root,font = "Arial", text="Exit Program",padx=40,command=root.quit)

label_1.grid(row=0,column=0)
label_2.grid(row=1,column=0)
label_3.grid(row=3,column=0)
label_4.grid(row=4,column=0)
label_5.grid(row=5,column=0)
label_6.grid(row=6,column=0)
label_7.grid(row=7,column=0)
label_8.grid(row=8,column=0)

in_ip.grid(row=0,column=1)
in_mask.grid(row=1,column=1)
out_netip.grid(row=3,column=1)
out_broadip.grid(row=4,column=1)
out_netmask.grid(row=5,column=1)
out_numaddr.grid(row=6,column=1)
out_startaddr.grid(row=7,column=1)
out_endaddr.grid(row=8,column=1)

button_calc.grid(row=2,column=0)
button_clear.grid(row=2,column=1)
buton_exit.grid(row=9,column=0,columnspan=2)




root.mainloop()


        # print(f"Network mask\t\t: {network.netmask}")
        # print(f"Number of hosts \t: {(network.num_addresses)-2}")    
        # print(f"Starting IP Address \t: {(network.network_address)+1}")
        # print(f"Ending IP Address \t: {(network.broadcast_address)-1}")
