#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools

import struct



class commands():
	"""Comandos para impresora fiscal bixolon SRP-150, he pasado todos los comandos hexadecimales
	que aparecen en el manual para poder trabajar con python struct mas tranquilo """

	#Abre el comando desde el controlador a la impresora
	CMD_OPEN_COMMAND = 160	

	"""Obtiene el valor del estado secundario de la impresora."""
	CMD_OBT_SYS_SEC_STATE= 01

	"""Configura la fecha y hora. En caso de estar en estado primario 'No Asignada'
	permite configurar cualquier hora, en otro caso, solo una variacion de hasta 2 horas
	del original."""
	CMD_CONF_FECHAHORA= 16

	"""Obtiene la configuracion de hora del dispositivo."""
	CMD_OBT_CONF_FECHA_HORA =17

	"""Entrega los datos del contribuyente a la impresora fiscal. Es necesario estado
	primario 'No asignada'."""
	CMD_CONF_DATOS_FISCALIZACION = 18

	"""Configura el descuento maximo que se puede hacer en una boleta. Solo valido para
	estado primario 'No asignada'."""
	CMD_CONF_MAX_PORC_DESCUENTO= 19

	"""Obtiene los datos del contribuyente."""
	CMD_OBT_DATOS_FISCALIZACION = 20

	"""Configura el texto una de las lineas de encabezado (0 a 9)."""
	CMD_CONF_LINEAS_ENCABEZADO = 21

	"""Obtiene el texto de una de las lineas de encabezado."""
	CMD_OBT_CONF_LINEAS_ENCABEZADO = 22

	"""Configura el texto una de las lineas de cola (0 a 9)."""
	CMD_CONF_LINEAS_COLA = 23

	"""Obtiene el texto de una de las lineas de cola."""
	CMD_OBT_CONF_LINEAS_COLA = 24

	"""Configura y activa el tipo de pago especificado, con la descripcion especificada."""
	CMD_CONF_TIPO_PAGO= 25

	"""Obtiene el texto de una de las lineas de uno de los tipos de pago."""
	CMD_OBT_TIPO_PAGO = 26

	"""Configura las claves privadas y publicas de la firma digital.
	Solo valido para 'No Asignada.'"""
	CMD_CONF_CLAVES = 27

	"""Obtiene la clave publica de la firma digital"""
	CMD_OBT_CLAVE_PUBLICA = 28

	"""Inicia la carga de un logo en la impresora."""
	CMD_INICIAR_CARGA_LOGOS = 29

	"""Envia un paquete del logo que esta recibiendo la impresora correspondiente a una fila."""
	CMD_ENVIAR_LOGOS_USUARIO = 30

	"""Imprime el logo correspondiente al numero entregado. Solo valido en estado
	secundario jornada no iniciada."""
	CMD_PRINT_LOGO = 31

	"""Cancela la carga de logos."""
	CMD_CANCELAR_CARGA_LOGOS = 32 #

	"""Avanza lineas."""
	CMD_FF = 48

	"""Avanza lineas."""
	CMD_LF = 49

	"""Avanza N lineas, segun el parametro que se le pasa."""
	CMD_FF_N = 50

	"""Suena la campana"""
	CMD_CMD_BELL= 51

	"""Corta el papel."""
	CMD_CMD_CUT = 52

	"""Salta N lineas y corta el papel."""
	CMD_CMD_CUT_N = 53


	"""Realiza un cierre de la jornada Fiscal. Debe ejecutarse en estado secundario
	'jornada fiscal abierta'."""
	CMD_CIERRE_Z = 64

	"""Inicializa un reporte de informes Z por rango de fechas. Se debe ejecutar en estado
	secundario 'jornada fiscal inicializada' o 'jornada fiscal no inicializada'."""
	CMD_INIC_INFO_Z_POR_FECHA = 66

	"""Inicializa un reporte de informes Z por rango de numero. Se debe ejecutar en estado
	secundario 'jornada fiscal inicializada' o 'jornada fiscal no inicializada'."""
	CMD_INIC_INFO_Z_POR_CIERRES = 67

	"""Inicializa un reporte de transacciones por rango de fechas. Se debe ejecutar en
	estado secundario 'jornada fiscal inicializada' o 'jornada fiscal no inicializada'."""
	CMD_INFO_TRANSAC_RANGO_FECHAS = 73

	"""Inicializa un reporte de transacciones por rango de numero. Se debe ejecutar en
	estado secundario 'jornada fiscal inicializada' o 'jornada fiscal no inicializada'."""
	CMD_INFO_TRANSAC_RANGO = 74

	"""Obtiene los siguientes datos del informe ya abierto. Para que este comando funcione
	debe haberse abierto alguno de los 4 tipos de informes mencionados anteriormente.
	En caso de existir datos, devuelve respuesta exito y los valores. En caso de haber
	terminado, devuelve RESP_FIN_INFORME."""
	CMD_OBTENER_SIG_DATOS_INFORME = 75

	"""Cierra el informe abierto, imprimiendo los totales si corresponde. Entrega los datos
	de tipos de pago y serial para incluirlos en el archivo de informe. Para que este comando
	funcione debe haberse abierto alguno de los 4 tipos de informes mencionados	anteriormente."""
	CMD_FINALIZAR_INFORME= 76

	"""Cancela el informe abierto, volviendo al estado anterior de la impresora. Para que
	este comando funcione debe haberse abierto alguno de los 4 tipos de informes mencionados
	anteriormente."""
	CMD_CANCELAR_INFORME = 77

	CMD_ABRIR_BOLETA_FISCAL = 80

	"""Agrega un item adicional a la boleta fiscal, segun el texto, valor y cantidad
	entregada. Debe estar en estado secundario boleta fiscal abierta."""
	CMD_ITEM_BF = 81

	"""Imprime el subtotal de la boleta y lo envia por la puerta serial. Debe estar en estado
	boleta abierta."""
	CMD_SUBTOTAL_BF = 82

	"""Agrega un descuento o un cargo a la boleta fiscal."""
	CMD_DESC_REC_BF = 83

	"""Agrega un pago a la boleta fiscal.. Este comando no imprime los valores hasta cerrar
	la boleta fiscal."""
	CMD_PAGOS_BF = 84

	"""Cierra una boleta fiscal. Este comando genera la impresion de los totales y las
	transacciones correspondientes."""
	CMD_CERRAR_BF = 85

	"""Agrega una donacion a la boleta fiscal, descontandolo del vuelto."""
	CMD_DONACIONES_BF = 91


	"""Obtiene el resto que queda por pagar en una Boleta Fiscal. Solo valido si el estado
	secundario es Boleta Fiscal Pago."""
	CMD_OBT_RESTO_BF = 92


	"""Abre un documento no fiscal."""
	CMD_ABRIR_DNF = 96

	"""Envia un texto para ser impreso en el documento no Fiscal."""
	CMD_IMP_TEXTO_DNF = 97

	"""Cierra un documento no fiscal."""
	CMD_CERRAR_DNF = 98

	"""Abre un documento no fiscal de Medio de Pago."""
	CMD_ABRIR_DNFMP = 112

	"""Envia un texto para ser impreso en el documento de Medio de Pago."""
	CMD_IMP_TEXTO_DNFMP=  113

	"""Cierra un documento de medio de pago."""
	CMD_CERRAR_DNFMP = 114

	"""Abre el cajon de dinero."""
	CMD_ABRIR_CAJON = 74

	"""Envia el texto con el serial de la impresora, y la deja en estado certificado."""
	CMD_CERTIFICAR = 121

	"""Imprime el serial de la impresora."""
	CMD_GETSERIAL = 123

	"""Obtiene la firma segun los datos enviados como informe. Este comando puede
	tardar algunos segundos en procesar (tipicamente 90 segundos)."""
	CMD_GETSIGN = 124

	"""Solo entrega una respuesta Exito de la impresora."""
	CMD_PING = 126

	"""Entrega el numero de boleta actual."""
	CMD_GETNBOL = 127
	

	"""Entrega el valor que queda restante para poder cerrar la boleta."""
	CMD_GETRESTANTE = 128

	"""Imprime Comprobante para tarjeta de Credito."""
	CMD_IMP_TARDATA_DNFMP = 129

	""" NOTA @pcaceres : los siguiente dos comandos estan mal las documentaciones
	(La dumentacion de devoluciones esta en el proximo comando .....)"""
	CMD_DEVOLUCION = 130

	"""  Comando de devolucion se utiliza tanto para devolver productos de ventas
	anteriores, como para descontar productos de la misma boleta.
	La unica restriccion es que el subtotal temporal despues de la devolucion
	debe ser mayor a 0.Es decir, al menos debe quedar $1 por pagar.
	(la boleta nunca quedara en negativo ni en 0)."""
	CMD_GETNZ = 131


	"""NOTA @pcaceres : retorna los datos de la jornada, no hay documentacion en el documento """
	CMD_GET_DATOS_JORNADA = 132

	""" Emite un informe X por comando serial. """
	CMD_INFX = 133
	
	CM_PING = 126

	def openballot(self, seq=1):
		"""
		Abre una boleta, imprimiendo los datos del contribuyente, un logo y las lineas de
		encabezado si corresponde. Se debe ejecutar en estado secundario 'jornada fiscal inicializada' o
		'jornada fiscal	no inicializada' . En caso de ni inicializada, la abre automaticamente.
		"""
		# Herramientas de convercion de datos a hexadecimal y calculo de CRC32
		# Paquete de datos especifico para abrir una boleta fiscal
		package = (self.CMD_ABRIR_BOLETA_FISCAL,04,00,00,01,00)
		# formato del paquete de datos
		s = struct.Struct('6B')
		# paquete de datos en hexa
		paquetehexa = s.pack(*package)
		# crc calculado
		crc= tools.crc32(paquetehexa)
		# tamanio del paquete de datos
		datalen= s.size

		#formato de envio del paquete de datos
		command= struct.Struct('13B')
		print (self.CMD_OPEN_COMMAND,
					seq,
					datalen,
					int(crc[2:4], 16),
					int(crc[4:6], 16),
					int(crc[6:8], 16),
					int(crc[8:10], 16),
					package[0],
					package[1],
					package[2],
					package[3],
					package[4],
					package[5])
		return command.pack(
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0],
			package[1],
			package[2],
			package[3],
			package[4],
			package[5])

	def ping(self, seq=1):
		"""
		Suena la campana
		"""

		#formato del paquete de datos (son 8 "bits")
		format = '2B'
		#tamanio del paquete de datos
		datalen= 01
		#paquete de datos especificos para abrir la boleta fiscal
		package = (self.CMD_PING)

		paquetehexa= struct.pack('B',self.CMD_PING)
		crc= tools.crc32(paquetehexa)
		
		command = struct.pack(format,
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0])
		return command

	def bell(self, seq=1):
		"""
		Suena la campana
		"""

		#formato del paquete de datos (son 8 "bits")
		format = '8B'
		#tamanio del paquete de datos
		datalen= 01
		#paquete de datos especificos para abrir la boleta fiscal
		package = (self.CMD_CMD_BELL,0)

		paquetehexa= struct.pack('B',self.CMD_CMD_BELL)
		crc= tools.crc32(paquetehexa)
		
		command = struct.pack(format,
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0])
		return command

	def zreport(self, seq=1):
		"""
		Imprime el reporte Z

		nota: no lo imprime si la impresora no tiene boletas abiertas en la jornada fiscal
		"""

		#formato del paquete de datos (son 8 "bits")
		format = 'BBBBBBBBBB'
		#tamanio del paquete de datos
		datalen= 03
		#paquete de datos especificos para abrir la boleta fiscal
		package = (self.CMD_CIERRE_Z, 1,0)

		paquetehexa= struct.pack('BBB',self.CMD_CIERRE_Z, 1,0)
		crc= tools.crc32(paquetehexa)
		
		command = struct.pack(format,
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0],
			package[1],
			package[2])
		return command

	def xreport(self, seq=1):
		"""
		Imprime el reporte X
		"""

		#formato del paquete de datos (son 8 "bits")
		format = 'BBBBBBBBBB'
		#tamanio del paquete de datos
		datalen= 03
		#paquete de datos especificos para abrir la boleta fiscal
		package = (self.CMD_INFX, 1,0)

		paquetehexa= struct.pack('BBB',self.CMD_INFX, 1,0)
		crc= tools.crc32(paquetehexa)
		
		command = struct.pack(format,
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0],
			package[1],
			package[2])
		return command
	def addItem(self, seq=2, descripcion="Hub USB", valor=1,  cantidad=10):
		"""
		Agrega un item a la boleta fiscal

		"""

		cant1= cantidad / 1000
		cant2= cantidad % 1000

		valorenBits= (  (0xFF000000 & valor)>>24,(0xFF0000 & valor)>>16,(0xFF00 & valor)>>8,(0xFF & valor))

		strings = ""
		descripcionlen= len(descripcion)
		packageValues = (self.CMD_ITEM_BF,
			9 + descripcionlen ,
			(0xFF00 & cant2)>>8 , (0xFF & cant2),
			(0xFF00 & cant1)>>8 , (0xFF & cant1),
			valorenBits[0] ,valorenBits[1],
			valorenBits[2], valorenBits[3] ,
			descripcionlen )
		for letter in descripcion:
		 	packageValues += (letter,)
		 	strings += 's '
		s = struct.Struct('11B '+ strings)

		paquetehexa= s.pack(*packageValues)
		datalen= s.size

		crc= tools.crc32(paquetehexa)
		
		command= struct.Struct('18B' + strings)

		datacommand= (self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10],16),
			packageValues[0],
			packageValues[1],
			packageValues[2],
			packageValues[3],
			packageValues[4],
			packageValues[5],
			packageValues[6],
			packageValues[7],
			packageValues[8],
			packageValues[9],
			packageValues[10])
		for letter in descripcion :
			datacommand += (letter,)
		print datacommand
		return command.pack(*datacommand)


	def subtotal(self, seq=3):
		"""agrega el sub total a la boleta"""

		#formato del paquete de datos (son 13 "bits")
		format = '10B'
		#tamanio del paquete de datos
		datalen= 03
		#paquete de datos especificos para abrir la boleta fiscal
		package = (self.CMD_SUBTOTAL_BF,1,1)

		paquetehexa= struct.pack('3B',self.CMD_SUBTOTAL_BF,1,1)
		crc= tools.crc32(paquetehexa)
		
		command = struct.pack(format,
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0],
			package[1],
			package[2])
		return command

	def close(self, seq=4):
		"""
		Cierra la boleta fiscal
		"""

		#formato del paquete de datos (son 13 "bits")
		format = '11B'
		#tamanio del paquete de datos
		datalen= 04
		#paquete de datos especificos para abrir la boleta fiscal
		package = (self.CMD_CERRAR_BF,2,0,1)

		paquetehexa= struct.pack('4B',self.CMD_CERRAR_BF,02,00,01)
		crc= tools.crc32(paquetehexa)
		
		command = struct.pack(format,
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0],
			package[1],
			package[2],
			package[3])
		return command


	def openbox(self, seq=1):
		"""Cierra una boleta fiscal"""

		#formato del paquete de datos (son 9 "bits")
		format = '9B'
		#tamanio del paquete de datos
		datalen= 02
		#paquete de datos especificos para abrir la boleta fiscal
		package = (self.CMD_ABRIR_CAJON,0)

		paquetehexa= struct.pack('2B',self.CMD_GETNBOL,0)
		crc= tools.crc32(paquetehexa)
		
		command = struct.pack(format,
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0],
			package[1]
			)
		'''
long COcxsam350Ctrl::abrircajon() 
{

unsigned char msg[]={0x74, 0};
unsigned char buff[4];
CrcBytes(msg,2,buff);
PortWrite(0xA0);

PortWrite(seq);
seq++;
PortWrite(2);
PortWrite(buff[0]);
PortWrite(buff[1]);
PortWrite(buff[2]);
PortWrite(buff[3]);
for (int k=0; k<2; k++) PortWrite(msg[k]);
return esperarespuesta();

	// TODO: Add your dispatch handler code here

	return 0;
}

'''

		return command


	def pagos(self, seq=5,tipo=0, valor=10000 ):
		"""agrega un pago a la boleta"""

		#formato del paquete de datos (son 13 "bits")
		format = '14B'
		#tamanio del paquete de datos
		datalen= 07
		#paquete de datos especificos para abrir la boleta fiscal
		package = (self.CMD_PAGOS_BF,
			05,
			tipo,
			(0xFF000000 & valor)>>24,
			(0xFF0000 & valor)>>16,
			(0xFF00 & valor)>>8,
			(0xFF & valor))

		paquetehexa= struct.pack('7B',self.CMD_PAGOS_BF,
			05,
			tipo,
			(0xFF000000 & valor)>>24,
			(0xFF0000 & valor)>>16,
			(0xFF00 & valor)>>8,
			(0xFF & valor))
		crc= tools.crc32(paquetehexa)
		
		command = struct.pack(format,
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0],
			package[1],
			package[2],
			package[3],
			package[4],
			package[5],
			package[6])
		return command
	def cerrar(self,seq=6):
		"""Cierra una boleta fiscal"""

		#formato del paquete de datos (son 13 "bits")
		format = '11B'
		#tamanio del paquete de datos
		datalen= 04
		#paquete de datos especificos para abrir la boleta fiscal
		package = (self.CMD_CERRAR_BF, 2,0,1)

		paquetehexa= struct.pack('4B',self.CMD_CERRAR_BF, 2,0,1)
		crc= tools.crc32(paquetehexa)
		
		command = struct.pack(format,
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0],
			package[1],
			package[2],
			package[3])
		return command

	def ballotNumber(self, seq=1):
		"""Cierra una boleta fiscal"""

		#formato del paquete de datos (son 13 "bits")
		format = '9B'
		#tamanio del paquete de datos
		datalen= 02
		#paquete de datos especificos para abrir la boleta fiscal
		package = (self.CMD_GETNBOL,0)

		paquetehexa= struct.pack('2B',self.CMD_GETNBOL,0)
		crc= tools.crc32(paquetehexa)
		
		command = struct.pack(format,
			self.CMD_OPEN_COMMAND,
			seq,
			datalen,
			int(crc[2:4], 16),
			int(crc[4:6], 16),
			int(crc[6:8], 16),
			int(crc[8:10], 16),
			package[0],
			package[1]
			)
		return command


		
