import subprocess
from scapy.all import ARP, sniff
import psutil
import socket
import sys
import re
"""
Functions defined
"""
def enable_dhcp(interface_name): 
    
    command = f"netsh interface ipv4 set address name=\"{interface_name}\" source=dhcp"
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    main_string = str(result.stdout.decode('utf-8').strip())
    pattern = r'\bRun as administrator\b'
    #sys.exit()
    if result.returncode==0:
        print (f"\nDHCP enabled on interface: {interface_name}")
    elif re.search(pattern, main_string):     
        
        print('\n'+result.stdout.decode('utf-8').strip())
        input("Please right-click the file and select \"Run as Administrator\"")
        sys.exit()
    else:
        print('\n'+result.stdout.decode('utf-8').strip())
        
    return result.returncode
    
def arp_display(pkt):
    if ARP in pkt and pkt[ARP].op == 1:  # If it's an ARP request (who-has)
        print(f"\nA device with \nIP\t\t: {pkt[ARP].psrc}\nMAC Address\t: {pkt[ARP].hwsrc}\nis sending ARP Request")
        
        
def display_ipv4_interfaces():
    # Get network interface addresses
    interface_addrs = psutil.net_if_addrs()
    ifaces_list = []
    print("=======================================")
    print("Network interfaces available in this PC")
    print("---------------------------------------")
    for interface, addrs in interface_addrs.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ifaces_list.append(interface)
    
    return ifaces_list
"""
Main Code
"""
if __name__ == "__main__":
    timeout = 30 # set timeout for sniffing if not packets received
    ifaces_list = display_ipv4_interfaces()
    for iface in ifaces_list:
        print (str(ifaces_list.index(iface)+1) + ' ' + iface)
    print("=======================================")    
    index = input("Select network interface: ")
    interface = ifaces_list[int(index)-1]
    stats = psutil.net_if_stats()[interface]
    
    enable_dhcp(interface)
    if stats.isup:
        try:
            print(f"\nSearching for Source IP in ARP broadcast in interface \"{interface}\" for {timeout} seconds")
            # sniffing network traffic for ARP packets
            sniff(filter="arp", prn=arp_display, store=0, iface=interface, count=5, timeout=timeout)
            input()
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        print("\nSelected Network Interface is Down, Please check the connection.")
        input("\nPress any key to exit.")