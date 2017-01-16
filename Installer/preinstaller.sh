#!/bin/bash

#Este es el wrapper script para el juez en linea.
#Desarrollado por Licdo. Moisés Alvarado de la Facultad de Ciencias y Tecnologìa de la Honorable Universidad de Carabobo. Venezuela, Junio 2015.

#Funciones
function language()
{
	lan=$(locale | grep LANGUAGE | cut -d= -f2 | cut -d_ -f1)

	#Detectando el idioma del sistema:
	if [ "$lan" = "es" ]; then
	#Para idioma español:	
		mensajes=([no-space]="Insuficiente espacio en el disco...abortando." 
		[abortar]="abortando"
		[instalacion-fallida]="Instalación fallida del paquete"
	 	[instalacion-innecesaria]="No es necesario instalar el paquete"
	 	[instalacion-correcta]="Instalación del paquete...satisfactoria"
	 	[descarga]="Descargando -> "
	 	[extraccion]="Extrayendo -> "
	 	[ok]="Listo"
	 	[extraccion-error]="Error al descomprimir -> "
	 	[ejecutando]="Ejecutando"
	 	[md5-nok]="Comprobación fallida...descargando .md5 nuevamente..."
	 	[error-descarga]="Ops, algo salió mal. Volviendo a descargar archivos..."
	 	[paquete-ok]="Paquete Juez comprobado. Descarga exitosa."
	 	[no-internet]="No se detectó conexión a internet"
	 	#[]=""
	 	)
	else
	#para idioma ingles:
		mensajes=([no-space]="There is not enough disk space ... aborting." 
		[abortar]="aborting"
		[instalacion-fallida]="Package installation failed"
	 	[instalacion-innecesaria]="No need to install the package"
	 	[instalacion-correcta]="Package installation successful"
	 	[descarga]="Downloading -> "
	 	[extraccion]="Unpacking -> "
	 	[ok]="Ok"
	 	[extraccion-error]="unzip error -> "
	 	[ejecutando]="running"
	 	[md5-nok]="Failed to check files...downloading again .md5 ..."
	 	[error-descarga]="oops, something went wrong. Downloading files again..."
	 	[paquete-ok]="Judge package checked. successful download."
	 	[no-internet]="No internet connection"
	 	#[]=""
	 	)
	fi
}

function download() {	
    local url=$1
    echo -n "    "
    wget -P judge --progress=dot $url 2>&1|grep --line-buffered -o "[0-9]*%"|xargs -L1 echo -en "\b\b\b\b";echo
}

function downloadQ() {
	#esta idea pertenece a -> LOUIS MARASCIO, y puedes encontrarla en: http://fitnr.com/showing-file-download-progress-using-wget.html
    local url=$1
    wget -q -P judge $url 
}

#Esta función recibe el nombre de un paquete y verifica si está instalado. De no estarlo, lo instala.
function check_installed {

	dep=$(dpkg-query -W -f='${Status}' $1)
		
	if [ "$dep" != "install ok installed" ]; then

		sudo apt-get --assume-yes install ${1}
		#echo "esto es ->" $?
		#read -p "Press [Enter] key to start backup..."
		#Condicional que determina el estado que retorna el comando apt-get install git
		if [ $? -gt 0 ]; then
			echo ${mensajes[instalacion-fallida]} "${1}"
			exit 3
		else
			echo ${mensajes[instalacion-correcta]} "${1}"
		fi	
	else
		echo ${mensajes[instalacion-innecesaria]} "${1}"
	fi
}

function validate_download {

	#Se procede a generar el .md5 para el .zip recien descargado:
	cd judge && md5sum -c --status md5.txt
	
	while [ $? = 1 ]; do
		#Se borra el md5 actual:
		rm md5.txt

		cd ../

		#se descarga el md5 nuevamente:
		echo ${mensajes[md5-nok]}	
		file="md5.txt"
		download "https://raw.githubusercontent.com/m0ises2/juez/master/$file"
		
		#Se comprueba por segunda vez el .zip:
		cd judge && md5sum -c --status md5.txt

		if [ $? = 1 ]; then

			echo ${mensajes[error-descarga]}

			cd ../ && rm -r judge

			#cd judge && rm md5.txt && rm md5.txt~ && rm juez.zip  && cd../ && rm judge

			#Se descarga el .zip del juez: https://github.com/m0ises2/juez/blob/master/juez.zip?raw=true
			file="juez.zip"
			echo -e ${mensajes[descarga]} $file
			download "https://github.com/m0ises2/juez/raw/master/$file"

			#Se descarga el .md5 del .zip del juez: https://github.com/m0ises2/juez/blob/master/md5.txt
			file="md5.txt"
			echo -e ${mensajes[descarga]} $file
			download "https://raw.githubusercontent.com/m0ises2/juez/master/$file"

			#Se comprueba por segunda vez el .zip:
			cd judge && md5sum -c --status md5.txt
		fi
	done

	echo -e "\n"${mensajes[paquete-ok]}"\n"
}

