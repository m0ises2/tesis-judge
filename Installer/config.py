#!/usr/bin/env python3

#Codigo desarrollado por: Moisés Alvarado
#twitter: m0ises2
#github: https://github.com/m0ises2
#email: moisesalvarado84@gmail.com

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from zipfile import ZipFile
from urllib.request import urlopen
from urllib.error import URLError


import subprocess
import threading
import functools
import logging
import shutil
import crypt
import pwd
import sys
import os


#Debugger:
import pdb

import interfaz_1
import interfaz_2
import interfaz_3
import interfaz_4

#-----------------------------------------------------------------------------------------Definición de clases para interfaz:------------------------------------------------------------------------------------------------------------#

class Instalador_interfaz_1(QDialog, interfaz_1.Ui_instalador_interfaz_1):
	
	def __init__(self, parent=None):
		super(Instalador_interfaz_1, self).__init__(parent)
		self.setupUi(self)

	def closeEvent(self, event):        
		reply = QMessageBox.question(self, 'Message',
			"¿Seguro que desea salir?", QMessageBox.Yes | 
				QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()	

class Instalador_interfaz_2(QDialog, interfaz_2.Ui_instalador_interfaz_2):
	def __init__(self, parent=None):
		super(Instalador_interfaz_2, self).__init__(parent)
		self.setupUi(self)
		self.LineUsuario.setValidator(QRegExpValidator(QRegExp("^[A-Za-z0-9]+$"), self))
		self.LineUsuario.setEnabled(False)
		self.LineUsuario.setText('admin')
		self.labelUsuario.setText('adminJuez')	
		self.usuario = ""
		self.contrasenha = ""

	def closeEvent(self, event):        
		reply = QMessageBox.question(self, 'Message',
			"¿Seguro que desea salir?", QMessageBox.Yes | 
				QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	@pyqtSlot("QString")
	def on_LineUsuario_textEdited(self):		
		texto = "admin_juez"
		self.labelUsuario.setText(texto)
		estado = False

		if self.contrasenha_1.text() and self.contrasenha_2.text() and self.LineUsuario.text():
			estado = True

		self.siguiente_2.setEnabled(estado)
	
	@pyqtSlot("QString")
	def on_contrasenha_2_textEdited(self):
		estado = False
		if self.contrasenha_1.text():
			if self.contrasenha_1.text() == self.contrasenha_2.text():
				res = "Coinciden"
				self.coincidencia.setStyleSheet('color: green')
				if self.LineUsuario.text():
					estado = True
					self.usuario = self.labelUsuario.text().lower()
					self.contrasenha = self.contrasenha_2.text().lower()
			else:
				res = "No coinciden"
				self.coincidencia.setStyleSheet('color: red')			
			
			self.coincidencia.setText(res)
			self.siguiente_2.setEnabled(estado)
		else:
			self.coincidencia.setText("")
			self.siguiente_2.setEnabled(estado)

	@pyqtSlot("QString")
	def on_contrasenha_1_textEdited(self):
		estado = False
		if self.contrasenha_1.text():
			if self.contrasenha_1.text() == self.contrasenha_2.text():
				res = "Coinciden"
				self.coincidencia.setStyleSheet('color: green')
				if self.LineUsuario.text():
					estado = True
			else:
				res = "No coinciden"
				self.coincidencia.setStyleSheet('color: red')
			
			self.coincidencia.setText(res)
			self.siguiente_2.setEnabled(estado)
		else:
			self.coincidencia.setText("")
			self.siguiente_2.setEnabled(estado)

	def get_usuario(self):
		return self.usuario

	def get_contrasenha(self):
		return self.contrasenha

class Instalador_interfaz_3(QDialog, interfaz_3.Ui_instalador_interfaz_3):
	def __init__(self, parent=None):
		super(Instalador_interfaz_3, self).__init__(parent)
		self.setupUi(self)

	def closeEvent(self, event):        
		reply = QMessageBox.question(self, 'Message',
			"¿Seguro que desea salir?", QMessageBox.Yes | 
				QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

class Instalador_interfaz_4(QDialog, interfaz_4.Ui_instalador_interfaz_4, QObject):

	#Señal para determinar cuando finaliza el proceso de instalación:
	sig = pyqtSignal()

	#Señal para aumentar la barra de progresos:
	aumentar = pyqtSignal(int)

	def __init__(self, parent=None):
		super(Instalador_interfaz_4, self).__init__(parent)
		self.setupUi(self)
		self.instalacionBar.setValue(0)
		self.barraValor = 0

	def closeEvent(self, event):        
		reply = QMessageBox.question(self, 'Message',
			"¿Seguro desea cancelar la instalación?", QMessageBox.Yes | 
				QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
			_stop.set()
		else:
			event.ignore()

	@pyqtSlot()
	def on_finalizar_clicked(self):
		sys.exit(0)

	def conectar_sig(self):
		self.sig.connect(self.actualizar)

	def emitir(self):
		if _stop.is_set():
			logging.critical(mensajes['mensajefinal1'])
		else:
			logging.info(mensajes['mensajefinal2'])

		self.sig.emit()

	def actualizar(self):
		self.finalizar.setEnabled(True)
		self.cancelar_4.setEnabled(False)

	def barra(self, cant):
		self.aumentar.emit(cant)

	def conectar_aumentar(self):
		self.aumentar.connect(self.aumentarBarra)

	def aumentarBarra(self, value):
		self.barraValor = self.barraValor + value
		self.instalacionBar.setValue(self.barraValor)

#--------------------------------------------------------------------------------Definición de funciones y procedimientos:-------------------------------------------------------------------------------------------------#

#Eventos de transición de ventanas:
def mostrar_siguiente(interfaz):

	if interfaz == "uno":
		uno_.hide()
		dos_.setGeometry(uno_.pos().x(), uno_.pos().y(), 684, 454)
		dos_.show()
	elif interfaz == "dos":
		dos_.hide()
		tres_.usuario.setText(dos_.usuario)		
		tres_.contrasenha.setText(dos_.contrasenha)
		tres_.setGeometry(dos_.pos().x(), dos_.pos().y(), 684, 454)
		tres_.show()
	elif interfaz == "tres":
		tres_.hide()
		cuatro_.setGeometry(tres_.pos().x(), tres_.pos().y(), 684, 454)
		cuatro_.show()

def mostrar_anterior(interfaz):
	if interfaz == "dos":
		dos_.hide()
		uno_.setGeometry(dos_.pos().x(), dos_.pos().y(), 684, 454)		
		uno_.show()
	elif interfaz == "tres":
		tres_.hide()
		dos_.setGeometry(tres_.pos().x(), tres_.pos().y(), 684, 454)
		dos_.show()	

#Configuración del logging:
def config_logger():
		
	if not	os.path.exists(dir_log):
		os.mkdir(dir_log)
	else:
		shutil.rmtree(dir_log);
		os.mkdir(dir_log)

	logging.basicConfig(filename='/var/log/jo+/juez.log', level=logging.DEBUG ,format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def config_lenguaje(idioma):
	if idioma == 'Spanish':
		mensajes = {
				'mensaje1':'Comprobando conexión a internet...',		
				'mensaje2':'No se detectó conexión a internet. Python3 error: ',
				'mensaje3':'Chequeando dependencias...',
				'mensaje4':'Se procede a chequear la lista de dependencias.',
				'mensaje5':'Comprobando ',
				'mensaje6':'Instalando ',
				'mensaje7':'Error de sistema operativo: Python3 error: ',
				'mensaje8':'No fue necesario instalar: ',
				'mensaje9':'No se pudo leer el archivo de dependencias. Python3 error: ',
				'mensaje10':'Se procede a crear la cuenta de usuario UNIX en el equipo.',
				'mensaje11':'Creando cuenta de administrador...',
				'mensaje12':'Error creando la cuenta de usuario UNIX. Python3 error: ',
				'mensaje13':'Reinicando Apache2.',
				'mensaje14':'Reiniciando Servicio Apache2...',
				'mensaje15':'Error reiniciando Apache2. Python3 error:',
				'mensaje16':'Moviendo archivos web del Juez JO+',
				'mensaje17':'Creando directorio',
				'mensaje18':'Directorio web para el Juez JO+ ya existía. Fue eliminado y se creó un directorio nuevo.',
				'mensaje19':'No se pudo crear el directorio web para el Juez JO+.',
				'mensaje20':'Configurando propietario y permisos para los archivos...',
				'mensaje21':'No se encontró el archivo .zip que contiene la interfaz web del Juez JO+.',
				'mensaje22':'Activando módulo rewrite de Apache2...',
				'mensaje23':'No se pudo activar el módulo rewrite. Python3 error: ',
				'mensaje24':'No se pudo configurar host para el Virtual Host. Python3 error: ',
				'mensaje25':'No se pudo configurar allowOverride en Apache2.conf. Python3 error:',
				'mensaje26':'Colocando el archivo vhost en /etc/apache/sites-available.',
				'mensaje27':'Configurando Virtual Host...',
				'mensaje28':'Habilitando Virtual host.',
				'mensaje29':'Escribiendo host en /etc/hosts...',
				'mensaje30':'Escribiendo el nuevo host en el archivo hosts(/etc/hosts).',
				'mensaje31':'Habilitando allowOverride de Apache2.',
				'mensaje32':'No se pudo habilitar Virtual Host. Python3 error: ',
				'mensaje33':'Cargando y Configurando la Base de Datos...',
				'mensaje34':'Cargando y Configurando la base de datos en postgresql.',
				'mensaje35':'Base de datos para Juez JO+ no pudo ser configurada correctamente. Python3 error: ',
				'mensaje36':'Completada.',
				'mensaje37':'No se pudo completar la instalación. Revise el archivo log.',
				'mensajefinal1':'Instalación fallida.',
				'mensajefinal2':'Instalación Completada.'
				}
	else:
		mensajes = {
				'mensaje1':'Checking Internet',		
				'mensaje2':'Could not detect internet connection. Python3 error: ',
				'mensaje3':'Checking dependencies...',
				'mensaje4':'We proceed to check the list of dependencies.',
				'mensaje5':'Checking ',
				'mensaje6':'Installing ',
				'mensaje7':'OS Error: Python3 error: ',
				'mensaje8':'No need to install: ',
				'mensaje9':'Could not read the dependencies file. Python3 error: ',
				'mensaje10':'We proceed to create the UNIX user account on the computer.',
				'mensaje11':'Creating administrator account...',
				'mensaje12':'Error creating administrator account. Python3 error: ',
				'mensaje13':'Restarting Apache2.',
				'mensaje14':'Restarting Servicio Apache2...',
				'mensaje15':'Error restarting apache2. Python3 error:',
				'mensaje16':'Moving Judge\'s files ',
				'mensaje17':'Making directory',
				'mensaje18':'The Judge\'s web directory already exists. It was removed and created again.',
				'mensaje19':'Could not create the Jusge\'s web directory.',
				'mensaje20':'Setting ownership and permissions for files...',
				'mensaje21':'The file containing the Judge\'s web files, was not found.',
				'mensaje22':'Enabling module rewrite for Apache2...',
				'mensaje23':'Error enabling the module rewrite. Python3 error: ',
				'mensaje24':'Failed to configure the virtual host. Python3 error: ',
				'mensaje25':'Could not set the AllowOverride in Apache2.conf. Python3 error:',
				'mensaje26':'Moving the vhost file to /etc/apache/sites-available.',
				'mensaje27':'Setting Virtual Host...',
				'mensaje28':'Enabling Virtual host.',
				'mensaje29':'Writing host on /etc/hosts...',
				'mensaje30':'Writing new host on the host\'s files(/etc/hosts).',
				'mensaje31':'Enabling allowOverride de Apache2.',
				'mensaje32':'Could not enable virtual host. Python3 error: ',
				'mensaje33':'Loading and configuring the database...',
				'mensaje34':'Loading and configuring the postgresql database.',
				'mensaje35':'The database could not be loaded. Python3 error: ',
				'mensaje36':'Completed.',
				'mensaje37':'The installation was not completed. Check the log file.',
				'mensajefinal1':'Installation failed',
				'mensajefinal2':'Installation Complete'
				}

	return mensajes

#------------------------------------------------------------------------------------------Núcleo del instalador:----------------------------------------------------------------------------------------------------------#

#Esta función permite saber si se disponde de una conexión a internet:
def internet():
	#Chequeo de conexión a internet:
	cuatro_.infor.setText(mensajes['mensaje1'])

	try:
		response = urlopen('http://74.125.196.105',timeout=1)
	except URLError as error:
		_stop.set()
		logging.critical(mensajes['mensaje2']+format(error))

#Esta función permite determinar si un paquete está instalado en el sistema.
def check(package):
	#esta función ejecuta en la consola del sistema el comando dpkg-query concatenado con el nombre
	#del paquete. Dicho comando evalua si el paquete está instalado.
	status = subprocess.getstatusoutput("dpkg-query -W -f='${Status}' " + package)	
	return status[1] == "install ok installed"  #está instalado en el sistema.

#Esta función lee el archivo dependencias.in que se encuentra en el directorio instalador/Dependencias
def chequear_dependencias():
	#Chequear el archivo de dependencias:
	cuatro_.infor.setText(mensajes['mensaje3'])
	logging.info(mensajes['mensaje4'])

	try:
		dependencias_file = open('dependencias/dependencias.in', 'r')

		with dependencias_file:
			for linea in dependencias_file:	
				cuatro_.infor.setText(mensajes['mensaje5'] + linea)
				logging.info(mensajes['mensaje5'] + linea)
				if not check(linea):
					logging.info(mensajes['mensaje6'] + linea)
					cuatro_.infor.setText(mensajes['mensaje6'] + linea)
					try:				
						os.system("apt-get --assume-yes install " + linea);
					except OSError as error:
						logging.critical(mensajes['mensaje7']+format(error))
						_stop.set()
				else:
					logging.info(mensajes['mensaje8']+linea);
	except IOError as file_error:
		dependencias_file = 0
		logging.critical(mensajes['mensaje9']+format(file_error))
		_stop.set()

def crear_cuenta():
	#primero se detecta si el usuario existe. En caso de existir, se le cambia la contraseña por la suministrada en la interfaz
	logging.info(mensajes['mensaje10'])
	try:	
		subprocess.call("useradd -m -p "+crypt.crypt(dos_.get_contrasenha(), "22")+" "+dos_.get_usuario(), shell=True)
		cuatro_.infor.setText(mensajes['mensaje11'])
	except OSError as error:
		_stop.set()
		logging.critical(mensajes['mensaje12']+format(error))

def reiniciar_apache2():
	logging.info(mensajes['mensaje13'])

	try:
		cuatro_.infor.setText(mensajes['mensaje14'])
		os.system("service apache2 restart")	
	except OSError as error:
		logging.error(mensajes['mensaje15']+format(error))

def colocar_archivos_web_juez():
	
	logging.info(mensajes['mensaje16']);
	id_usuario = int(subprocess.getstatusoutput('id -u '+dos_.get_usuario())[1])
	id_grupo_usuario = int(subprocess.getstatusoutput('id -g '+dos_.get_usuario())[1])
	
	cuatro_.infor.setText(mensajes['mensaje17']+juez_web_directorio+"...")

	#Crear el directorio:
	try:
		if os.path.exists(juez_web_directorio):
			shutil.rmtree(juez_web_directorio);
			logging.warning(mensajes['mensaje18']);
		
		os.mkdir(juez_web_directorio)		
	except OSError:
		logging.critical(mensajes['mensaje19'])
		_stop.set()

	#Descomprimir el juez en juez_web_directorio:
	if os.path.isfile('judge/juez.zip'):	
		with ZipFile('judge/juez.zip') as file:			
			file.extractall(juez_web_directorio)			

		cuatro_.infor.setText(mensajes['mensaje20'])	

		#Configurar propiedad de los archivos de la interfaz web a la cuenta recien creada:
		os.chown(juez_web_directorio, id_usuario, id_grupo_usuario)	
		os.chmod(juez_web_directorio, 0o711)	
		
		#Este ciclo me permitirá recorrer todo el arbol del subdirectorio y cambiar al propietario y otorgar permisos tipo 7-0-0.
		for raiz, dirs, files in os.walk(juez_web_directorio):		
			for subdirectorio in dirs:
				os.chown(os.path.join(raiz, subdirectorio), id_usuario, id_grupo_usuario)
				os.chmod(os.path.join(raiz, subdirectorio), 0o751)			
			for archivo in files:
				os.chown(os.path.join(raiz, archivo), id_usuario, id_grupo_usuario)
				os.chmod(os.path.join(raiz, archivo), 0o644)

	else:
		logging.critical(mensajes['mensaje21'])
		_stop.set()

def activar_mod_rewrite():
	#Activar el módulo rewrite(mod_rewrite) de apache2:
	try:
		cuatro_.infor.setText(mensajes['mensaje22'])
		subprocess.call('a2enmod rewrite', shell=True)
	except OSError as error:
		_stop.set()
		logging.critical(mensajes['mensaje23']+format(error))

def escribir_host():
	try:
		with open('/etc/hosts','r') as f:
			data = f.readlines()
			
			try:
				data.index('127.0.0.1\tjuez.com\n')
			except ValueError as e:
				data.insert(data.index('\n'),'127.0.0.1\tjuez.com\n')

		with open('/etc/hosts','w') as l:
			l.writelines(data)

	except IOError as error:
		_stop.set()
		logging.critical(mensajes['mensaje24']+format(error))

def permitir_allowoverride():

	try:
		with open('/etc/apache2/apache2.conf','r') as f:
			data = f.readlines()

			site = data.index('<Directory /var/www/>\n')	
			
			i = site+1
			go = True
			max_ = len(data)

			while go and i < max_:
				if data[i] == '\tAllowOverride None\n':
					data[i] = '\tAllowOverride All\n'
					go = False
				i += 1

		with open('/etc/apache2/apache2.conf','w') as l:
			l.writelines(data)
	except IOError as error:
		_stop.set()
		logging.critical(mensajes['mensaje25']+format(error))

def config_interfaz_web():
	logging.info(mensajes['mensaje26'])
	#Colocar el archivo vhost en /etc/apache/sites-available
	cuatro_.infor.setText(mensajes['mensaje27'])
	if not os.path.exists('/etc/apache2/sites-available/juez.conf'):	subprocess.call('cp vhost/juez.conf /etc/apache2/sites-available/',shell=True)
	
	#Ejecutar a2ensite juez.conf para habilitar el sitio virtual:
	try:
		logging.info(mensajes['mensaje28'])
		cuatro_.infor.setText(mensajes['mensaje28']+"...")
		subprocess.call('a2ensite juez.conf',shell=True)

		#Escribir host en /etc/hosts
		cuatro_.infor.setText(mensajes['mensaje29'])
		logging.info(mensajes['mensaje30'])
		escribir_host()

		#Configurar apache2.conf para permitier allowOverride All:
		logging.info(mensajes['mensaje31'])
		cuatro_.infor.setText(mensajes['mensaje31']+"...")
		permitir_allowoverride()
	except OSError as error:
		_stop.set()
		logging.critical(mensajes['mensaje32']+format(error))

def config_bd():
	cuatro_.infor.setText(mensajes['mensaje33'])
	logging.info(mensajes['mensaje34'])
	
	try:
		subprocess.call('sudo -i -u postgres psql < BD/bd1.sql',shell=True)
		subprocess.call('sudo -i -u postgres psql -d judge < BD/judge.sql',shell=True)
	except OSError as error:
		_stop.set()
		logging.critical(mensajes['mensaje35']+format(erro))

#Procedimiento que es ejecutado por el thread creado y que llevará a cabo todo el proceso de instalación:
def instalar():

	cuatro_.barra(5)

	#Previo a la instalación, se debe saber si existe conexión a internet:
	internet()

	cuatro_.barra(5)

	#Primer paso, chequear que las dependencias estén instaladas sino, instalarlas.
	if not _stop.is_set():	chequear_dependencias()	
	cuatro_.barra(5)
			
	#Segundo paso, crear la cuenta de usuario con la información suministrada por el usuario en la interfaz:
	if not _stop.is_set():	crear_cuenta()	
	cuatro_.barra(5)
	
	#Colocar los archivos web del juez en los directorios indicados:
	if not _stop.is_set():	colocar_archivos_web_juez()	
	cuatro_.barra(5)

	#Activar módulo rewrite de Apache2:
	if not _stop.is_set():	activar_mod_rewrite()	
	cuatro_.barra(5)
	
	#Configurar interfaz_web(virtaul host, allowOverride All y host de linux):
	if not _stop.is_set():	config_interfaz_web()	
	cuatro_.barra(5)
	
	#Configurar Base de Datos:
	if not _stop.is_set():	config_bd()	
	cuatro_.barra(5)
	
	#Reiniciar apache2 server:
	if not _stop.is_set():	reiniciar_apache2()	
	cuatro_.barra(5)
	
	if not _stop.is_set():
		cuatro_.infor.setText(mensajes['mensaje36'])
	else:
		cuatro_.infor.setText(mensajes['mensaje37'])
	cuatro_.barra(5)
		
	#Último paso, emitir una señal perzonalizada. Esta señal indica que la instalación finalizó correctamente y actualiza la interfaz para que el botón
	#de finalizar esté habilitado.
	cuatro_.emitir()

#Esta función inicia el proceso de instalación creando un hilo exclusivamente para la instalación:
def iniciar():
	#Inicio del proceso de instalación:
	tres_.hide()
	cuatro_.setGeometry(tres_.pos().x(), tres_.pos().y(), 684, 454)
	cuatro_.show()
	
	#Creando el hilo para el chequeo de dependencias:
	chequeo = threading.Thread(target=instalar)
	chequeo.daemon = True

	chequeo.start()

	
#------------------------------------------------------------------------------------------------------MAIN:---------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
	
    #Declaraciòn de la aplicación:
	app = QApplication(sys.argv)
	
	#Configuración de los traductores:
	locale = QLocale.system().languageToString(QLocale.system().language())
	qtTranslator1 = QTranslator()

	if qtTranslator1.load(locale+"_1.qm", "translate/English/"):	app.installTranslator(qtTranslator1);

	qtTranslator2 = QTranslator()
	if qtTranslator2.load(locale+"_2","translate/English/",".qm"):	app.installTranslator(qtTranslator2);

	qtTranslator3 = QTranslator()
	if qtTranslator3.load(locale+"_3","translate/English/",".qm"):	app.installTranslator(qtTranslator3);

	qtTranslator4 = QTranslator()
	if qtTranslator4.load(locale+"_4","translate/English/",".qm"):	app.installTranslator(qtTranslator4);

	#Declaración de las interfaces:
	uno_ = Instalador_interfaz_1()
	dos_ = Instalador_interfaz_2()
	tres_ = Instalador_interfaz_3()
	cuatro_ = Instalador_interfaz_4()

	#Definición del diccionario de mensajes:
	mensajes = config_lenguaje(locale)
	
	#Definición del archivo Log:	
	dir_log = "/var/log/jo+"
	config_logger()
	
	#Definiciones de variables:

	#Directorio donde está alojada la interfaz web del juez:
	juez_web_directorio = "/var/www/juez-JIO+"

	#Host para el juez:
	host = '127.0.0.1	juez.com\n'
	
	#Definiciones de eventos de botón:	
	#Para interfaz_1:
	uno_.cancelar.clicked.connect(uno_.close)	
	uno_.siguiente.clicked.connect(functools.partial(mostrar_siguiente, "uno"))

	#Para interfaz_2:
	dos_.cancelar_2.clicked.connect(dos_.close)
	dos_.siguiente_2.clicked.connect(functools.partial(mostrar_siguiente, "dos"))
	dos_.anterior_2.clicked.connect(functools.partial(mostrar_anterior, "dos"))	

	#Para interfaz 3:
	tres_.cancelar_3.clicked.connect(tres_.close)
	tres_.instalar.clicked.connect(iniciar)
	tres_.anterior_3.clicked.connect(functools.partial(mostrar_anterior, "tres"))

	#para interfaz 4:
	cuatro_.cancelar_4.clicked.connect(cuatro_.close)
	cuatro_.conectar_sig()
	cuatro_.conectar_aumentar()

	#Definición de los eventos de parada:
	_stop = threading.Event()

	#Mostrar y ejecutar la interfaz principal:
	uno_.show()

	app.exec_()


#Codigo desarrollado por: Moisés Alvarado
#twitter: m0ises2
#github: https://github.com/m0ises2
#email: moisesalvarado84@gmail.com