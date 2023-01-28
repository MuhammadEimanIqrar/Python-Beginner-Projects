# name = ""

# print("My name is: " + name)
# print("My name is: {}".format(name))
# print(f"My name is: {name}")

name = input('name: ')
age = int(input('age: '))
feeling = input('feeling: ')

madlib = f"My name is: {name} \
    and i'm {age} years old \
        and i {feeling} my life"

print(madlib)