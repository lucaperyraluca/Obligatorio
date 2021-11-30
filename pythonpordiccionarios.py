import subprocess
from subprocess import Popen, PIPE
import argparse
import sys 

parser = argparse.ArgumentParser()

parser.add_argument("-r", "--recursive", help="Muestra la salida de las horas", action="store_true")
parser.add_argument("-u", "--user", type=str , help="Muestra para un usuario en particular.")
parser.add_argument("-o", "--order", type=str, choices=["u", "t", "h", "d"], help="Ordena" )
parser.add_argument("-i", "--invert", help="Invierte la salida", action="store_true")
parser.add_argument("-f", "--filter", type=str, choices=["u", "t", "h", "f", "c", "n", "d"], help="Filtra ")


try:
 args = parser.parse_args()
except SystemExit as e:
 exit(20)

#ruta al script en bash
ej1_y_lista_parametros = ['/home/alumno/Escritorio/hola/Obligatorio/PRUEBA.sh']

if args.recursive:
    ej1_y_lista_parametros.append("-r")
#agrego el parametro como string a la lista   
if args.user:
    ej1_y_lista_parametros.append("-u")
    ej1_y_lista_parametros.append(args.user)

process=Popen(ej1_y_lista_parametros, stdout = PIPE, stderr = PIPE)
output=process.communicate()

#=======================================================================================
#                                      Salida de error 
#=======================================================================================
if process.returncode > 0:
    print(output[1].decode(), file = sys.stderr, end="")
    exit(process.returncode)
#=======================================================================================
#=======================================================================================
#                                        Opcion -r y -u
#=======================================================================================
#=======================================================================================

#opcion -r
if args.recursive == True:
    print(output[0].decode(), file=sys.stdout)


#opcion -u
if args.user != None:
    print(output[0].decode(), file=sys.stdout)
#=======================================================================================
#=======================================================================================
#                                        Opcion -o u
#=======================================================================================
#=======================================================================================
if args.order == "u":
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for linea in lista:
        usuario=linea[0:7]
        terminal=linea[9:21]
        host=linea[22:39]
        fecha=linea[39:50]
        hcon=linea[50:55]
        hdest=linea[57:65]
        tcon=linea[65:72]
        dic={"usuario":usuario, "terminal":terminal, "host":host, "fecha":fecha, "hcon":hcon, "hdest":hdest, "tcon":tcon }
        otra_lista.append(dic)
    otra_lista.sort(key=lambda x: x["usuario"])
    
    #print(otra_lista[3]["usuario"])
    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    for i in range(len(otra_lista)):
        for k in claves:    
            print(otra_lista[i][k],end="")
        print()
#=======================================================================================
#=======================================================================================
#                                        Opcion -o t
#=======================================================================================
#=======================================================================================
        
        
if args.order == "t":
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for linea in lista:
        usuario=linea[0:7]
        terminal=linea[9:21]
        host=linea[22:39]
        fecha=linea[39:50]
        hcon=linea[50:55]
        hdest=linea[57:65]
        tcon=linea[65:72]
        dic={"usuario":usuario, "terminal":terminal, "host":host, "fecha":fecha, "hcon":hcon, "hdest":hdest, "tcon":tcon }
        otra_lista.append(dic)
    otra_lista.pop(len(otra_lista)-1)
    otra_lista.sort(key=lambda x: x["terminal"])
    
    #print(otra_lista[3]["usuario"])
    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    for i in range(len(otra_lista)):
        for k in claves:
            print(otra_lista[i][k],end="")
        print()
#=======================================================================================
#=======================================================================================
#                                        Opcion -o h
#=======================================================================================
#=======================================================================================

if args.order == "h":
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for linea in lista:
        usuario=linea[0:7]
        terminal=linea[9:21]
        host=linea[22:39]
        fecha=linea[39:50]
        hcon=linea[50:55]
        hdest=linea[57:65]
        tcon=linea[65:72]
        dic={"usuario":usuario, "terminal":terminal, "host":host, "fecha":fecha, "hcon":hcon, "hdest":hdest, "tcon":tcon }
        otra_lista.append(dic)
    #aca es necesario hacer un pop para borrar los cabezales y el final que esta vacio, sino la saida queda mal
    titulos1=otra_lista[0]
    otra_lista.pop(len(otra_lista)-1)
    otra_lista.pop(0)
    otra_lista.sort(key=lambda x: x["host"])

    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    for i in range(1):
        for k in claves:
            print(titulos1[k],end="")
    print()
    for i in range(len(otra_lista)):
        for k in claves:
            print(otra_lista[i][k],end="")
        print()

#=======================================================================================
#=======================================================================================
#                                        Opcion -o d
#=======================================================================================
#=======================================================================================

