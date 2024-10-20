'''
The program reads the meter reading details from the text file 'readings.txt'
calculates the units consumed and the total charge based on the 
readings of the previous & current month and writes the details
to another file

'''

with open("readings.txt","r") as fileinpobj:
    with open("bills.txt","w") as fileoutobj:
        #Writing the column headings
        fileoutobj.write("Consumer No\tUnits\tTot Charge\n")
        
        #Reading each line from the file into a list
        for line in fileinpobj:
            #Splitting the line on the basis of ',' as the delimeter
            reading=line.split(",")
            #Coverting each of the fields to integer
            consumer_no=int(reading[0])
            prev_read=int(reading[1])
            curr_read=int(reading[2])
            #Calculating the units consumed by substracting 'prev_read' from 'curr_read'
            units=curr_read-prev_read
            tot_charge=units*8
            #Formatting the bill details so that it camn be written to a text file
            bill=f"{consumer_no},{units},{tot_charge}\n"
            fileoutobj.write(bill)