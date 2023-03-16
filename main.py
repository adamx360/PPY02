# a
string1 = "Python 2023"
string2 = "Python 2023"
string3 = string1

print(string1 == string2)
print(string2 == string3)

# b
string1 = "Python 2023"
string2 = "Python 2023"
string3 = string1

print(type(string1), hex(id(string1)))
print(type(string2), hex(id(string2)))
print(type(string3), hex(id(string3)))

# c
string1 = "Python 2023"
string2 = "Python 2023"
string3 = string1

string3 = "Java 11"

print(string1 == string2)
print(string2 == string3)

print(type(string1), hex(id(string1)))
print(type(string2), hex(id(string2)))
print(type(string3), hex(id(string3)))
