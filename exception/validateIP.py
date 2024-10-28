class InvalidIPException(Exception):
     def _init_(self,error):
          super()._init_(error)
try:
    def validataIp(ip):
        ##Splitting the ip on the basis of '.' as the delimeter
        octets=ip.split(".")
        #Checking if the length of the list is exactly 4.
        if len(octets)!=4:
            raise InvalidIPException("The number of octets should excatly be 4..")
            #return False
        for strOctet in octets:
            if int(strOctet)<0 or int(strOctet)>255:
                 valid=False
                 raise InvalidIPException("The octet should be an integer in th range of [0-255]" ) 
                 
                 #return False   
                        
        print("Valid IP")
except InvalidIPException as inv:
     print(inv)
     

validataIp("12.12.12.225")