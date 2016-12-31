#!/usr/bin/env python3

import math

def Sigma(N):
	range2 = int(math.ceil(float(N)/2))+1
	return sum([n for n in range(1, min(N, range2)) if N%n==0])

def Kanten(L):
	#return [(l, ll) for l in L for ll in L if l==Sigma(ll)]
	result = []
	for l in L:
		sl = Sigma(l)
		for ll in L:
			if not(sl==l) and (sl==ll):
				result += [(ll, l)]
	return result

def KantenNach(l, L=None, kanten=None):
	if not(kanten is None):
		return [k for k in kanten if k[0]==l]
	elif not(L is None):
		return [k for k in Kanten(L) if k[0]==l]
	else:
		return []

def Grad(l, L=None, kanten=None):
	return len(KantenNach(l, L=L, kanten=kanten))


def Perfekt(L=None):
	if not(L is None):
		return [l for  l in L if l==Sigma(l)]
	else:
		return []

def MaxInDeg(L):
	K = Kanten(L)
	G = [(l, Grad(l, kanten=K)) for l in L]
	maxG = max([g[1] for g in G] + [0])
	knoteMaxG = max([g[0] for g in G if g[1]==maxG] + [0])
	return (maxG, knoteMaxG, Perfekt(L))

if __name__=="__main__":
	#
	#print(Sigma(10000000))
	def ksort(a, b):
		if a[0]>=b[0]:
			return 1
		elif a[0]==b[0] and a[1]>=b[1]:
			return 1
		elif a[0]==b[0] and a[1]==b[1]:
			return 0
		else:
			return -1
	#
	#k = Kanten(range(1, 10000))
	#k.sort(ksort)
	#print(k)
	#print(len(k))
	#
	#print(Grad(1, range(1, 3000)))
	#
	#print(MaxInDeg([2,3,5,7,11,13]))
	#
	#print(MaxInDeg(list(range(2,20000))))
	#
	#print(MaxInDeg([6]))
	#
	#print(MaxInDeg([7]))
	#print(MaxInDeg([1 ,12496 ,14264 ,14536 ,15472 ,14288]))
	#
	#print(MaxInDeg([]))
