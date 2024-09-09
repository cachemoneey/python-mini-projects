phonebook

people = {
    "Azizur": "012345",
    "Rohman": "678900"
}

name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")