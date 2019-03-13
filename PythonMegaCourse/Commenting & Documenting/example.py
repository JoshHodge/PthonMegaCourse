import datetime
"""
This is a docstring. This function creates a file based on the datetime
and inputs 'Hello' as a string. The filename is printed in format dd-MMM-YYYY.
The script then outputs the name of the file into the cmd
"""
#filename = "sample1.txt"
dateTimeObj = datetime.datetime.now()
filename1 = dateTimeObj.strftime("%d-%b-%Y") + ".txt"
#Create empty file
def create_file(filename):
    with open(filename,"w+") as file:
        file.write("Hello") #writing hello

create_file(filename1)
print(filename1)
