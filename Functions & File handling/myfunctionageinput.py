def age_foo(age):
    new_age = float(age) + 50
    return new_age

age = float(input("Please enter age: "))
if age < 150 :
    print(age_foo(age))
else:
    print("Age is too high")
