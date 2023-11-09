import ipaddress
from ipaddress import IPv4Network
import re

app_loop = ''
while(app_loop!= 'n'):
    input_IP = input("Enter the IP address \t: ")
    if ipaddress.ip_interface(input_IP):
        mask_input = input("Enter subnet mask \t: ")
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
        
        print(f"\n\nInterface IP \t\t: {input_IP}")
        print(f"Subnet Mask\t\t: {mask_input}")
        print(f"Network Address \t: {network.network_address}")
        print(f"Broadcast Address \t: {network.broadcast_address}")
        print(f"Network mask\t\t: {network.netmask}")
        print(f"Number of hosts \t: {(network.num_addresses)-2}")    
        print(f"Starting IP Address \t: {(network.network_address)+1}")
        print(f"Ending IP Address \t: {(network.broadcast_address)-1}")

        app_loop = input("\nEnter new address?(y/n)\t: ")
        continue
    else:
        pass
    app_loop = input("INVALID IP. TRY AGAIN? (y/n)\t:")
exit()