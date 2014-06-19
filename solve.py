#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
La cadena de  verdulerías “Don Rudy S. A.” últimamente incrementó su cantidad
de sucursales a 7 por lo cual necesitan establecer un depósito que sirva de
punto medio entre las mismas. Cada vez que la camioneta de la empresa
descargue la mercadería en una sucursal deberá volver a aprovisionarse al
depósito y así hasta reponer la mercadería de cada sucursal.
En total la camioneta hará 7 viajes diarios (ida y vuelta).

¿ En que intersección de la grilla deberían ubicar el depósito para
recorrer la menor distancia posible ?
"""

from time import time

tiempo_inicio = time()

sucursales = [(1,2),(3,5),(3,8),(5,7),(7,5),(9,1),(9,8)]
cantidad_sucursales = len(sucursales)
x_total = y_total = 0

for sucursal in sucursales:
	x_total = x_total + (sucursal[0] * 2)
	y_total = y_total + (sucursal[1] * 2)

print x_total / (cantidad_sucursales * 2);
print y_total / (cantidad_sucursales * 2);

print 'Se ejecutó en %f segundos' % (time() - tiempo_inicio)