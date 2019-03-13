file=open("examplewrite.txt","w")
l=["Line1","Line2","Line3"]
for i in l:
    file.write(i+"\n")
file.close()
