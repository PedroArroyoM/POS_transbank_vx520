#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Comando import *
class Factory(object):

	def abrirBoleta(self):
		return AbrirBoleta()

	def reporteZ(self):
		return ReporteZ()

	def reporteX(self):
		return ReporteX()
	def subTotal(self):
		return SubTotal()

	def cierreBoleta(self):
		return CierraBoleta()

	def pago(self):
		return Pago()

	def numeroBoleta(self):
		return NumeroBoleta()

	def descuento(self):
		return Descuento()

	def recargo(self):
		return Recargo()

	def devolucion(self):
		return Devolucion()

	def donacion(self):
		return Donacion()

	def agregarProducto(self):
		return AgregarProducto()	

	def avanzayCorta(self):
		return AvanzayCorta()
