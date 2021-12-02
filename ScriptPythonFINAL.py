import subprocess
from subprocess import Popen, PIPE
import argparse
import sys 

parser = argparse.ArgumentParser()

parser.add_argument("-r", "--recursive", help="Muestra la salida de las horas", action="store_true")
parser.add_argument("-u", "--user", type=str , help="Muestra para un usuario en particular.")
parser.add_argument("-o", "--order", type=str, choices=["u", "t", "h", "d"], help="Ordena" )
parser.add_argument("-i", "--invert", help="Invierte la salida", action="store_true")
parser.add_argument("-f", "--filter", type=str, help="Filtra ", choices=["u", "t", "h", "f", "c", "n", "d"], action='append')


try:
 args = parser.parse_args()
except SystemExit as e:
 exit(25)

#ruta al script en bash
ej1_y_lista_parametros = ['/mnt/hgfs/ObligatorioPC/ScriptBashFinal.sh']


#agrego el parametro -r a la lista que envio
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
    otra_lista.pop(len(otra_lista)-1)
    otra_lista.pop(len(otra_lista)-1)
    linea_delfinal=otra_lista[len(otra_lista)-1]
    otra_lista.pop(len(otra_lista)-1)
    if args.invert == True:
        otra_lista.sort(key=lambda x: x["usuario"], reverse=True)
    else:
        otra_lista.sort(key=lambda x: x["usuario"])
    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    if args.filter != None:
        delet=(args.filter)
            
        for letra in delet:
            if letra == "u":
                claves.remove("usuario")
            if letra == "h":
                claves.remove("host")
            if letra == "t":
                claves.remove("terminal")
            if letra == "f":
                claves.remove("fecha")
            if letra == "c":
                claves.remove("hcon")
            if letra == "n":
                claves.remove("hdest")
            if letra == "d":
                claves.remove("tcon")

        if len(delet) == 7:
            print("Al menos un campo debe estar visible, no pudiéndose ocultar todos")
            exit(20)    
    

    for i in range(len(otra_lista)):
        for k in claves:    
            print(otra_lista[i][k],end="")
        print()

    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    for k in claves:
        print(linea_delfinal[k],end="")
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
    otra_lista.pop(len(otra_lista)-1)
    linea_delfinal=otra_lista[len(otra_lista)-1]
    otra_lista.pop(len(otra_lista)-1)
    if args.invert == True:
        otra_lista.sort(key=lambda x: x["terminal"], reverse=True)
    else:
        otra_lista.sort(key=lambda x: x["terminal"])
    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    if args.filter != None:
        delet=(args.filter)
    
        for letra in delet:
            if letra == "u":
                claves.remove("usuario")
            if letra == "h":
                claves.remove("host")
            if letra == "t":
                claves.remove("terminal")
            if letra == "f":
                claves.remove("fecha")
            if letra == "c":
                claves.remove("hcon")
            if letra == "n":
                claves.remove("hdest")
            if letra == "d":
                claves.remove("tcon")

        if len(delet) == 7:
            print("Al menos un campo debe estar visible, no pudiéndose ocultar todos")
            exit(20)
 
    for i in range(len(otra_lista)):
        for k in claves:    
            print(otra_lista[i][k],end="")
        print()
    
    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]    
    for k in claves:
        print(linea_delfinal[k],end="")
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
    otra_lista.pop(0)
    otra_lista.pop(len(otra_lista)-1)
    otra_lista.pop(len(otra_lista)-1)
    linea_delfinal=otra_lista[len(otra_lista)-1]
    otra_lista.pop(len(otra_lista)-1)
    if args.invert == True:
        otra_lista.sort(key=lambda x: x["host"], reverse=True)
    else:    
        otra_lista.sort(key=lambda x: x["host"])
    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    if args.filter != None:
        delet=(args.filter)
            
        for letra in delet:
            if letra == "u":
                claves.remove("usuario")
            if letra == "h":
                claves.remove("host")
            if letra == "t":
                claves.remove("terminal")
            if letra == "f":
                claves.remove("fecha")
            if letra == "c":
                claves.remove("hcon")
            if letra == "n":
                claves.remove("hdest")
            if letra == "d":
                claves.remove("tcon")

        if len(delet) == 7:
            print("Al menos un campo debe estar visible, no pudiéndose ocultar todos")
            exit(20)
                
    for i in range(1):
        for k in claves:
            print(titulos1[k],end="")
    print()
    for i in range(len(otra_lista)):
        for k in claves:    
            print(otra_lista[i][k],end="")
        print()
    
    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]    
    for k in claves:
        print(linea_delfinal[k],end="")
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
    otra_lista.pop(0)
    otra_lista.pop(len(otra_lista)-1)
    otra_lista.pop(len(otra_lista)-1)
    linea_delfinal=otra_lista[len(otra_lista)-1]
    otra_lista.pop(len(otra_lista)-1)
    if args.invert == True:
        otra_lista.sort(key=lambda x: x["tcon"], reverse=True)
    else:
        otra_lista.sort(key=lambda x: x["tcon"])
    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    if args.filter != None:
        delet=(args.filter)
            
        for letra in delet:
            if letra == "u":
                claves.remove("usuario")
            if letra == "h":
                claves.remove("host")
            if letra == "t":
                claves.remove("terminal")
            if letra == "f":
                claves.remove("fecha")
            if letra == "c":
                claves.remove("hcon")
            if letra == "n":
                claves.remove("hdest")
            if letra == "d":
                claves.remove("tcon")

        if len(delet) == 7:
            print("Al menos un campo debe estar visible, no pudiéndose ocultar todos")
            exit(20)
            
    for i in range(1):
        for k in claves:
            print(titulos1[k],end="")
        print()
    for i in range(len(otra_lista)):
        for k in claves:
            print(otra_lista[i][k],end="")
        print()

    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    for k in claves:
        print(linea_delfinal[k],end="")
    print()





