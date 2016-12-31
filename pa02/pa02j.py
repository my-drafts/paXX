#!usr/bin/env python

import re

def konvertiere(zahl, basis, basisNeu):
	ZIFFREN = [chr(i) for i in range(ord('0'),ord('9')+1) + range(ord('A'),ord('Z')+1) + range(ord('a'),ord('z')+1)]

	def zahl2code(zahl, basis):
		zahl = zahl[::-1]
		codes = [(i, ZIFFREN.index(zahl[i])) for i in range(len(zahl))]
		return reduce(lambda r, c: r + c[1]*(basis**c[0]), codes, 0)
		print(reduce(lambda r, c: r + c[1]*(basis**c[0]), codes, 0))
	def code2zahl(code, basis):
		zahl = []
		while code>0:
			zahl += [ZIFFREN[code%basis]]
			code /= basis
		return ''.join(zahl[::-1] if len(zahl)>0 else ZIFFREN[0])

	if not re.match('^['+''.join(ZIFFREN)+']+$', zahl):
		return ''
	elif not(basis>1 and basis<=len(ZIFFREN)) or not re.match('^['+''.join(ZIFFREN[:basis])+']+$', zahl):
		return ''
	elif not(basisNeu>1 and basisNeu<=len(ZIFFREN)):
		return ''
	elif basis==basisNeu:
		return zahl
	else: 
		code = zahl2code(zahl, basis)
		zahlNeu = code2zahl(code, basisNeu)
		return zahlNeu

print(konvertiere('2456754', 34, 10))



