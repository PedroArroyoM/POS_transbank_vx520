#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Herramientas para manejo de paquetes de datos para la impresora fiscal"""
import  binascii 
import struct

def crc32(data):
	""" ejemplo de data \x50\x04\x00\x00\x01\x00
	retorna el crc32 en hexadecimal
	"""
	crc32 = hex(binascii.crc32(data) & 0xffffffff)
	return crc32

def tupledecimal2hex(numbers):
	hexstrig = ""
	digit= 0
	for number in numbers:
		digit= hex(number)
		if len(digit[2:]) == 1:
			digit = "0" + digit[2:]	
		hexstrig = hexstrig + digit
	return hexstrig
	# def decimal2hex(self, numbers):
	# 	"""convierte un paquete de datos en numeros hexadecimales"""
	# 	hexastring= "0x"
	# 	for number in numbers:
	# 		if  len(hex(number)[2:]) > 1:
	# 			hexastring = hexastring + hex(number)[2:]
	# 		else:
	# 			hexastring = hexastring + "0" +hex(number)[2:]
	# 	print hexastring
	# 	return hexastring