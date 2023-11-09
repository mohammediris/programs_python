import ipaddress
import re
'''
*SCHOOL OF IRIS - MODULE*
this module contains all the essential codes 
required for input vaidation. 
Each code block is a funtion which can be 
called in the main function for code reusability
'''

def validate_website_address(host):
    '''
    Code block to validate if the given input is 
    a valid website address 
    '''
    url_check = re.match(r"^.+\..+",host)
    url2_check = re.match(r"^.+\..+\..+",host)
    if (url_check or url2_check):
        return True
    else:
        return False

def validate_ipv4_address(ipv4_add):
    '''
    Code block to validate if the given input is 
    a valid IPv4 address
    '''
    try:
        if ipaddress.ip_interface(ipv4_add):
            return True
    except:
        return False
    
def validate_ipv4_mask(ipv4_mask):
    '''
    Code block to validate if the given input is 
    a valid IPv4 address
    '''
    mask_check = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",ipv4_mask)
    octet = ipv4_mask.split('.')
    if (mask_check and 
        0<= int(octet[0]) <= 255 and
        0<= int(octet[1]) <= 255 and
        0<= int(octet[2]) <= 255 and
        0<= int(octet[3]) <= 255 ):
        return True   
    elif re.fullmatch(r"[0-9]{1,2}",ipv4_mask) and 0<=int(ipv4_mask)<=32:
        return True
    else:
        return False
    
def validate_email(email_address):
    '''
    Code block to validate a given email address
    '''
    email_check = re.match(r"^.+@.+\..+",email_address)
    if email_check:
        return True
    else:
        return False

def validate_password(password,char_len,complexiity):
    '''
    Code block to validate the password
    to check if the password entered meets the 
    minimum requirement
    complexity level 
    1   -   alphabets only
    2   -   alphanumeric
    3   -   alphanumeric + special character
    '''
    if len(password) == char_len:
        if complexiity == 1:
            if re.match(r"^[a-zA-Z]+",password):
                return True
            else:
                return False
        elif complexiity == 2:
            if re.match(r"^[a-zA-Z0-9]+",password):
                return True
            else:
                return False
        elif complexiity == 3:
            if re.match(r"^.+",password):
                return True
            else:
                return False
    else:
        return False