# operadores

"operadores aritmeticos"
print(f"suma: 3 + 2 = { 3 + 2 }")
print(f"resta: 3 - 2 = { 3 - 2 }")
print(f"multiplicacion: 3 * 2 = { 3 * 2 }")
print(f"division: 3 / 2 = { 3 / 2 }")
print(f"modulo: 3 % 2 = { 3 % 2 }")
print(f"exponente: 3 ** 2 = { 3 ** 2 }")
print(f"division entera: 3 // 2 = { 3 // 2 }")

'operadores de comparacion'
print(f"igualdad: 5 == 3 es {5 == 3}")
print(f"desigualdad: 5 != 3 es {5 != 3}")
print(f"mayor que: 5 > 3 es {5 > 3}")
print(f"menor que: 5 < 3 es {5 < 3}")
print(f"mayor o igual que: 5 >= 3 es {5 > 3}")
print(f"menor o igual que: 5 <= 3 es {5 < 3}")

'operadores logicos'
print(f"AND &&: 5 + 3 == 8 and 4 - 1 == 3 es { 5 + 3 == 8 and 4 - 1 == 3}")
print(f"OR ||: 5 + 3 == 8 or 4 - 1 == 3 es { 5 + 3 == 8 or 4 - 1 == 3}") #el OR solo pide que sea verdadera una de las dos condiciones.
print(f"NOT !: not 5 + 3 == 100 es {not 5 + 3 == 100}")
print(f"NOT !: not 5 + 3 == 8 es {not 5 + 3 == 8}")

'operadores de asignacion'
my_j = 11 #asignacion.
print(my_j)
my_j += 1 #suma y asignacion.
print(my_j)
my_j -= 1 #resta y asignacion.
print(my_j)
my_j *= 1 #multiplicacion y asignacion. 
print(my_j)
my_j /= 1 #division y asignacion.
print(my_j)
my_j %= 1 #modulo y asignacion.
print(my_j)
my_j **= 1 #exponente y asignacion
print(my_j)
my_j //= 1 #division entera y asignacion.
print(my_j)

'operadores de identidad'
new_variable = 0.0
print(f"my_j is new_variable es {my_j is new_variable}")
print(f"my_j is not new_variable es {my_j is not new_variable}")

'operadores de pertenencia'
print(f"'a' in 'javi' = {'a' in 'javi'}")
print(f"'a' not in 'javi' = {'a' not in 'javi'}")

'operadores de bit'
v = 5 #101
t = 8 #1000
print(f"AND: 5 & 8 = {5 & 8}") 
print(f"OR: 5 | 8 = {5 | 8}")
print(f"XOR: 5 ^ 8 = {5 ^ 8}") 
print(f"NOT: ~5 = {~5}") 
print(f"desplazamiento hacia la derecha: 10 >> 1 = {10 >> 1}")
print(f"desplazamiento hacia la izquierda: 10 << 1 = {10 << 1}")

"""
estructuras de control
"""
'condicional'
eljavi0 = "medrano"
if eljavi0 == "javier":
    print("eljavi0 es 'javier'")
elif eljavi0 == "medrano":
    print ("eljavi0 es 'medrano'")
else:
    print("eljavi0 no es 'javier' ni es 'medrano'")

"iterativas"
for i in range(10):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

'manejo de excepciones'
try:
    print(10 / 0)
except:
    print("no se puede")
finally:
    print("ha finalizado el manejo de excepciones")

"""
extra
"""
for number in range (10, 56):
    if number % 2 == 0 and number != 16 and number %3 != 0:
        print(number)
