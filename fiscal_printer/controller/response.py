#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Codigos de respuesta de la impresora"""

class respuesta():

	def decifraRespuesta(self, respuesta="default"):
		response= {}
		#lenresponse= len(respuesta)
		"""a00109f9ee0178a80001000400000018"""
		if(respuesta[0:2] == 'a0'):
			response['ACK'] = True
			#Contador de comando enviado
			response['corelativo']= respuesta[2:4]
			response['tamanio_data'] = respuesta[4:6]
			response['CRC1']= respuesta[6:8] 
			response['CRC2']= respuesta[8:10]
			response['CRC3']= respuesta[10:12]
			response['CRC4']= respuesta[12:14]
			response['data'] = self.responseData(respuesta[14:])
		else:
			response['ACK']= False
		return response

	def responseData(self, package):
		data={}
		#lendata= len(data)
		data['encabezado']= package[0:2]
		if(package[2:4] == '00'):
			data['status_impresion']= 'Exito'
		else:
			data['status_impresion']= 'Fracaso'
		data['estado_primario'] = self.getEstado(package[4:6])
		data['codigo_respuesta']= self.getCodigoRespuesta(package[6:8])
		data['longitud_respuesta_extendida'] = package[8:10]
		data['respuesta_extendida'] = package[10:]
		return data



	def getEstado(self, codigoEstado):
		nombreEstado= "Estado Sin Asignar"
		if(codigoEstado== '01'):
			nombreEstado= "Jornada Fiscal No Iniciada"			
		elif(codigoEstado=='02'):
			nombreEstado= "Jornada Fiscal Iniciada"
		elif(codigoEstado=='03'):
			nombreEstado= "Documento No Fiscal Abierto"
		elif(codigoEstado=='04'):
			nombreEstado= "Documento No Fiscal de Pago Abierto"
		elif(codigoEstado=='05'):
			nombreEstado= "Boleta Fiscal Abierta"
		elif(codigoEstado=='06'):
			nombreEstado= "Boleta Fiscal Pago"
		elif(codigoEstado=='07'):
			nombreEstado= "Memoria Llena"
		elif(codigoEstado=='08'):
			nombreEstado= "Informe Z por rango"
		elif(codigoEstado=='09'):
			nombreEstado= "Informe Transacciones por rango"
		elif(codigoEstado=='0a'):
			nombreEstado= "Infore Z por Fecha"
		elif(codigoEstado=='0b'):
			nombreEstado= "Informe Transacciones por rango"
		return nombreEstado

	def getCodigoRespuesta(self, codigo):
		#respuesta=""
		codigos={
		"00" : "RESP_EXITO",
		"01" : "RESP_ERROR_INTERNO",  
		"02" : "RESP_ERROR_DE_INICIALIZACION",  
		"03" : "RESP_ERROR_DE_PROCESO", 
		"04" : "RESP_INVALIDO_PARA_ESTADO", 
		"05" : "RESP_INVALIDO_PARA_DOCUMENTO", 
		"06" : "RESP_COMANDO_INVALIDO", 
		"07" : "RESP_COMANDO_INCOMPLETO",  
		"08" : "RESP_LARGO_COMANDO_INVALIDO",   
		"09" : "RESP_RT_INVALIDO",  
		"0A" : "RESP_CODIGO_BARRA_INVALIDO",  
		"0B" : "RESP_CODIGO_BARRA_NO_PERMITIDO",  
		"0C" : "RESP_ERROR_DE_HARDWARE",  
		"0D" : "RESP_IMPRESORA_OFFLINE",  
		"0E" : "RESP_ERROR_DE_IMPRESION", 
		"0F" : "RESP_NO_HAY_PAPEL", 
		"10" : "RESP_POCO_PAPEL", 
		"11" : "RESP_COMANDO_NO_SOPORTADO", 
		"12" : "RESP_FH_NO_CONFIGURADA", 
		"13" : "RESP_ERROR_AL_CAMBIAR_FECHA", 
		"14" : "RESP_FECHA_FUERA_DE_RANGO", 
		"15" : "RESP_NUMERO_CAJA_INVALIDO", 
		"16" : "RESP_RUT_INVALIDO", 
		"17" : "RESP_NUMERO_LINEA_HC_INVALIDO", 
		"18" : "RESP_DEMASIADAS_FISCALIZACIONES", 
		"19" : "RESP_DEMASIADOS_TIPOS_DE_PAGOS" ,
		"1A" : "RESP_TIPO_DE_PAGO_YA_DEFINIDO", 
		"1B" : "RESP_NUMERO_PAGO_INVALIDO", 
		"1C" : "RESP_DESCRIPCION_PAGO_INVALIDA ", 
		"1D" : "RESP_MAXIMO_PORC_DESC_INVALIDO", 
		"1E" : "RESP_CLAVES_INVALIDA", 
		"1F" : "RESP_CLAVES_NO_CONFIGURADAS", 
		"20" : "RESP_INVALIDO_FUERA_FISCAL", 
		"21" : "RESP_INVALIDO_EN_FISCAL", 
		"22" : "RESP_MEM_FISCAL_LLENA" ,
		"23" : "RESP_24H_REQ_CIERRE_Z" ,
		"24" : "RESP_PAGOS_NO_DEFINIDOS " ,
		"25" : "RESP_DEMASIADOS_PAGOS_EN_JFISCAL", 
		"26" : "RESP_PERIODO_SIN_DATOS", 
		"27" : "RESP_DEMASIADAS_DONACIONES", 
		"28" : "RESP_DONACION_NO_ENCONTRADA" ,
		"29" : "RESP_TIPO_PAGO_NO_DEFINIDO",
		"2A" : "RESP_TOTAL_DEBE_SER_MAYOR_CERO" ,
		"2B" : "RESP_PAGO_NO_ENCONTRADO", 
		"2C" : "RESP_ITEM_NO_ENCONTRADO", 
		"2D" : "RESP_DEMASIADOS_PAGOS" ,
		"2E" : "RESP_DEMASIADOS_DESC_RECARG", 
		"2F" : "RESP_DEMASIADAS_TASAS_IMP", 
		"30" : "RESP_DEMASIADOS_ITEMS" ,
		"31" : "RESP_OVERFLOW", 
		"32" : "RESP_UNDERFLOW" ,
		"33" : "RESP_NO_PERMIT_DESP_DESC_REC" ,
		"34" : "RESP_NO_PERMIT_DESP_FASE_PAGO", 
		"35" : "RESP_TIPO_ITEM_INVALIDO", 
		"36" : "RESP_DESCRIP_EN_BLANCO", 
		"37" : "RESP_CANTIDAD_RESUL_MENOR_CERO", 
		"38" : "RESP_CANTIDAD_RESUL_MAYOR_MAX" ,
		"39" : "RESP_PRECIO_MAYOR_MAX", 
		"3A" : "RESP_NO_PERMITIDO_ANTES_PAGO", 
		"3B" : "RESP_FASE_PAGO_NO_FINALIZADA", 
		"3C" : "RESP_FASE_PAGO_FINALIZADA", 
		"3D" : "RESP_MONTO_PAGO_NO_PERMITIDO" ,
		"3E" : "RESP_MONTO_DESC_NO_PERMITIDO", 
		"3F" : "RESP_MONTO_DONA_NO_PERMITIDO", 
		"40" : "RESP_VUELTO_NO_MAYOR_CERO" ,
		"41" : "RESP_NO_PERMITIDO_ANTES_ITEM" ,
		"42" : "RESP_NF_MAX_LINES" ,
		"43" : "RESP_LOGO_COMPLETO" ,
		"44" : "RESP_LOGO_NO_COMPLETO" ,
		"45" : "RESP_FIN_INFORME", 
		"FF" : "RESP_ERROR_DESCONOCIDO" }


		return codigos[codigo.upper()]
