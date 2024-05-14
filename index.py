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

# buscar datos con in y not in
print(", welc" in welcome) # da true porque esta
print("4" not in welcome) # da true porque no esta
print("5" not in welcome) # da false porque esta

# operadores de pertenencia