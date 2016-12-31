#!/usr/bin/env python3

import re

class Matrix:
	def __init__(self, string=None, m=None, n=None, elements=None):
		if not(string is None):
			a = [int(i) for i in re.split(r'[\s\,]+', string)]
			n = len(string.split(','))
			m = len(a)/n
			pattern = '^[\s]*?{0}[\s]*?$'.format('[\s]*?,[\s]*?'.join(['[\s]+'.join(['[\d]+']*m)]*n))
			if not re.match(pattern, string):
				raise Exception('Error')
			else:
				self.elements = a
				self.n = n
				self.m = m
		elif not(m is None) and m>0 and not(n is None) and n>0:
			self.elements = [0]*n*m
			self.n = n
			self.m = m
			if not(elements is None):
				for i in len(elements):
					self.elements[i] = elements[i]

	def __str__(self):
		p = ', '.join([' '.join(['{0}{1}{2}'.format('{', i*self.m+j, '}') for j in range(0, self.m)]) for i in range(0, self.n)])
		return p.format(*self.elements)

	def __mul__(self, M):
		if self.m==M.n:
			result = Matrix(n=self.n, m=M.m)
			for i in range(self.n):
				for j in range(M.m):
					resultMin = None
					for k in range(self.m):
						x = self.elements[i*self.m + k] + M.elements[k*M.m + j]
						resultMin = x if resultMin is None else min(resultMin, x)
					result.elements[i*result.m + j] = resultMin
			return result

	def __pow__(self, x):
		result = Matrix(str(self))
		for i in range(1, x):
			result = result*self
		return result

def mul(A, B):
	a = Matrix(A)
	b = Matrix(B)
	return a*b

def pow(A, x):
	a = Matrix(A)
	return a**x
A = '4 3 , 1 7'
B = '2 5 9 , 8 6 1'
print mul(A,B)
print pow(A,0)
