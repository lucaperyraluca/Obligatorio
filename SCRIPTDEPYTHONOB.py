import subprocess
from subprocess import Popen, PIPE
import argparse
import sys 

parser = argparse.ArgumentParser()

parser.add_argument("-r", "--recursive", help="Muestra la salida de las horas", action="store_true")
parser.add_argument("-u", "--user", type=str , help="Muestra para un usuario en particular.")
parser.add_argument("-o", "--order", type=str, choices=["u", "t", "h", "d"], help="Ordena" )
parser.add_argument("-i", "--invert", help="Invierte la salida", action="store_true")


try:
 args = parser.parse_args()
except SystemExit as e:
 exit(20)

#ruta al script en bash
ej1_y_lista_parametros = ['/home/linux/Desktop/PRUEBASCARPETA/PRUEBA.sh']
#agrego el parametro a la lista
if args.recursive:
    ej1_y_lista_parametros.append("-r")
#agrego el parametro como string a la lista   
if args.user:
    ej1_y_lista_parametros.append("-u")
    ej1_y_lista_parametros.append(args.user)

process=Popen(ej1_y_lista_parametros, stdout = PIPE, stderr = PIPE)
output=process.communicate()

#muestra la salida de error:
if process.returncode > 0:
    print(output[1].decode(), file = sys.stderr, end="")
    exit(process.returncode)

#opcion -r
if args.recursive == True:
    print(output[0].decode(), file=sys.stdout)


#opcion -u
if args.user != None:
    print(output[0].decode(), file=sys.stdout)

#OPCION ORDENAR ----"U"------
if args.order == "u":
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for i in lista:
        i_procesado= i.split("\n")
        otra_lista.append(i_procesado)

    b=(len(otra_lista) - 1)


    #Genero una lista donde cada tupla  tiene una posicion
    # fijarme si aca puedo usar len(lista_de_tuplas) en lugar de b,le saco el 0 porque? 
    lista_de_tuplas=[]
# Aca el for estaba con un range de 1,b. lo cambie y ahora estaria con 0,b y anda bien
    for i in range(b):
        lista_de_tuplas.append(otra_lista[(i)])
    #con la funcion sort le digo que se ordene por la clave definida en lambda como el ubicado en la primer posicion, entonces
    #la lista, que tiene tuplas dentro, las va a ordenar por el valor del de la primer poscion. p es un nombre cualquiera
    lista_de_tuplas.sort(key=lambda p: p[0])

    #convierto las listar en string con join, y luego reemplazo las comas por tabulaciones y/o espacios
    cabecera=",".join(otra_lista[0])
    cabecera_ordenada=cabecera.replace(',','\t\t  ')
    print(cabecera_ordenada)
    for i in range(1,(b-1)):
        linea=",".join(lista_de_tuplas[(i)])
        linea_ordenada=linea.replace(',','\t\t')
        print(linea_ordenada)




if args.order == "t":
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for i in lista:
        i_procesado= i.split()
        otra_lista.append(i_procesado)

    b=(len(otra_lista) - 1)


    #Genero una lista donde cada tupla  tiene una posicion
    # fijarme si aca puedo usar len(lista_de_tuplas) en lugar de b,le saco el 0 porque? 
    lista_de_tuplas=[]
    for i in range(1,b):
        lista_de_tuplas.append(otra_lista[(i)])

    #con la funcion sort le digo que se ordene por la clave definida en lambda como el ubicado en la primer posicion
    lista_de_tuplas.sort(key=lambda p: p[1])

    #convierto las listar en string con join, y luego reemplazo las comas por tabulaciones y/o espacios
    cabecera=",".join(otra_lista[0])
    cabecera_ordenada=cabecera.replace(',','\t\t  ')
    print(cabecera_ordenada)
    for i in range(1,(b-1)):
        linea=",".join(lista_de_tuplas[(i)])
        linea_ordenada=linea.replace(',','\t\t')
        print(linea_ordenada)

