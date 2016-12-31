#!/usr/bin/env python3

from decimal import *
import re

#getcontext().prec = 100

def calc(value1, value2 = None, action = None):
	result = None
	if action is None and value2 is None:
		result = value1
	elif action=='*':
		result = value1 * value2
	elif action=='+':
		result = value1 + value2
	elif action=='**':
		result = value1 ** value2
	elif action=='//':
		# TODO: devision by zero
		result = value1 // value2
	elif action=='/':
		# TODO: devision by zero
		result = value1 / value2
	elif action=='%':
		# TODO: devision by zero
		result = value1 % value2
	elif action=='-':
		result = value1 - value2
	## debug
	#print('calc: {0} {1} {2} -> {3}'.format(value1, action, value2, result))
	## return
	if result is None:
		raise Exception('Wrong action')
	else:
		return result

def sub(S, pattern):
	searched, depth, exp = None, 0, [0, 0, 0]
	for s in pattern.finditer(S):
		# init search
		if searched is None:
			searched = s.group(0)
			exp[0] = s.end(0)
		# <- depth ->
		depth += 1 if searched==s.group(0) else -1
		if depth==0:
			exp[1] = s.start(0)
			exp[2] = s.end(0)
			break
	result = (S[exp[0]:exp[1]], S[exp[2]:])
	## debug
	#print('sub: {0} -> {1}'.format(S, result))
	## return
	return result

def cut(S, concatIt, cutIt = 0):
	result, depth = None, concatIt
	pattern = [
		##0 actions
		re.compile(r'^ ([\+]|[\*]) (.+) $', re.X), #[\*]{2}|[\/]{2}|[\-]|[\/]|[\%]|
		##1 number
		re.compile(r'^ ([\-\+]{0}) ([\d]+ (?:[\.][\d]*){0}) (.*) $', re.X),
		##2 group ()
		[ re.compile(r'^ [\(]', re.X), re.compile(r'[\(\)]', re.X) ],
		##3 group []
		[ re.compile(r'^ [\[]', re.X), re.compile(r'[\[\]]', re.X) ],
		##4 group {}
		[ re.compile(r'^ [\{]', re.X), re.compile(r'[\{\}]', re.X) ],
	]
	##0 actions
	if pattern[0].match(S) and cutIt>0:
		(action, expression) = pattern[0].split(S)[1:-1]
		(c, d) = ([], 0) if not(expression) else cut(expression, concatIt, cutIt + 1)
		result = [action] + c
		depth = max(depth, d)
	##1 number
	elif pattern[1].match(S):
		(sign, value, expression) = pattern[1].split(S)[1:-1]
		if sign and cutIt>0:
			raise Exception('Signed number')
		elif cutIt==0:
			value = sign + value
		value = Decimal(value)
		(c, d) = ([], 0) if not(expression) else cut(expression, concatIt, cutIt + 1)
		result = [value] + c
		depth = max(depth, d)
	##2 group ()
	elif pattern[2][0].match(S):
		(s, expression) = sub(S, pattern[2][1])
		(cc, dd) = concat(s, concatIt + 1)
		(c, d) = ([], 0) if not(expression) else cut(expression, concatIt, cutIt + 1)
		result = [cc] + c
		depth = max(depth, d, dd)
	##3 group []
	elif pattern[3][0].match(S):
		(s, expression) = sub(S, pattern[3][1])
		(cc, dd) = concat(s, concatIt + 1)
		(c, d) = ([], 0) if not(expression) else cut(expression, concatIt, cutIt + 1)
		result = [cc] + c
		depth = max(depth, d, dd)
	##4 group {}
	elif pattern[4][0].match(S):
		(s, expression) = sub(S, pattern[4][1])
		(cc, dd) = concat(s, concatIt + 1)
		(c, d) = ([], 0) if not(expression) else cut(expression, concatIt, cutIt + 1)
		result = [cc] + c
		depth = max(depth, d, dd)
	## debug
	#print('cut: {0} -> {1} {2}'.format(S, result, depth))
	## return
	if result is None:
		raise Exception('Wrong expression');
	else:
		return (result, depth)

def concat(S, concatIt = 0):
	(s, depth) = cut(S, concatIt)
	for A in [r'^(?:[\*]{2}|[\/]{2}|[\/]|[\%]|[\*])$', r'^(?:[\-]|[\+])$']:
		while True:
			a = [i for i in range(1, len(s), 2) if re.match(A, s[i])]
			if len(a)>0:
				a = a[0]
				ss = s[:a-1] + [calc(s[a-1], value2=s[a+1], action=s[a])] + s[a+2:]
				## debug
				#print('parse [{1}]: {2} -> {3}'.format(S, s[a], s, ss))
				s = ss
			else:
				break
	## return
	return (s[0], depth)

def parse(S):
	try:
		result = concat(S)
		#return result
		return (int(result[0]), result[1])
	except Exception:
		return 'Der Ausdruck ist nicht korrekt.'
		#raise Exception('Der Ausdruck ist nicht korrekt.')

if __name__=='__main__':
	a = '1324+(1234+234)'
	#a = '2+13/((1)+(1))*2%7**2-4' # [1324, +, 123, *, 2, +, 123] -> [1324, +, (123*2), +, 123]
	#a = '2+13/(1+1)*2-4'
	#a = '-2+13/2*2-4' 
	#a = '123+3*(2+[1*3])+(7)'
	a = '[{1}+5]*({2}+[{1*(3)}+2])'

	print(parse(a))
