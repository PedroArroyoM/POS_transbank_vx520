# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)]
# From type library 'ocxsam350.ocx'
# On Fri Jul 17 18:55:03 2015
'ocxsam350 ActiveX Control module'
makepy_version = '0.5.01'
python_version = 0x20700f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{531C1877-C9DA-4778-97E9-91EA75A2F898}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 10
LCID = 0x0

from win32com.client import DispatchBaseClass
class _DOcxsam350(DispatchBaseClass):
	'Dispatch interface for Ocxsam350 Control'
	CLSID = IID('{8487AC2C-A0C7-4C32-A7C2-DB4BAB2B5A9D}')
	coclass_clsid = IID('{EAE378B4-31CC-4680-9AC2-93CC7A2451E0}')

	def AboutBox(self):
		return self._oleobj_.InvokeTypes(-552, LCID, 1, (24, 0), (),)

	def abrirboleta(self, logo=defaultNamedNotOptArg, impencabezado=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((2, 0), (2, 0)),logo
			, impencabezado)

	def abrircajon(self):
		return self._oleobj_.InvokeTypes(44, LCID, 1, (3, 0), (),)

	def abrirnofiscal(self, logo=defaultNamedNotOptArg, impencabezados=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (3, 0), ((2, 0), (2, 0)),logo
			, impencabezados)

	def agregadescuento(self, descripcion=defaultNamedNotOptArg, valor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), ((8, 0), (3, 0)),descripcion
			, valor)

	def agregadevolucion(self, descripcion=defaultNamedNotOptArg, valor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), ((8, 0), (3, 0)),descripcion
			, valor)

	def agregadonacion(self, descripcion=defaultNamedNotOptArg, valor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((8, 0), (3, 0)),descripcion
			, valor)

	def agregaitem(self, descripcion=defaultNamedNotOptArg, cantidad=defaultNamedNotOptArg, valorunit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((8, 0), (4, 0), (3, 0)),descripcion
			, cantidad, valorunit)

	def agregaitemdec(self, descripcion=defaultNamedNotOptArg, cantentera=defaultNamedNotOptArg, cantdecimal=defaultNamedNotOptArg, valorunit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(45, LCID, 1, (3, 0), ((8, 0), (3, 0), (3, 0), (3, 0)),descripcion
			, cantentera, cantdecimal, valorunit)

	def agregapago(self, tipo=defaultNamedNotOptArg, valor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((2, 0), (3, 0)),tipo
			, valor)

	def agregarecargo(self, descripcion=defaultNamedNotOptArg, valor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((8, 0), (3, 0)),descripcion
			, valor)

	def cargarlogo(self, archivo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (3, 0), ((8, 0),),archivo
			)

	def cierraboleta(self, impcola=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((2, 0),),impcola
			)

	def cierranofiscal(self, impcola=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(30, LCID, 1, (3, 0), ((2, 0),),impcola
			)

	def cierrejornada(self):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (3, 0), (),)

	def conflineacola(self, numero=defaultNamedNotOptArg, texto=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), ((2, 0), (8, 0)),numero
			, texto)

	def conflineaencabezado(self, numero=defaultNamedNotOptArg, texto=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (3, 0), ((2, 0), (8, 0)),numero
			, texto)

	def conftipopago(self, numero=defaultNamedNotOptArg, descripcion=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (3, 0), ((2, 0), (8, 0)),numero
			, descripcion)

	def fini(self):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), (),)

	def firmadoatexto(self, archfirmado=defaultNamedNotOptArg, archtexto=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(41, LCID, 1, (3, 0), ((8, 0), (8, 0)),archfirmado
			, archtexto)

	def firmaultimoinforme(self):
		return self._oleobj_.InvokeTypes(38, LCID, 1, (3, 0), (),)

	def informeTransfecha(self, inicial=defaultNamedNotOptArg, final=defaultNamedNotOptArg, imprime=defaultNamedNotOptArg, archivo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(34, LCID, 1, (3, 0), ((8, 0), (8, 0), (2, 0), (8, 0)),inicial
			, final, imprime, archivo)

	def informeTransno(self, inicial=defaultNamedNotOptArg, final=defaultNamedNotOptArg, imprime=defaultNamedNotOptArg, archivo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(36, LCID, 1, (3, 0), ((3, 0), (3, 0), (2, 0), (8, 0)),inicial
			, final, imprime, archivo)

	def informeTransnoZ(self, zin=defaultNamedNotOptArg, zfin=defaultNamedNotOptArg, imprime=defaultNamedNotOptArg, archivo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(58, LCID, 1, (3, 0), ((3, 0), (3, 0), (2, 0), (8, 0)),zin
			, zfin, imprime, archivo)

	def informeX(self):
		return self._oleobj_.InvokeTypes(43, LCID, 1, (3, 0), (),)

	def informeZfecha(self, inicial=defaultNamedNotOptArg, final=defaultNamedNotOptArg, imprime=defaultNamedNotOptArg, archivo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(37, LCID, 1, (3, 0), ((8, 0), (8, 0), (2, 0), (8, 0)),inicial
			, final, imprime, archivo)

	def informeZno(self, inicial=defaultNamedNotOptArg, final=defaultNamedNotOptArg, imprime=defaultNamedNotOptArg, archivo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(35, LCID, 1, (3, 0), ((3, 0), (3, 0), (2, 0), (8, 0)),inicial
			, final, imprime, archivo)

	def init(self, com=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((2, 0),),com
			)

	def lineanofiscal(self, texto=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(29, LCID, 1, (3, 0), ((8, 0),),texto
			)

	def nofirmadoatexto(self, archfirmado=defaultNamedNotOptArg, archtexto=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(42, LCID, 1, (3, 0), ((8, 0), (8, 0)),archfirmado
			, archtexto)

	def obtenerSerial(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(46, LCID, 1, (8, 0), (),)

	def obtenerdatosfiscal(self):
		return self._oleobj_.InvokeTypes(53, LCID, 1, (3, 0), (),)

	def obtenerdescuento(self):
		return self._oleobj_.InvokeTypes(50, LCID, 1, (3, 0), (),)

	def obtenerestado(self):
		return self._oleobj_.InvokeTypes(31, LCID, 1, (3, 0), (),)

	def obtenerfecha(self):
		return self._oleobj_.InvokeTypes(56, LCID, 1, (3, 0), (),)

	def obtenerhora(self):
		return self._oleobj_.InvokeTypes(47, LCID, 1, (3, 0), (),)

	def obtenerlineacola(self, numero=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(52, LCID, 1, (3, 0), ((2, 0),),numero
			)

	def obtenerlineaenc(self, numero=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(51, LCID, 1, (3, 0), ((2, 0),),numero
			)

	def obtenernumboleta(self):
		return self._oleobj_.InvokeTypes(32, LCID, 1, (3, 0), (),)

	def obtenernumz(self):
		return self._oleobj_.InvokeTypes(33, LCID, 1, (3, 0), (),)

	def obtenerresto(self):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), (),)

	def obtenertextopago(self, numpago=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(54, LCID, 1, (3, 0), ((2, 0),),numpago
			)

	def requiercierre(self):
		return self._oleobj_.InvokeTypes(55, LCID, 1, (2, 0), (),)

	def sethora(self, segundos=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(48, LCID, 1, (3, 0), ((3, 0),),segundos
			)

	def statuscajon(self):
		return self._oleobj_.InvokeTypes(57, LCID, 1, (3, 0), (),)

	def subtotal(self):
		return self._oleobj_.InvokeTypes(49, LCID, 1, (3, 0), (),)

	def verificaarchivofirmado(self, archivofirmado=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(39, LCID, 1, (3, 0), ((8, 0),),archivofirmado
			)

	def verificaarchivofirmadoclaves(self, archivo=defaultNamedNotOptArg, publica=defaultNamedNotOptArg, modulo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(40, LCID, 1, (3, 0), ((8, 0), (8, 0), (8, 0)),archivo
			, publica, modulo)

	_prop_map_get_ = {
		"Z": (3, 2, (3, 0), (), "Z", None),
		"boleta": (2, 2, (3, 0), (), "boleta", None),
		"bufferlinea": (6, 2, (8, 0), (), "bufferlinea", None),
		"caja": (9, 2, (3, 0), (), "caja", None),
		"descuento": (7, 2, (3, 0), (), "descuento", None),
		"estado": (4, 2, (3, 0), (), "estado", None),
		"estadoimpresion": (10, 2, (3, 0), (), "estadoimpresion", None),
		"fecha": (11, 2, (3, 0), (), "fecha", None),
		"hora": (5, 2, (3, 0), (), "hora", None),
		"restoboleta": (1, 2, (3, 0), (), "restoboleta", None),
		"valsubtotal": (8, 2, (3, 0), (), "valsubtotal", None),
	}
	_prop_map_put_ = {
		"Z" : ((3, LCID, 4, 0),()),
		"boleta" : ((2, LCID, 4, 0),()),
		"bufferlinea" : ((6, LCID, 4, 0),()),
		"caja" : ((9, LCID, 4, 0),()),
		"descuento" : ((7, LCID, 4, 0),()),
		"estado" : ((4, LCID, 4, 0),()),
		"estadoimpresion" : ((10, LCID, 4, 0),()),
		"fecha" : ((11, LCID, 4, 0),()),
		"hora" : ((5, LCID, 4, 0),()),
		"restoboleta" : ((1, LCID, 4, 0),()),
		"valsubtotal" : ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _DOcxsam350Events:
	'Event interface for Ocxsam350 Control'
	CLSID = CLSID_Sink = IID('{2B0FE9EF-9088-4915-8484-BA72ABCBB94B}')
	coclass_clsid = IID('{EAE378B4-31CC-4680-9AC2-93CC7A2451E0}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'OCXSAM350.Ocxsam350Ctrl.1'
class Ocxsam350(CoClassBaseClass): # A CoClass
	# Ocxsam350 Control
	CLSID = IID('{EAE378B4-31CC-4680-9AC2-93CC7A2451E0}')
	coclass_sources = [
		_DOcxsam350Events,
	]
	default_source = _DOcxsam350Events
	coclass_interfaces = [
		_DOcxsam350,
	]
	default_interface = _DOcxsam350

RecordMap = {
}

CLSIDToClassMap = {
	'{EAE378B4-31CC-4680-9AC2-93CC7A2451E0}' : Ocxsam350,
	'{8487AC2C-A0C7-4C32-A7C2-DB4BAB2B5A9D}' : _DOcxsam350,
	'{2B0FE9EF-9088-4915-8484-BA72ABCBB94B}' : _DOcxsam350Events,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
}


NamesToIIDMap = {
	'_DOcxsam350Events' : '{2B0FE9EF-9088-4915-8484-BA72ABCBB94B}',
	'_DOcxsam350' : '{8487AC2C-A0C7-4C32-A7C2-DB4BAB2B5A9D}',
}


