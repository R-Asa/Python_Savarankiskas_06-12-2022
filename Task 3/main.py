# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def showObjectKeys():
  audi_values = audi.values()
  print(audi_values)

showObjectKeys()
# dict_values(['audi', 'A6', 2005, 'white'])