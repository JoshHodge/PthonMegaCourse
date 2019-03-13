with open("ExampleWith.txt","a+") as file:
    file.seek(0)
    content = file.read()
    file.write("Line 6\n")
