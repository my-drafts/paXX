#!/usr/bin/env python

import math

def reelle_nullstellen(a, b, c):
	if a==0 and b==0 and c==0:
		return 'Das gegebene Polynom ist das Nullpolynom.'
	elif a==0 and b==0:
		return 'Das Polynom besitzt {0} verschiedene reelle Nullstellen. Davon sind {1} positiv, {2} negativ und {3} doppelt.'.format(0, 0, 0, 0)
	elif a==0 : 
		x=[-c/b]
		n=len(set(x))# Anzahl
		u=len([y for y in set(x) if y>0]) #positive
		v=len([y for y in set(x) if y<0]) #negative
		k=0  #dopelt
		return 'Das Polynom besitzt {0} verschiedene reelle Nullstellen. Davon sind {1} positiv, {2} negativ und {3} doppelt.'.format(n, u, v, k)
	else:
		d=b**2-4*a*c #Determinante
		if d<0:
			return 'Das Polynom besitzt {0} verschiedene reelle Nullstellen. Davon sind {1} positiv, {2} negativ und {3} doppelt.'.format(0, 0, 0, 0)
		else:
			x=[(-b-math.sqrt(d))/(2*a), (-b+math.sqrt(d))/(2*a)] 
			n=len(set(x))# Anzahl
			u=len([y for y in set(x) if y>0]) #positive
			v=len([y for y in set(x) if y<0]) #negative
			k=len([y for y in set(x) if x.count(y)>1]) #dopelt
			return 'Das Polynom besitzt {0} verschiedene reelle Nullstellen. Davon sind {1} positiv, {2} negativ und {3} doppelt.'.format(n, u, v, k)

