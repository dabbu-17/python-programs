'''
Define a method that takes in a as a parameter an ip address in the IV4 format
and should check if the ip address is valid.
Validations:

1. The number of octets should excatly be 4.
2..The deleimiting character of each octet should be '.'.
3. Each octet should be an integer in the range of 0-255.
'''

def validate_ip(ip):
    ##Splitting the ip on the basis of '.' as the delimeter
    octets=ip.split(".")
    #Checking if the length of the list is exactly 4.
    if len(octets)!=4:
        return False
    for strOctet in octets:
        if int(strOctet)<0 or int(strOctet)>255:
                   return False               
    return True

if validate_ip("12.12.222.45"):
    print("Valid ip")
else:
     print("In valid ip")