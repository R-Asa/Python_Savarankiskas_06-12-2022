# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def shshowObjectKeys():
  for x in audi:
    print(audi[x])

shshowObjectKeys()

# audi
# A6
# 2005
# white


# arba

def showObjectKeys_2():
  audi_values = audi.values()
  print(audi_values)

showObjectKeys_2()
# dict_values(['audi', 'A6', 2005, 'white'])