#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 17-01-2016

@author: administrador
'''

import serial
from controller.commands import commands
from controller.response import respuesta
import logging
import platform
# from controller.comandos.AbrirBoleta import AbrirBoleta
from  controller.comandos.CommandFactory import Factory
import re
import time
from _socket import timeout

_logger = logging.getLogger('Fiscal Printer Driver')
hdlr = logging.FileHandler('fiscal_printer.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
_logger.addHandler(hdlr) 
_logger.setLevel(logging.DEBUG)

class Driver(object):
    '''
    Usado para interactuar con la impresora fiscal.
    '''
    _comando= commands()
    _decodificador = respuesta()    
    _cf = Factory()
    _secuencia = 0
    _puerto = []
    
    def __init__(self):
        '''
        Constructor
        '''
        self._comando= commands()
        self._decodificador = respuesta()    
        self._cf = Factory()
        self._secuencia = 0
        self._puerto = self.busca_puerto()
        self._puerto = [['/dev/ttyUSB0']]
        #self.zreport()

    def getsecuencia(self):

        self._secuencia += 1

        _logger.debug('secuencia: %s'%(self._secuencia))

        if not 0 <= self._secuencia <= 255:

            self._secuencia = 0

        

        return self._secuencia


    def imprimir(self, receipt):
        _logger.info('Inicio de impresion')
        _logger.debug('parametros enviados %s'%(receipt))
       

        _logger.debug('Total sin impuestos: %s' % (receipt['total_without_tax']))
        _logger.debug('Total impuestos: %s' % (receipt['total_tax']))
        _logger.debug('Total descuento: %s' % (receipt['total_discount']))
        _logger.debug('Total con impuesto: %s' % (receipt['total_with_tax']))
   
     
        #secuencia=0
        pagos=0
        totalimpreso=0
        pago_cheq_rest=0
        
        for line in receipt['orderlines']:
            totalimpreso+= int(round(line['price_with_tax']))
        
        for payment in receipt['paymentlines']:
            pago_cheq_rest += int(round(payment['amount'])) if payment['FpPayType'] == 'restaurant_voucher_pay' else 0
            pagos += int(round(payment['amount']))
        
        _logger.debug('Monto total impreso %s monto total pagado %s'%(totalimpreso,pagos)) 
        
        if pago_cheq_rest != 0:
            if pago_cheq_rest >= pagos:
                _logger.info('Boleta pagada con cheque restaurant')
                return "Boleta pagada con cheque restaurant"
            
        
        if totalimpreso>pagos:
            _logger.warning('El monto a pagar es menor a lo facturado')
            return "El monto a pagar es menor a lo facturado"
        
        try:
            
            #Buscar el puerto comm disponible
            #s = serial.Serial(2,9600)
            
            s = serial.Serial(self._puerto[0][0],9600) #if self.conexion_puerto(self._puerto[0][0]) else None
            
            _logger.info('Puerto serial abierto %s'%(self._puerto[0][0]))
            #self._secuencia += 1
            
            for r in self._comando.ballotNumber(int(self.getsecuencia())):
                #print(r)
                try:
                    s.write(chr(r))
                except:
                    s.write((r))
            #self._secuencia = self._secuencia + 1
    
    
            #ENCABEZADO
            s.write('\xA0' + chr(self.getsecuencia()) + '\x06\x51\xD7\x3E\xD5\x50\x04\x00\x00\x01\x00')
            _logger.debug('Encabezado enviado')
            time.sleep (0.8)
            #DETALLE
            totalimpreso = 0
            _logger.debug('cantidad de lineas del pedido: %s' % (len(receipt['orderlines'])))
            for line in receipt['orderlines']:

                _logger.debug('imprimiendo producto: %s' % (line['product_name']))
                _logger.debug('cantidad: %s' % (line['quantity']))
                _logger.debug('UOM: %s' % (line['unit_name']))
                _logger.debug('precio: %s' % (line['price']))
                _logger.debug('precio sin impuesto: %s' % (line['price_without_tax']))
                _logger.debug('precio con impuesto: %s' % (line['price_with_tax']))
                
                quantity = line['quantity']
                
                uom = line['unit_name']
                
                product_name = line['product_name']
                product_name =  product_name.encode('utf8','ignore')
                #product_name = product_name.decode('utf8','replace')
                price = int(line['price'])                
                
                price_without_tax = round(line['price_without_tax'])
                
                price_with_tax=round(line['price_with_tax'])
                #if price_with_tax==0:
                #    _logger.debug('Producto con valor a pagar en 0')
                #    continue              
                _logger.info('linea detalle %s %s %s'%(product_name, quantity, price))
                
                totalimpreso += price
                #self._secuencia += 1

                if price_with_tax>0:
                    for r in self._cf.agregarProducto().setCantidad(quantity).setValor(price).setDescripcion(product_name).setSequence(self.getsecuencia()).createPackage().getPackage():
                        #print(r)
                        try:
                            s.write(chr(r))
                        except:
                            s.write((r))
                    time.sleep (0.3)
                else:
                    _logger.debug('Producto con valor a pagar en 0')
            
            
            
            

            #    for r in self._cf.agregarProducto().setCantidad('1').setValor(str(valor)).setDescripcion('item desajuste').setSequence(self._secuencia).createPackage().getPackage():
                    #print(r)
            #        try:
            #            s.write(chr(r))
            #        except:
            #            s.write((r))
            #    time.sleep (0.5)
            
            print 'Totales de la boleta'
            total_without_tax = round(receipt['total_without_tax'])
            print 'Total sin impuesto: ',total_without_tax
            total_tax = round(receipt['total_tax'])
            print 'Total con impuesto: ', total_tax
            total_discount=0
            try:
                total_discount = round(receipt['total_discount'])
            except Exception:
                total_discount = 0 #receipt['discount']
            print 'Total descuento: ',total_discount
            total_with_tax = round(receipt['total_with_tax'])
            print 'Total con impuesto: ', total_with_tax
            
    
            #SUBTOTAL
            #self._secuencia += 1
            s.write('\xA0' + chr(self.getsecuencia()) + '\x03\x89\x62\x12\x8D\x52\x01\x00')
            time.sleep (0.5)
    
            #PAGOS
            _logger.info('Pagos ingresados.')
            
  
            cheq_rest_pago = []
            otros_pago = []
            if receipt['paymentlines']:
                for payment in receipt['paymentlines']:
                    if payment['FpPayType'] == 'restaurant_voucher_pay':
                        cheq_rest_pago += [payment] 
                    else:
                        otros_pago +=[payment]
                        
                for payment in cheq_rest_pago:
                    amount=int(payment['amount'])
                    
                    _logger.info('pago a imprimir: %s tipo de pago: %s'%(amount, "cheque restaurant"))
                    
                    for r in self._cf.descuento().setValor(amount).setDescripcion("Pago con cheque restaurant").setSequence(self.getsecuencia()).createPackage().getPackage():
                            #print(r)
                            try:
                                s.write(chr(r))
                            except:
                                s.write((r))
                
                for payment in otros_pago:
                            
                    _logger.debug('Diario de pago: %s' % (payment['journal']))
                    _logger.debug('Monto: %s' % (payment['amount']))
                    
                    journal = ''
                    journal = payment['journal']
                    
                    FpPayType = payment['FpPayType']
                    tipopago = 1
                    if FpPayType == 'cash_pay':
                        tipopago = 0
                        _logger.info( 'tipo de pago efectivo')
                    elif FpPayType == 'voucher_pay':
                        tipopago = 1
                        _logger.info('tipo de pago cheque')
                    elif FpPayType == 'debit_card' or FpPayType == 'credit_card':
                        tipopago = 2
                        _logger.info('tipo de pago tarjeta')
                    else:
                        tipopago = 0
                        _logger.info('tipo de pago no identificado')
                    
                    amount=int(payment['amount'])
                    #self._secuencia += 1
                    
                    _logger.info('pago a imprimir: %s tipo de pago: %s'%(amount, tipopago))
                    
                    for r in self._cf.pago().setTipoPago(tipopago).setValor(amount).setSequence(self.getsecuencia()).createPackage().getPackage():
                        #print(r)
                        try:
                            s.write(chr(r))
                        except:
                            s.write((r))
                    #self._secuencia += 1
                    time.sleep (0.3)
                    
            #CIERRE BOLETA
            #self._secuencia += 1
            for r in self._cf.cierreBoleta().setSequence(self.getsecuencia()).createPackage().getPackage():
                    #print(r)
                    try:
                        s.write(chr(r))
                    except:
                        s.write((r))
            time.sleep (0.5)
            
            s.close()
            
            _logger.info('Cierre enviado')
    
    
            
            
        except serial.SerialException as e:
            _logger.error('Ocurrio un error ', str(e))
        except TypeError as e:
            
            s.close()
            return None

        print 'enviado return'
        return

    def busca_puerto(self):
        _logger.debug('Buscando puerto impresora fiscal...')
                
        import serial.tools.list_ports;
        if platform.system()=='Windows':
            res = [['\\.\COM4']]
        elif platform.system()=='Linux':
            res = [port for port in serial.tools.list_ports.comports() if port[2] != 'n/a']
        
        _logger.debug('Sistema: %s, puerto encontrado: %s' % (platform.system(),res))
        return res
        
    def comprueba_puerto(self):
        _logger.debug('Comprobando si el puerto esta abierto...')
        
        try:
            if len(self._puerto)==0:
                self._puerto = self.busca_puerto()
                
            ser = serial.Serial(self._puerto[0][0], 9600)
            ser.close()
            _logger.debug('Puerto abierto.')
            return True
        
        except:
            return False

    def abrir_cajon(self):
        _logger.debug('Abriendo gaveta...')

        #self._secuencia += 1
        #s.write('\xA0' + chr(secuencia))
        #arr = {27,110,0,25,250}
        s = serial.Serial(self._puerto[0][0],9600)
        s.write('\xA0' + chr(self.getsecuencia()) + '\x02\x0A\x8A\xAE\x0D\x74\x00')
        
        print('Puerto serial abierto')
        #self._secuencia += 1
        
        for r in self._comando.openbox(int(self._secuencia)):
            #print(r)
            try:
                s.write(chr(r))
            except:
                s.write((r))
        #secuencia = secuencia + 1
        
        time.sleep (0.5)
        _logger.debug('Apertura de gaveta enviada')
        
        s.close()
            
    
    def conecta_puerto(self, portname):

        try:
            return serial.Serial(portname, 9600)
        except:
            return False
        
    def ping(self):
        s = serial.Serial(self._puerto[0][0],9600)
        
        #self._secuencia += 1
        #pool = self._comando.ping(int(self._secuencia))
        pool = '\xA0' + chr(self.getsecuencia()) + '\x02\x0A\x8A\xAE\x0D\x74\x7E'
        for r in pool:
            print(hex(ord(r)))
            try:
                s.write(chr(r))
            except:
                s.write(r)
                
        #print s.readline(timeout=1)
        print self.doRead(s,term='\n')
        s.close()
        
    def obtenerestadosecundario(self):
        s = self.conecta_puerto(self._puerto[0][0])
        self._secuencia +=1
        for r in self._comando.bell(int(self._secuencia)):
                try:
                    s.write(chr(r))
                except:
                    s.write((r))
                    
        print s.readline(timeout=1)
        s.close()
        
    def doRead(self, ser, term):
        matcher = re.compile(term)    #gives you the ability to search for anything
        buff    = ""
        tic     = time.clock()
        buff   += ser.read(128)
        tout = 99
        # you can use if not ('\n' in buff) too if you don't like re
        while ((time.clock - tic) < tout) and (not matcher.search(buff)):
            buff += ser.read(128)
    
        return buff
    
    def zreport(self):
        _logger.info('Emitiendo z fiscal')
        try:
            s = serial.Serial(self._puerto[0][0],9600)
            _logger.debug('Puerto abierto ' + self._puerto[0][0])
            for r in self._cf.reporteZ().setSequence(int(self.getsecuencia())).createPackage().getPackage():
                try:
                    s.write(chr(r))
                except:
                    s.write((r))
            #respuesta=(s.read(126)).encode('hex')
            #print decodificador.decifraRespuesta(respuesta)
            print 'zreport enviado'
            s.close()
            #self._secuencia += 1
        except serial.SerialException as e:
            _logger.error('Ocurrio un error ', str(e))
        except TypeError as e:
            self._secuencia +=1
            s.close()
            return None            
            
    def xreport(self):
        _logger.info('Emitiendo x fiscal')
        #print('Procesing /pos/print_receipt GET method')
        try:
        
            s = serial.Serial(self._puerto[0][0],9600)
            _logger.debug('Puerto abierto ' + self._puerto[0][0])
            for r in self._cf.reporteX().setSequence(self.getsecuencia()).createPackage().getPackage():
                try:
                        s.write(chr(r))
                except:
                        s.write((r))
            #respuesta=(s.read(126)).encode('hex')
            #print decodificador.decifraRespuesta(respuesta)
            s.close()
            self._secuencia +=1
        except serial.SerialException as e:
            _logger.error('Ocurrio un error ', str(e))
        except TypeError as e:
            self._secuencia +=1
            s.close()
            return None
            
        return
