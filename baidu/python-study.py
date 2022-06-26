from unicodedata import name


print("nihao")
names = ['a','b','b','c']
newname = [name.upper() for name in names if len(name)<3]
print(newname)