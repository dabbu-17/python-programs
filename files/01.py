#opens the file anudip.txt in write mode
'''
fileobj = open("abc.txt","w")
if fileobj:
    print("File Created successfully")
    fileobj.write("I am writing something to the filo")
#Closing the file
fileobj.close()
'''
with open("abc.txt","w") as fileobj:
    print("File Created successfully")
    print(fileobj)
    fileobj.write("I am writing something to the file")