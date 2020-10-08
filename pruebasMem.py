import random 

input("Press Enter to start the memory game")

filas=int(input("ingrese el numero de filas: "))
columnas=int(input("ingrese el número de columnas: "))
half=0
def OriginalMatrix(fils,columns):
  if columns%2 == 0 and fils%2 == 0:
    half = (fils*columns)/2
  else:
    print("Error los numeros deben ser pares")
  listaXD = list(range(0,int(half)))
  listaXD=listaXD*2
  random.shuffle(listaXD)
  cero=0
  listfils=[]
  tablero=[]

  pollo=0
  for i in range(fils):
    filatemporal=[]
    for j in range(columns):
      filatemporal.append(listaXD[pollo])
      pollo+=1
    tablero.append(filatemporal)
  for xD in tablero:
    print("--------"*columns)
    print((*xD), sep="   |   ")
    print("--------"*columns)
  input("Press Enter when you're ready to continue")
  for i in range(0,50):
    print("-----"*50)

OriginalMatrix(filas,columnas)
