file=open("example.txt",'r')
if file != '':
    print("File opened")
    file.seek(0)
    content = file.readlines()
    print(content)
    content = [i.rstrip("\n") for i in content]
    print("Content stripped")
else:
    print("File cannot open")
print(content)
print("File closing...")
file.close()
print("File closed.")
