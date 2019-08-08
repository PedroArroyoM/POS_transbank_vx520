#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct
import binascii


class Comando(object):
	"""Clase para definir la estructura de los comandos en general	"""
	def __init__(self, sequence=0):	
		self.packageFormat= "7B"
		self.dataformat = ""
		self.start     = 160
		self.sequence  = sequence
		self.datalen   = 0
		self.CRC0      = 0
		self.CRC1      = 0
		self.CRC2      = 0
		self.CRC3      = 0
		self.data      = ()
		self.package   = None

	def addData(self, data=None, dataformat='B'):
		if(isinstance(data, int)):
			self.datalen += 1
			self.data += (data,)
		elif(isinstance(data, str)):
			self.datalen += 1
			self.data += (data,)
		elif(isinstance(data, long)):
			self.datalen += 1
			self.data += (data,)
		else:
			self.datalen += len(data)
			self.data += data
		self.dataformat += dataformat
		s = struct.Struct(self.dataformat)
		data = s.pack(*self.data)
		self.calculateCRC(data)
		return self

	def createPackage(self, package=None):
		
		self.package = (
			self.start,
			self.sequence ,
			self.datalen,
			self.CRC0,
			self.CRC1,
			self.CRC2,
			self.CRC3,
			) + self.data
		s = struct.Struct(self.packageFormat + self.dataformat)
		self.packacte= s.pack(*self.package)
		return self

	def getPackage(self):
		return self.package

	def setSequence(self, sequence):
		self.sequence = sequence
		return self
	def calculateCRC(self , data):
		"""retorna el crc32 en hexadecimal"""
		crc32 ='%08X' % (binascii.crc32(data) & 0xffffffff)
		# crc32 = hex(binascii.crc32(data) & 0xffffffff)
		self.CRC0= int(crc32[0:2], 16)
		self.CRC1= int(crc32[2:4], 16)
		self.CRC2= int(crc32[4:6], 16)
		self.CRC3= int(crc32[6:8], 16)

class AbrirBoleta(Comando):
	"""Comando para abrir la boleta fiscal"""
	def __init__(self):
		super(AbrirBoleta, self).__init__()
		self.codigoComando= 80
		self.addData((self.codigoComando,04,00,00,01,00), '6B')
		
class AvanzayCorta(Comando):
	"""Comando para abrir la boleta fiscal"""
	def __init__(self):
		super(AvanzayCorta, self).__init__()
		self.codigoComando= 52
		self.addData((self.codigoComando,01,00), '3B')

class ReporteZ(Comando):
	"""Imprime un reporte Z de la jornada cerrandola, no se puede imprimir si la jornada fiscal
	no esta abierta """
	def __init__(self):
		super(ReporteZ, self).__init__()
		self.codigoComando= 64
		self.addData((self.codigoComando, 1,0), '3B')

class ReporteX(Comando):
	"""Imprime un  Reporte X """
	def __init__(self ):
		super(ReporteX, self).__init__()
		self.codigoComando =  133
		self.addData((self.codigoComando, 1,0), '3B')

class SubTotal(Comando):
	"""Imprime el subtotal en la boleta, solo funciona cuando la boleta esta abierta"""
	def __init__(self):
		super(SubTotal, self).__init__()
		self.codigoComando= 82
		self.addData((self.codigoComando,1,1), '3B')

class CierraBoleta(Comando):
	"""Cierra la boleta fiscal activa"""
	def __init__(self):
		super(CierraBoleta, self).__init__()
		self.codigoComando = 85
		self.addData((self.codigoComando,2,0,1), '4B')

class Pago(Comando):
	"""Ingresa un  pago a la boleta fiscal, no se pueden ingresar mas de 20 pagos o la impresora se bloquea
	asi que se tiene que completar el monto antes de eso """
	def __init__(self):
		super(Pago, self).__init__()
		self.codigoComando = 84
		self.addData((self.codigoComando, 05), '2B')

	def setTipoPago(self, tipoPago=0):
		self.addData(tipoPago, 'B')
		return self

	def setValor(self, valor=1):
		self.addData(((0xFF000000 & int(valor))>>24), 'B')
		self.addData(((0xFF0000 & int(valor))>>16), 'B')
		self.addData(((0xFF00 & int(valor))>>8), 'B')
		self.addData((0xFF & int(valor)), 'B')
		return self

class NumeroBoleta(Comando):
	"""La impresora retorna el numero de boleta   """
	def __init__(self):
		super(NumeroBoleta, self).__init__()
		self.codigoComando= 127
		self.addData((self.codigoComando,0), '2B')

class Descuento(Comando):
	"""Agrega un descuento a la boleta fiscal"""
	def __init__(self):
		super(Descuento, self).__init__()
		self.codigoComando= 83
		self.addData((self.codigoComando, 6 , 0), '3B')
	
	def setValor(self, valor=1):
		self.addData(((0xFF000000 & valor)>>24), 'B')
		self.addData(((0xFF0000 & valor)>>16),'B')
		self.addData(((0xFF00 & valor)>>8),'B' )
		self.addData((0xFF & valor), 'B')
		return self

	def setDescripcion(self, descripcion):
		datalist= list(self.data)
		datalist[1] += (len(descripcion))
		self.data = tuple(datalist)
		self.addData(len(descripcion), 'B')
		for letter in descripcion:
			self.addData(letter, 's')
		return self