#=======================================================================================
#=======================================================================================
#                                        Opcion I
#=======================================================================================
#=======================================================================================

if args.invert == True and args.filter == None and args.order == None:
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

if args.filter != None and args.order == None:
    lista=output[0].decode().split("\n")
    delet=(args.filter)
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
    otra_lista.pop(len(otra_lista)-1)
    otra_lista.pop(0)
    claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
    for letra in delet:
        if letra == "u":
            claves.remove("usuario")
        if letra == "h":
            claves.remove("host")
        if letra == "t":
            claves.remove("terminal")
        if letra == "f":
            claves.remove("fecha")
        if letra == "c":
            claves.remove("hcon")
        if letra == "n":
            claves.remove("hdest")
        if letra == "d":
            claves.remove("tcon")
    if args.recursive == True:
        linea_delfinal=otra_lista[len(otra_lista)-1]
        otra_lista.pop(len(otra_lista)-1)
        if len(delet) == 7:
            print("Al menos un campo debe estar visible, no pudiéndose ocultar todos")
            exit(20)
        else:
            for i in range(1):
                for k in claves:
                    print(titulos1[k],end="")
            print()
            for i in range(len(otra_lista)):
                for k in claves:
                    print(otra_lista[i][k],end="")
                print()
            claves=["usuario", "terminal", "host", "fecha", "hcon", "hdest", "tcon"]
            for k in claves:
                print(linea_delfinal[k],end="")
            print()

    else:
        if len(delet) == 7:
            print("Al menos un campo debe estar visible, no pudiéndose ocultar todos")
            exit(20)
        else: 
            for i in range(1):
                for k in claves:
                    print(titulos1[k],end="")
            print()
            for i in range(len(otra_lista)):
                for k in claves:
                    print(otra_lista[i][k],end="")
                print()
  
#=======================================================================================
#                               Imprimo la salida en pantalla 
#=======================================================================================
if args.filter == None and args.order == None and args.invert == False:
    print(output[0].decode(), file=sys.stdout)

if args.recursive == True:
    contador=output[0].decode().split("\n")
    if args.user != None:
        print("Cantidad de conexiones listadas para el usuario", args.user ,len(contador) - 5)
    else:
        print("Cantidad de conexiones listadas:",len(contador) - 5)
