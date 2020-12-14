names = ["Fred","BB","Laurence"]

print(names[1])

names.append("Léa")

print(names[3])

names.sort()

print(names)

simple_name = input("Add a name ")

names.append(simple_name)

print(f"The list has {len(names)} elements : {names}")