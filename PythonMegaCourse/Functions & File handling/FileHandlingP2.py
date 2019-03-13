file=open("055 fruits.txt","r")
file.seek(0)
content = file.readlines()
file.close()

from LengthString import len_str
for i in content:
    print(len_str(i))
