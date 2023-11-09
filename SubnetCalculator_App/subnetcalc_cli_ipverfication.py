import ipaddress
from ipaddress import IPv4Network
import re

app_loop = ''
while(app_loop!= 'n'):
    input_IP = input("Enter the IP address \t: ")
    if re.fullmatch(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",input_IP):
        octet_list = input_IP.split('.')
        if (
            len(octet_list) == 4 
            and 1 <= int(octet_list[0]) <= 223 
            and int(octet_list[0]) != 127 
            and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254)
            and 0 <= int(octet_list[1]) <= 255 
            and 0 <= int(octet_list[2]) <= 255 
            and 0 <= int(octet_list[3]) <= 255
            ):
            mask_loop = ''
            while(mask_loop != 'n'):
                mask_input = input("Enter subnet mask \t: ")
                if re.fullmatch(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",mask_input):   
                    # following code will strip the subnet mask 
                    # and calculate the number of subnets and number of hosts
                    str_masksplit = mask_input.split('.')
                    int_Masksplit = [int(mask) for mask in str_masksplit]
                    bin_masksplit = [(bin(m).lstrip('0b')).zfill(8) for m in int_Masksplit]
                    bin_mask = ''.join(bin_masksplit)
                    number_host = 2**(bin_mask.count('0'))-2
                    number_subnet = 2**(bin_mask.count('1'))
                    print(f"Number of subnets \t: {number_subnet} \nNumber of hosts \t: {number_host}")
                    hostIP = input_IP + '/' + str(bin_mask.count('1'))
                    break
                elif re.fullmatch(r"[0-9]{1,2}",mask_input) and 0<=int(mask_input)<=32:
                    x,y,z = ['','','']
                    list = []
                    cidr = []
                    for _ in range(int(mask_input)):
                        x = x + '1'
                    z = x + y.zfill(32-int(mask_input))
                    list = re.findall(".{8}",z)
                    for i in list:
                        cidr.append(str(int(i,2)))
                    cidr_op = '.'.join(cidr)
                    
                    hostIP = input_IP + '/' + cidr_op
                    # number_host = 2**(abs(32-int(mask_input)))-2
                    # number_subnet = 2**(int(mask_input))
                    # print(f"Number of subnets \t: {number_subnet} \nNumber of hosts \t: {number_host}")
                    break
                else:                   
                    mask_loop = input("INVALID SUBNET MASK!!! TRY AGAIN?(y/n)")
                    continue
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
    else:
        pass
        # app_loop = input("INVALID IP. TRY AGAIN? (y/n)\t:")
        # break
    app_loop = input("INVALID IP. TRY AGAIN? (y/n)\t:")
exit()