#OPCION ORDENAR ---"H"----
if args.order == "h":
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for i in lista:
        i_procesado= i.split()
        otra_lista.append(i_procesado)

    b=(len(otra_lista) - 1)


    #Genero una lista donde cada tupla  tiene una posicion
    # fijarme si aca puedo usar len(lista_de_tuplas) en lugar de b,le saco el 0 porque? 
    lista_de_tuplas=[]
    for i in range(1,b):
        lista_de_tuplas.append(otra_lista[(i)])

    #con la funcion sort le digo que se ordene por la clave definida en lambda como el ubicado en la primer posicion
    lista_de_tuplas.sort(key=lambda p: p[3])

    #convierto las listar en string con join, y luego reemplazo las comas por tabulaciones y/o espacios
    cabecera=",".join(otra_lista[0])
    cabecera_ordenada=cabecera.replace(',','\t\t  ')
    print(cabecera_ordenada)
    for i in range(1,(b-1)):
        linea=",".join(lista_de_tuplas[(i)])
        linea_ordenada=linea.replace(',','\t\t')
        print(linea_ordenada)






#OPCION ORDENAR --- "D"---
if args.order == "d":
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for i in lista:
        i_procesado= i.split()
        otra_lista.append(i_procesado)

    b=(len(otra_lista) - 1)


    #Genero una lista donde cada tupla  tiene una posicion
    # fijarme si aca puedo usar len(lista_de_tuplas) en lugar de b,le saco el 0 porque?
    lista_de_tuplas=[]
    for i in range(1,b):
        lista_de_tuplas.append(otra_lista[(i)])

    #con la funcion sort le digo que se ordene por la clave definida en lambda como el ubicado en la primer posicion
    lista_de_tuplas.sort(key=lambda p: p[6])

    #convierto las listar en string con join, y luego reemplazo las comas por tabulaciones y/o espacios
    cabecera=",".join(otra_lista[0])
    cabecera_ordenada=cabecera.replace(',','\t\t  ')
    print(cabecera_ordenada)
    for i in range(1,(b-1)):
        linea=",".join(lista_de_tuplas[(i)])
        linea_ordenada=linea.replace(',','\t\t')
        print(linea_ordenada)



#OPCION ORDENAR ---"I"----
if args.invert == True:
    lista=output[0].decode().split("\n")
    list_name=[]
    for i in range(1,len(lista)):
        list_name.append(lista[(i)].split("\t"))
    for i in range(len(list_name)):
        list_name.sort(key=lambda x: x[0], reverse=True)
    print(lista[0])
    for i in range(len(list_name) - 1):
        linea=",".join(list_name[(i)])
        linea_ordenada=linea.replace(',','\t')
        print(linea_ordenada)

#lo que hago aca es tomar la salida estandar y convertilo, con split en una lista separada por los \t. Luego creo una lista vacia que se va a convertir en una lista de listas,
#en la cual le voy haciendo append de cada linea con un for. El rango lo dejo asi para que la primer linea, que son las cabeceras, no partcipen ya que ellas van siempre en la misma
#posicion.
#list se ve de esta forma:
#['Usuario \t Terminal \t Host \t\t Fecha \t\t H.con \t\t H.Dest \t\t T.Con', 'linux\t\t 0\t\t 0\t\tThu Nov 25\t 07:20\t\t 11:12\t\t\t 03:5.... etc 
#entonces cuando realizo un list_name.append(lista[(i)].split("\t")) lo que estoy haciendo es pasandole cada linea y convirtiendola en una lista.
#list_name se ve asi.
#[['linux', '', ' 0', '', ' 0', '', 'Thu Nov 25', ' 07:20', '', ' 11:12', '', '', ' 03:52'], ['linux', '', ' 0', '', ' 0', '', 'Wed Nov 24', ' 14:13', '', ' 18:5', '', '', 'etc
#Ahora utilizo la funcion sort, y con lambda le indico que tome el segundo valor [1] para tomar el orden, y al decirle reverse true, los invierte. 
#Sin embargo, siguen siendo listas, por lo que los convierto a un string con join, y de esa forma los imprimo en pantalla



