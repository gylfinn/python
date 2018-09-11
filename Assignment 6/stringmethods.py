name = input("Input a name: ")

name = name.split(", ")

firstname = name[1]
firstinitial = firstname[0]
lastname = name[0]

print (firstinitial.capitalize() + ". " + lastname.capitalize())