if args.order == "d":
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for linea in lista:
        usuario=linea[0:7]
        terminal=linea[9:21]
        host=linea[22:39]
        fecha=linea[39:50]
        hcon=linea[50:55]
        hdest=linea[57:65]
        tcon=linea[65:72]
        dic={"usuario":usuario, "terminal":terminal, "host":host, "fecha":fecha, "hcon":hcon, "hdest":hdest, "tcon":tcon }
        otra_lista.append(dic)
    #aca es necesario hacer un pop para borrar los cabezales y el final que esta vacio, sino la saida queda mal
    titulos1=otra_lista[0]
    otra_lista.pop(len(otra_lista)-1)
    otra_lista.pop(0)
    otra_lista.sort(key=lambda x: x["tcon"])

    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    for i in range(1):
        for k in claves:
            print(titulos1[k],end="")
    print()
    for i in range(len(otra_lista)):
        for k in claves:
            print(otra_lista[i][k],end="")
        print()
#=======================================================================================
#=======================================================================================
#                                        Opcion I
#=======================================================================================
#=======================================================================================

if args.invert:
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for linea in lista:
        usuario=linea[0:7]
        terminal=linea[9:21]
        host=linea[22:39]
        fecha=linea[39:50]
        hcon=linea[50:55]
        hdest=linea[57:65]
        tcon=linea[65:72]
        dic={"usuario":usuario, "terminal":terminal, "host":host, "fecha":fecha, "hcon":hcon, "hdest":hdest, "tcon":tcon }
        otra_lista.append(dic)
    #aca es necesario hacer un pop para borrar los cabezales y el final que esta vacio, sino la saida queda mal
    titulos1=otra_lista[0]
    otra_lista.pop(len(otra_lista)-1)
    otra_lista.pop(0)
    otra_lista.sort(key=lambda x: x["usuario"], reverse=True)

    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    for i in range(1):
        for k in claves:
            print(titulos1[k],end="")
    print()
    for i in range(len(otra_lista)):
        for k in claves:
            print(otra_lista[i][k],end="")
        print()

#=======================================================================================
#=======================================================================================
#                                        Opcion F
#=======================================================================================
#=======================================================================================

#=======================================================================================
#                                        Opcion -f u
#=======================================================================================



if args.filter == "u":
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for linea in lista:
        #usuario=linea[0:7]
        terminal=linea[9:21]
        host=linea[22:39]
        fecha=linea[39:50]
        hcon=linea[50:55]
        hdest=linea[57:65]
        tcon=linea[65:72]
        dic={ "terminal":terminal, "host":host, "fecha":fecha, "hcon":hcon, "hdest":hdest, "tcon":tcon }
        otra_lista.append(dic)
    #aca es necesario hacer un pop para borrar los cabezales y el final que esta vacio, sino la saida queda mal
    titulos1=otra_lista[0]
    otra_lista.pop(len(otra_lista)-1)
    otra_lista.pop(0)

    claves=["terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    for i in range(1):
        for k in claves:
            print(titulos1[k],end="")
    print()
    for i in range(len(otra_lista)):
        for k in claves:
            print(otra_lista[i][k],end="")
        print()

#=======================================================================================
#                                        Opcion -f t
#=======================================================================================

#filtrador=[]

#if args.filter == "t":
#    filtrador.append("terminal")
#if args.filter == "h":
#    filtrador.append("host")
#if args.filter == "f":
#    filtrador.append("fecha")

#if filtrador != None:
#    print(filtrador)

'''
    lista=output[0].decode().split("\n")
    otra_lista=[]
    for linea in lista:
        usuario=linea[0:7]
        terminal=linea[9:21]
        host=linea[22:39]
        fecha=linea[39:50]
        hcon=linea[50:55]
        hdest=linea[57:65]
        tcon=linea[65:72]
        if x=="usuario":
            dic={ "terminal":terminal, "host":host, "fecha":fecha, "hcon":hcon, "hdest":hdest, "tcon":tcon }
            claves=["terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    
        otra_lista.append(dic)
    #aca es necesario hacer un pop para borrar los cabezales y el final que esta vacio, sino la saida queda mal
    titulos1=otra_lista[0]
    otra_lista.pop(len(otra_lista)-1)
    otra_lista.pop(0)

    for i in range(1):
        for k in claves:
            print(titulos1[k],end="")
    print()
    for i in range(len(otra_lista)):
        for k in claves:
            print(otra_lista[i][k],end="")
        print()
'''

#=======================================================================================
#                                        Opcion -f h
#=======================================================================================


#=======================================================================================
#                                        Opcion -f f
#=======================================================================================


#=======================================================================================
#                                        Opcion -f c
#=======================================================================================


#=======================================================================================
#                                        Opcion -f n
#=======================================================================================


#=======================================================================================
#                                        Opcion -f d
#=======================================================================================