function check_internet
{
	#Validar que exista conexión a internet:
	wget -q --tries=10 --timeout=20 --spider http://google.com #Si el comando arroja status 4, se interpreta como una inexistencia de conexión a internet.

	if [[ $? -eq 4 ]]; then
	    return 1 #Sin conexión a internet no se puede hacer nada.
	fi
	return 0
}

function main
{
	#Lista de mensajes:
	declare -A mensajes

	language

	#¿Cuantos cores posee la maquina?
	cores=$(nproc)

	#Validar que exista conexión a internet:

	if [ ! check_internet ]; then
		echo ${mensajes[no-internet]}
	    exit 1 #Sin conexión a internet no se puede hacer nada.
	fi

	#Comando para obtener el espacio libre expresado en kiloBytes
	used=$(df -k / | tail -1 | awk '{print $4}')

	#echo "$used"
	#Condicional que determina si el espacio libre es suficiente. Sino, retorna estatus 1.
	if ! [ "$used" -gt 1048576 ]; then
		echo ${mensajes[no-space]}
		exit 2 #Insuficiente espacio en el disco.
	fi

	#Chequear que GIT esté instalado:
	check_installed git

	#Chequear que Python 3 esté instalado:
	check_installed python3

	#Chequear si está instalado phyton3-dev:
	check_installed python3-dev

	#chequear Qt5:
	check_installed qt5-default

	#Chequear qt5-qmake
	check_installed qt5-qmake

	(
		#Se descarga el .zip del juez: https://github.com/m0ises2/juez/blob/master/juez.zip?raw=true
		file="juez.zip"
		downloadQ "https://github.com/m0ises2/juez/raw/master/$file"

		#Se descarga el .md5 del .zip del juez: https://github.com/m0ises2/juez/blob/master/md5.txt
		file="md5.txt"	
		downloadQ "https://raw.githubusercontent.com/m0ises2/juez/master/$file"
	) &

	#Chequear que SIP esté instalado:
	file="sip-4.16.7.tar.gz"
	echo -e "\n"${mensajes[descarga]} $file
	download "http://sourceforge.net/projects/pyqt/files/sip/sip-4.16.7/$file"

	echo -e "\n"${mensajes[extraccion]} $file
	cd judge && tar -zxf ${file}

	if [ $? -eq 0 ]; then
		echo -e "\n"${mensajes[ok]}
	else
		echo -e "\n"${mensajes[extraccion-error]} $file
		exit 4
	fi

	#Se procede a la ejecución del script de instalación para SIP(SIP is a tool that makes it very easy to create Python bindings for C and C++ libraries.):
	cd sip-4.16.7 && echo -e "\n"${mensajes[ejecutando]} "configure.py\n" && python3 configure.py && echo -e "\n"${mensajes[ejecutando]} "Makefile\n" && sudo make -j $cores && echo -e "\n"${mensajes[ejecutando]} "Make Install\n" && sudo make install -j $cores 
	#Se vuelve a la raiz:
	cd ../../

	#Chequear que PyQt5 esté instalado:
	file="PyQt-gpl-5.4.1.tar.gz"
	echo -e "\n"${mensajes[descarga]} $file
	download "http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.4.1/$file"

	echo -e "\n"${mensajes[extraccion]} $file
	cd judge && tar -zxf ${file}

	if [ $? -eq 0 ]; then
		echo -e "\n"${mensajes[ok]}
	else
		echo -e "\n"${mensajes[extraccion-error]} $file
		exit 4
	fi

	#Se procede a la ejecución del script de instalación para PyQt5:
	cd PyQt-gpl-5.4.1 && echo -e "\n"${mensajes[ejecutando]} "configure.py\n" && python3 configure.py --confirm-license && echo -e "\n"${mensajes[ejecutando]} "Makefile\n" && sudo make -j $cores && echo -e "\n"${mensajes[ejecutando]} "Make Install\n" && sudo make install -j $cores

	#Se vuelve a la raiz:
	cd ../../

	#Se realizan las validaciones necesarias con el fin de determinar si el paquete se descargó correctamente
	validate_download

	cd ../
	
	#Esperamos por todos los subprocesos a que terminen:
	wait

	#Se procede a ejecutar el python3-script de instalación:
	./config.py
}
#Fin de Funciones

#-----------------------------------------MAIN--------------------------------------------------------------#
main