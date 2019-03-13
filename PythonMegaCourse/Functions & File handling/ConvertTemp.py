def celcius_to_farenheit(celcius):
    converted = celcius*(9/5) + 32
    return converted
out = []
temps =[10,-20,-289,100]

#temp = float(input("Please input temperature in C: "))
for i in temps:
    if i > -273.15:
        conv = float(celcius_to_farenheit(i))
        #print(conv)
        out = out + [str(conv)+"\n"]
    else: print("That temperature is too low")
#print(out)
file=open("ConvertedTemps.txt","w")
for i in out:
    file.write(i)
file.close()
