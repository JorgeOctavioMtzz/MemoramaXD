puntajeP=0
def crea_matriz_random(fils, columns):
    listaXD = list(range(0,int(half)))
    listaXD=listaXD*2
    random.shuffle(listaXD)
    tablero=[]
    pollo=0
    for i in range(fils):
        filatemporal=[]
        for j in range(columns):
            filatemporal.append(listaXD[pollo])
            pollo+=1
        tablero.append(filatemporal)
    return tablero

def crea_matriz_simbolos(fils, columns):
    matriz = []
    for ren in range(fils):
        matriz.append(["𝝮"] * columns)
    return matriz

def muestra_matriz(mat):
    for ren in range(len(mat)):
        print("-------"*columnas)
        for col in range(len(mat[0])):
            print("|",f'{mat[ren][col]:2}', end=' | ')
        print()
        print("-------"*columnas)

def puntajeXD(ren1, col1, ren2, col2, mat1):
    global puntajeP
    valor1 = mat1[ren1][col1]
    valor2 = mat1[ren2][col2]
    if valor1 == valor2:
        puntajeP+=10
        print("FELICIDADES")
        print("Puntaje :", puntajeP)
    else:
        puntajeP+=0
        print("Lastima...")
        print("Puntaje :", puntajeP)
    

def valida_pares(ren1, col1, ren2, col2, mat1, mat2):
    valor1 = mat1[ren1][col1]
    valor2 = mat1[ren2][col2]
    if valor1 == valor2:
        # los valores son iguales, sumo un punto
        mat2[ren1][col1] = valor1
        mat2[ren2][col2] = valor2
        muestra_matriz(mat2)
        return mat2
    else:
        # los valores no son iguales las matrices se quedan iguales
        print("fallaste")
        

import random 
input("Presione la tecla enter para comenzar el memorama ")
filas=int(input("ingrese el numero de filas: "))
columnas=int(input("ingrese el número de columnas: "))
half = (filas*columnas)/2
puntajeMax=half*10
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

matr1=crea_matriz_random(filas, columnas)

matr2= crea_matriz_simbolos(filas, columnas)

muestra_matriz(matr1)
input("Press Enter when you're ready to continue")
for i in range(0,200):
  print("↓"*176)

turnos=intentos
for i in range(intentos):  
    print("Intento #"+str(i+1))
    ca=int(input("Ingrese el número de columna de su primera Carta: "))
    runo=int(input("Ingrese el número de fila de su primera Carta: "))
    cb=int(input("Ingrese el número de columna de su segunda Carta: "))
    rdos=int(input("Ingrese el número de fila de su segunda Carta: "))
    if ca>columnas or runo>filas or cb>columnas or rdos> filas:
        print("Error ingresa un dato válido")
        turnos-=1
        puntajeP+=0
        print("Puntaje: ", puntajeP)
        print("Turnos restantes: ", turnos)
    else:
        caC=ca-1
        runoC=runo-1
        cbC=cb-1
        rdosC=rdos-1
        for f in range(10):
            print("🀫"*177)
        matriz2=valida_pares(runoC, caC, rdosC, cbC, matr1, matr2)
        puntajeXD(runoC, caC, rdosC, cbC, matr1)
        turnos-=1
        print("Turnos restantes: ", turnos)
        print()

if puntajeP==puntajeMax:
    for i in range(1,50):
        print("◀︎◀︎▷▷"*50)
    print("ganaste  "*20)
    

else:
    for i in range(1,50):
        print("☹️☹️☹️☹️"*50)
    print("perdiste "*20)
    