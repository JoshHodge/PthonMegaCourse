import datetime
"""
This function accepts three textfiles and merges them into a single file,
saving the file by the date time
"""
#filename = "sample1.txt"
dateTimeObj = datetime.datetime.now()
MergedFileName = dateTimeObj.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"
#Create empty file
def mergeText(file1,file2,file3):
    with open(file1,"r") as file1Temp:
        Text1 = [file1Temp.read()]
    with open(file2,"r") as file2Temp:
        Text2 = [file2Temp.read()]
    with open(file3,"r") as file3Temp:
        Text3 = [file3Temp.read()]
    with open(MergedFileName,"w+") as file:
        for i in Text1:
            file.write(i)
        for j in Text2:
            file.write(j)
        for k in Text3:
            file.write(k)

mergeText("content1.txt","content2.txt","content3.txt")
