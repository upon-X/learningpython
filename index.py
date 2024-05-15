# Python case sensitive

# Tipos de datos
int = 4
float = 4.4
string = "dsadasdas"
stringv2 = """
  jndsakdbnjasdnjid
  asdkopjsdaoidsa
  asdjiasdplsd
  """
boolean = True

# Variables
# declaro/defino
name = "Valentino"
print(name)
# Redefino
name = "David"
print(name)

name = "David"
name = 5
# f string | sirve para concatenar variables sin importar su contenido y no generar errores
welcome = f'Hello, welcome {name}'
print(welcome)

# para borrar variables
del name

# operadores de pertenencia in / not in
print(", welc" in welcome) # da true porque esta
print("4" not in welcome) # da true porque no esta
print("5" not in welcome) # da false porque esta

# datos compuestos

# list[] | se puede cambiar
lista = [ 
  "Valentino Micheloni",
  184,
  184,
  True,
]
lista[1] = 185
print(lista)
print(lista[1])

# tuple() | no se puede modificar
tupla = (
  "Valentino Micheloni",
  "Valentino Micheloni",
  184,
  True,
)
print(tupla[2])

# conjunto (set) | no modificable, no se pueden repetir valores, no se accede por indices
conjunto = {
  "Valentino Micheloni",
  184,
  True,
}
print(conjunto)

# diccionario (dict) | igual a un json en js

diccionario = {
  # key  /  value
  'name' : 'Valentino Micheloni',
  'age' : 20,
  'height' : 184,
  'gender' : 'Male',
  'has_job' : False
}

print(f"Has a Job? {diccionario['has_job']}")

# operadores
# aritmetica
suma = 10 + 5
resta = 10 - 5
multi = 10 * 2
divi = 10 / 2 # devuelve dato float (5.0)
exponente = 12**2
divi_baja = 10//3 # devuelve dato int redondeado hacia abajo
resto = 10 % 2

# comparación
igual_que = 10 == 10
mayor_que = 10 > 5
menor_que = 5 < 10
mayor_igual = 10 >= 5
menor_igual = 5 <= 5

# condicionales
age = 18
if age >= 18: 
  print('Adult')
  print('part of if')
else: 
  print('Not Adult')
  print('part of else')

# if
mensual_income = 7000
if mensual_income >= 10000:
  print('you are Good on every part of the world')
elif 1000 < mensual_income < 10000:
  print('you are OK on every part of the world')
else: print('poor')

nationality = 'german'

if (mensual_income > 1000) & (nationality == 'german'):
  print('welcome comrade')
elif (mensual_income > 1000) & (nationality != 'german'):
  print('you are not my comrade but respect you')
else: print('get out')

# not transforma el boolean al contrario
result = True & True # True
result2 = True | True # True
result2 = not True # False

# metodos
var1 = 'Hola'
var2 = '¿Que haces?'
var3 = 129
var4 = True

print(dir(var1)) # imprime todos los atributos validos con el dato que pasemos

# metodos de strings
# estructura de los metodos : dato.metodo() 
chain = "Hola Mundo"
chain.upper() # hace uppercase a la chain
print(chain)

searching_find = chain.find(" ") # retorna 4 porque busca el espacio
# Si no encuentra nada, devuelve -1

# Parecido a find, pero cuando no encuentra nada nos tira una excepcion
searching_index = chain.index("H")

# Verifica si el tipo de dato es int
is_number = chain.isnumeric()

# Devuelve true solo si no hay caracteres especiales
is_alpha = chain.isalpha()

# Devuelve la cantidad de veces que esta el dato que le pasamos en el chain
count_coincidence = chain.count("a")

# Cuenta cuantos caracteres hay | es una funcion()
count_charac = len(chain)

# Verificamos si un string empieza o termina con el string que se le pasa
start_with = chain.startswith("H")
ends_with = chain.endswith("H")

# si se encuentra el primer dato pasado, lo reemplzara con el segundo
new_string = chain.replace("Hola","OSTIA")
print(new_string)

# Devuelve una list que separa un string con el valor que le pasemos
chain2 = "Hola,Mundo,me,gusta,la,verga"
spaced_string = chain2.split(",")
print(spaced_string)

# metodos de lists
# crea una lista / deprecated
create_list = list(["hola", "mundo", 34])
print(create_list)

# Cuantos elementos hay en una lista
len_list = len(create_list) # 3

# Agrega un elemento al final de la lista
create_list.append("OSTIA")

# Agrega un elemento en el indice que queramos
create_list.insert(2,"Toma Mango")

# Agregar varios elementos al final de la lista
create_list.extend(["que", "mierda pensas", 323])

# Elimina el elemento que se encuentre en el indice que le pasemos
# Si le pasamos en negativo, elimina desde el final
create_list.pop(0)

# Remueve un elemento por su valor y si no lo encuentra nos arroja error
create_list.remove("que")

# Vacia la lista, asi de heavy
create_list.clear()

# Ordena de forma ascendente, pero si hay strings, nos arroja error
create_list.sort()
# si le agregamos (reverse=true), lo damos vuelta

# Da vuelta la lista
create_list.reverse()