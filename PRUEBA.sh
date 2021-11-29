#!/bin/bash


#primero generamos una variable vacia, y si matchea con la misma, se toma un rango que son las lineas de last contadas, y se realiza un for donde se imprime cada una de las que matchea
var=""


if [ "$*" == "$var" ]
then
    rango=$(last | egrep ".*[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | wc -l)
    
 
    echo  'Usuario  Terminal     Host              Fecha     H.con   H.Dest  T.Con'
    for i in $( seq 1 $rango )
    do
	echo "$(last | egrep ".*[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | head -$i | tail -1)"
    done
fi

        while getopts ":ru:" option
        do
         case "$option" in
         r) 
		 a=`last  | head -1`
                 if  [ "$a" == "" ]
                 then
                         echo "No se han encontrado conexiones para listar en el sistema.">&2
                 exit 0
                 fi
		 
		 if [ "$1" = "-r" ] && [ "$2" = "-r"  ]
		 then
			 echo "Cantidad de parámetros errónea, solo se aceptan los modificadores -r y -u '(seguido de un nombre de usuario)'">&2
			 exit 3
		 fi


	    if  [ "$1" = "-r" ] && [ "$2"  = "-u" ]
            then
                 continue
            else

		MINUTOS=`last  |  egrep -o "[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$"|egrep -o "[0-9][0-9][:][0-9][0-9]"|cut -d":" -f2| awk '{total = total + $1}END{print total}'`
		HORAS=`last  |  egrep -o "[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$"|egrep -o "[0-9][0-9][:][0-9][0-9]"|cut -d":" -f1| awk '{total = total + $1}END{print total}'`
		rango=$(last | egrep ".*[0-9][0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | wc -l)
		
    		echo  'Usuario  Terminal     Host              Fecha     H.con   H.Dest  T.Con'
		for i in $( seq 1 $rango )
		do
			echo "$(last | egrep ".*[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | head -$i | tail -1)"
		done



		if [ "$MINUTOS" -ge "60"  ]
		then
			resto_minutos=$( echo "$MINUTOS"%60 | bc)
			entero_minutos=$(( $MINUTOS / 60 ))
			MINUTOS=$resto_minutos
			HORAS="$(($HORAS + $entero_minutos))"
		fi



		if [ "$HORAS" -ge "24"  ]
		then
			parte_resto=$(echo "$HORAS"%24 | bc )
			parte_entera=$(( $HORAS / 24 ))
			HORAS=$parte_resto
			dias=$parte_entera
		fi
		

		if ! [ "$dias" = "" ]
		then
	    	echo El tiempo total de conexion es : "$dias" dias ,  "$HORAS"  horas y "$MINUTOS"  minutos.
		else
			echo El tiempo total de conexion es "$HORAS" horas y "$MINUTOS" minutos.
		fi
		echo
            fi
                 ;;

         u) USER=${OPTARG}

                 if  [ "$2" = "-r" ] || [ "$3"  = "-r" ]
                 then
                         echo "Los modificadores deben colocarse en el orden -r y -u">&2
                         exit 6
                 fi

                 if ! grep -q "^$USER:" /etc/passwd
                 then
                         echo "No existe el usuario "$USER"  en el sistema.">&2
                         exit 2
                 fi
		
		 
		 
		 if  [ "$1" = "-r" ] || [ "$2"  = "-u" ]
                 then
			 if [ "$#" -gt "3"  ]
			 then
				 echo "Cantidad de parámetros errónea, solo se aceptan los modificadores -r y -u '(seguido de un nombre de usuario)'">&2
				 exit 3
			 fi
               		 
		 a="`last "$USER"| egrep ".*[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | head -1`"
                	 if  [ "$a" == "" ]
                	 then
                         	echo "No se han encontrado conexiones para listar en el sistema para el usuario "$USER".">&2
                	 exit 0
               		 fi




                rango=$(last "$USER" | egrep ".*[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | wc -l)

                echo  'Usuario  Terminal     Host              Fecha     H.con   H.Dest  T.Con'
		for i in $( seq 1 $rango )
                do
                echo "$(last "$USER" | egrep ".*[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | head -$i | tail -1)"
		done			 
			 
			 
			 
			 MINUTOS=`last "$USER"| egrep -o "[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$"|egrep -o "[0-9][0-9][:][0-9][0-9]"|cut -d":" -f2| awk '{total = total + $1}END{print total}'`
                	 HORAS=`last  "$USER" | egrep -o "[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$"|egrep -o "[0-9][0-9][:][0-9][0-9]"|cut -d":" -f1| awk '{total = total + $1}END{print total}'`
                	 rango=$(last "$USER" | egrep ".*[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | wc -l)
			
               		if [ "$MINUTOS" -ge 60  ]
                	then
                         	resto_minutos=$( echo "$MINUTOS"%60 | bc)
                         	entero_minutos=$(( $MINUTOS / 60 ))
                        	MINUTOS=$resto_minutos
                        	HORAS="$(($HORAS + $entero_minutos))"
                        fi



                	if [ "$HORAS" -ge "24"  ]
                	then
                        	parte_resto=$(echo "$HORAS"%24 | bc )
                        	parte_entera=$(( $HORAS / 24 ))
                        	HORAS=$parte_resto
                        	dias= $parte_entera
                	fi


                	if ! [ "$dias" = "" ]
                	then
                		echo El tiempo total de conexion es : "$dias" dias ,  "$HORAS"  horas y "$MINUTOS"  minutos.
                	else
                        	echo El tiempo total de conexion es "$HORAS" horas y "$MINUTOS" minutos.
                	fi
                	echo
			 
			 


		else

			k="`last "$USER" |egrep "[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$"| head -1`"
			if  [ "$k" == "" ]
			then
     				echo "No se han encontrado conexiones para listar en el sistema.">&2
     				exit 0
			fi

                rango=$(last "$USER" | egrep ".*[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | wc -l)

                echo  'Usuario  Terminal     Host              Fecha     H.con   H.Dest  T.Con'
                for i in $( seq 1 $rango )
                do
                echo "$(last "$USER" | egrep ".*[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | head -$i | tail -1)"
                done



                         MINUTOS=`last "$USER"| egrep -o "[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$"|egrep -o "[0-9][0-9][:][0-9][0-9]"|cut -d":" -f2| awk '{total = total + $1}END{print total}'`
                         HORAS=`last  "$USER" | egrep -o "[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$"|egrep -o "[0-9][0-9][:][0-9][0-9]"|cut -d":" -f1| awk '{total = total + $1}END{print total}'`
                         rango=$(last "$USER" | egrep ".*[0-9][ ][ ][(][0-9][0-9][:][0-9][0-9][)]$" | wc -l)



		 fi
                 ;;
         :)
                echo “No se ha especificado el usuario para el modificador -u.”>&2
                exit 1 ;;
	*) if [ "$#" -gt "3" ]
	 then
		 echo "Cantidad de parámetros errónea, solo se aceptan los modificadores -r y -u (seguido de un nombre de usuario">&2
		 exit 3
	 fi
		 echo "Modificador "$*" incorrecto. Solo se aceptan -r y -u usuario, y en ese orden en caso de estar ambos presentes.">&2 
		 exit 4
         ;;

         esac
        done