class Recargo(Comando):
	"""Agrega un Recargo a la boleta fiscal"""
	def __init__(self):
		super(Recargo, self).__init__()
		self.codigoComando= 83
		self.addData((self.codigoComando, 6 , 1), '3B')
	
	def setValor(self, valor=1):
		self.addData(((0xFF000000 & valor)>>24), 'B')
		self.addData(((0xFF0000 & valor)>>16),'B')
		self.addData(((0xFF00 & valor)>>8),'B' )
		self.addData((0xFF & valor), 'B')
		return self

	def setDescripcion(self, descripcion="Recargo"):
		datalist= list(self.data)
		datalist[1] += (len(descripcion))
		self.data = tuple(datalist)
		self.addData(len(descripcion), 'B')
		for letter in descripcion:
			self.addData(letter, 's')
		return self

class Devolucion(Comando):
	"""Agrega un Devolucion a la boleta fiscal"""
	def __init__(self):
		super(Devolucion, self).__init__()
		self.codigoComando= 130
		self.addData((self.codigoComando, 5 ), '2B')
	
	def setValor(self, valor=1):
		self.addData(((0xFF000000 & valor)>>24), 'B')
		self.addData(((0xFF0000 & valor)>>16),'B')
		self.addData(((0xFF00 & valor)>>8),'B' )
		self.addData((0xFF & valor), 'B')
		return self

	def setDescripcion(self, descripcion="Devolucion"):
		datalist= list(self.data)
		datalist[1] += (len(descripcion))
		self.data = tuple(datalist)
		self.addData(len(descripcion), 'B')
		for letter in descripcion:
			self.addData(letter, 's')
		return self

class AgregarProducto(Comando):
	"""Agrega un producto a la boleta fiscal"""
	def __init__(self):
		super(AgregarProducto, self).__init__()
		self.codigoComando= 81
		self.datalen= 0
		self.addData((self.codigoComando,9), '2B')

	def setCantidadDEC(self,cantidad):
		entero = int("{:10.3f}".format(cantidad).split('.')[0])
		decimal = int("{:10.3f}".format(cantidad).split('.')[1])
		
		self.setCantidad2(entero*1000+decimal)
		return self
		
	def setCantidad(self, cantidad=1):
		if type(cantidad) is float:
			self.setCantidadDEC(cantidad)
		elif type(cantidad) is int:
			self.setCantidad2(cantidad)
			
		return self

	def setCantidad2(self, cantidad=1):
		cant1= cantidad / 1000
		cant2= cantidad % 1000
		if cant1>0:
			self.addData(((0xFF00 & cant1)>>8 ), 'B')
			self.addData((0xFF & cant1), 'B')
		self.addData(((0xFF00 & cant2)>>8), 'B')
		self.addData((0xFF & cant2))
		if cant1==0:
			self.addData(((0xFF00 & cant1)>>8 ), 'B')
			self.addData((0xFF & cant1), 'B')
		
		return self


	#def setCantidad(self, cantidad=1):
	#	cant1= cantidad / 1000
	#	cant2= cantidad % 1000
	#	self.addData(((0xFF00 & cant2)>>8), 'B')
	#	self.addData((0xFF & cant2))
	#	self.addData(((0xFF00 & cant1)>>8 ), 'B')
	#	self.addData((0xFF & cant1), 'B')
	#	return self
	

	def setValor(self, valor=1):
		self.addData(((0xFF000000 & valor)>>24), 'B')
		self.addData(((0xFF0000 & valor)>>16), 'B')
		self.addData((0xFF00 & valor)>>8, 'B')
		self.addData(0xFF & valor, 'B')
		return self
			

	def setDescripcion(self, descripcion=''.encode('utf8','replace')):
		datalist= list(self.data)
		datalist[1] += (len(descripcion))
		self.data = tuple(datalist)
		self.addData(len(descripcion), 'B')
		for letter in descripcion:
			self.addData(letter, 's')
		return self

class Donacion(Comando):
	"""Agrega una donacion a la Boleta fiscal"""
	def __init__(self):
		super(Donacion, self).__init__()
		self.codigoComando = 91
		self.addData((self.codigoComando, 5), '2B')

	def setValor(self, valor=1):
		self.addData(((0xFF000000 & valor)>>24), 'B')
		self.addData(((0xFF0000 & valor)>>16),'B')
		self.addData(((0xFF00 & valor)>>8),'B' )
		self.addData((0xFF & valor), 'B')
		return self

	def setDescripcion(self, descripcion="Devolucion"):
		datalist= list(self.data)
		datalist[1] += (len(descripcion))
		self.data = tuple(datalist)
		self.addData(len(descripcion), 'B')
		for letter in descripcion:
			self.addData(letter, 's')
		return self		

class ConfiguracionPago(Comando):
	"""Configura los tipos de pagos en la impresora Fiscal"""
	def __init__(self):
		super(ConfiguracionPago, self).__init__()
		self.codigoComando = 25
		self.addData((self.codigoComando, 2), '2B')

	def setValor(self, valor=1):
		self.addData((0xFF & valor), 'B')
		return self

	def setDescripcion(self, descripcion="Devolucion"):
		datalist= list(self.data)
		datalist[1] += (len(descripcion))
		self.data = tuple(datalist)
		self.addData(len(descripcion), 'B')
		for letter in descripcion:
			self.addData(letter, 's')
		return self		
