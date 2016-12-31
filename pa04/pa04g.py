#!/usr/bin/env python3

from bigfloat import *

PRECISION = 100000000

def golden_ratio(precision):
	if precision is None or precision<1:
		return 'Error precision'
	p, l = 1/BigFloat(precision, precision=PRECISION), 0
	F = [1, 0]
	while True:
		F = [F[0] + F[1]] + F[:2]
		if not(0 in F) and l%2==1:
			d = [BigFloat(f, precision=PRECISION) for f in F]
			dd = [d[i]/d[i+1] for i in range(len(d)-1)]
			ll = [dd[i]-dd[i+1] for i in range(len(dd)-1)] # if dd[i]>=dd[i+1]
			print(l, ll)
			if ll[0]<p:
				break
		l+=1

	return [(l+1)/2, (F[1], F[2]), (F[0], F[1])]
print(golden_ratio(10**30))
