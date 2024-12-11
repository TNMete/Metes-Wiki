# Python 3 - Vergleichsoperatoren

values

x = 10

y = 20

### Gleichheit
print(x == y)   # False 

### Ungleichheit
print(x != y)   # True 

### Größer als
print(x > y)    # False 

### Kleiner als
print(x < y)    # True

### Größer oder gleich
print(x >= y)   # False

### Kleiner oder gleich
print(x <= y)   # True

### if-Operatoren
x = 15
y = 10

if x > y:
    print("x ist größer als y")
else:
    print("x ist nicht größer als y")

### and, or & not Operatoren
x = 10
y = 20
z = 15

if x < y and z < y:
    print("Beide Bedingungen sind wahr")