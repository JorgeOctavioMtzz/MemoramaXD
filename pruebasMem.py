import random 
input("Presione la tecla enter para comenzar el memorama ")
filas=int(input("ingrese el numero de filas: "))
columnas=int(input("ingrese el número de columnas: "))
half = (filas*columnas)/2
mitad=half
matches=0
turn=0
intentos=int(input("¿En cuantos intentos crees conseguirlo?: "))
puntaje=0
puntajemax=10*half
turn=intentos
x=0
while x==0:
  intentos=int(input("¿En cuantos intentos crees conseguirlo?: "))
  if intentos<half:
    print("mmm... no lo veo posible, selecciona una opción más factible")
  elif intentos==half:
    print("Modo Hardcore")
    print("iniciando...")
    x=1
    break
  else:
    print("iniciando...")
    x=1
    break
half=0

if columnas%2 == 0 and filas%2 == 0:
  half = (filas*columnas)/2
else:
  print("Error los numeros deben ser pares")

listaXD = list(range(0,int(half)))
listaXD=listaXD*2
random.shuffle(listaXD)
cero=0
listfilas=[]
tablero=[]

pollo=0
for i in range(filas):
  filatemporal=[]
  for j in range(columnas):
    filatemporal.append(listaXD[pollo])
    pollo+=1
  tablero.append(filatemporal)

for xD in tablero:
  print("--------"*columnas)
  print((*xD), sep="   |   ")
  print("--------"*columnas)
input("Press Enter when you're ready to continue")
for i in range(0,200):
  print("↓"*176)
  


listfilas=[]
tablero=[]
for i in range(filas):
  filatemporal=[]
  for j in range(columnas):
    filatemporal.append("𝛀")
  tablero.append(filatemporal)
for xD in tablero:
  print("--------"*columnas)
  print((*xD), sep="   |   ")
  print("--------"*columnas)
 

for i in range(intentos):
  a=int(input("Ingrese el número de columna de su primera Carta: "))
  uno=int(input("Ingrese el número de fila de su primera Carta: "))
  b=int(input("Ingrese el número de columna de su segunda Carta: "))
  dos=int(input("Ingrese el número de fila de su sunda Carta: "))
  for f in range(10):
    print("🀫"*177)
  cc1=((uno-1)*columnas+a)
  cc2=((dos-1)*columnas+b)
  if cc1>len(listaXD) or cc2>len(listaXD):
    print("Error vuelve a intentarlo")
  else:

    c1=listaXD[int(cc1)]
    c2=listaXD[int(cc2)]

  if c1==c2:
    puntaje+=10
    matches+=1
    mitad-=1
    turn-=1
    print("Felicidades puntaje +10 "+str(mitad)+" pares restantes")
  else:
    print("Mmm... Lo siento...")
    turn-=1
  print("Tu puntaje: "+str(puntaje)+"pt")
  print("Turnos Restantes: "+str(turn))
  input("Presione la tecla enter para continuar ")
  for f in range(10):
    print("🀫"*177)

  for i in range(filas):
    filatemporal=[]
    for j in range(columnas):
      filatemporal.append("𝛀")
    tablero.append(filatemporal)
  for xD in tablero:
    print("--------"*columnas)
    print((*xD), sep="   |   ")
    print("--------"*columnas)
