'''
Libraries
'''
import networkx as nx 
import matplotlib.pyplot as plt
import netmiko
import re
from getpass import getpass
from queue import Queue
import signal
signal.signal(signal.SIGFPE,signal.SIG_DFL)
signal.signal(signal.SIGINT,signal.SIG_DFL)
'''
Function defenitions
'''
def add_node (name,device_name,ip_address):
    '''
    passes input arguments into structured data for creating nodes 
    '''
    node_list.append((name,{"device_name":device_name, "IP":ip_address}))
    G.add_nodes_from(node_list)

def add_edge (nodeA, nodeB,link_type):
    '''
    passes input arguments into structured data for creating node edges and links 
    '''
    edge_list.append((nodeA,nodeB,{"type":link_type}))
    edge_labels[(nodeA,nodeB)]=link_type
    G.add_edges_from(edge_list)
'''
Variable declarations
'''
G = nx.Graph()
node_list = []
edge_list = []
edge_labels = {}
nodpos_attr = {}
queue = Queue()
known_neighbors = {}
known_ip = [] 
device = {
        "ip" :"192.168.34.2",
        "device_type" : "cisco_ios",
        "username" : "cisco",
        "password" : "cisco"
        } # for testing purpose, the values are given in the code as dictionary variables.


'''
Main Code
'''
ipaddress = input("Enter IP Address : \n")
username = input("Enter username : \n")
password = input("Enter password : \n")

device = {
        "ip" :ipaddress,
        "device_type" : "cisco_ios",
        "username" : username,
        "password" : password
        }
        
queue.put(device["ip"]) # first IP address passed to queue
while not queue.empty():
    device["ip"] = queue.get()
    try:
        print(f'Connecting to device {device["ip"]}')
        connection = netmiko.ConnectHandler(**device) # establishing SSH connection
        node_name = connection.send_command('sh run | include host')
        cdp_output = connection.send_command('show cdp neighbors detail')
        add_node (node_name[9:],node_name[9:],device["ip"]) # adding current node to map
        neighbors = re.findall("Device ID: .+\n.*:.*\n.*:.*\n",str(cdp_output))
        for neighbor in neighbors:
            op_nbr = re.match(r"Device ID: (.*)\..*\..*\n.*\n.*: (.*)",str(neighbor))
            known_neighbors[op_nbr.group(1)] = op_nbr.group(2)
            if op_nbr.group(2) not in known_ip:
                known_ip.append(op_nbr.group(2))   
                queue.put(op_nbr.group(2)) # adding IP addresses of neighbor nodes for next iteration
                add_edge (node_name[9:], op_nbr.group(1),"copper") # adding neighbor nodes as edges to map
        connection.disconnect()
    except (netmiko.exceptions.NetmikoAuthenticationException,
            netmiko.exceptions.NetmikoTimeoutException) as error:
        error_message = re.match(".*",str(error)).group(0)
        print(f'Cannot connect to {device["ip"]} due to {error_message}')
        print('============================================================') 
print("\nknown neighbors are:")
for kn in known_neighbors:
    print(kn+' - '+known_neighbors[kn])
'''
code for plotting the network map
'''
nodpos = nx.spring_layout(G)
for n in G.nodes():
    nodpos_attr[n] = nodpos[n]+[0,-0.3]
edge_labels = nx.get_edge_attributes(G,'type')
node_labels = nx.get_node_attributes(G,'device_name')
nx.draw_networkx(G,pos=nodpos,with_labels=True,node_color="blue",node_size=1500,font_color="white",font_weight="bold")
nx.draw_networkx_edge_labels(G,pos=nodpos,edge_labels=edge_labels,label_pos=0.5,font_color='red')
nx.draw_networkx_labels(G,pos=nodpos_attr,labels=node_labels)
plt.show()