# problem 1
def remove(x):
	if x.endswith('!'):
		return x[:-1]

print(remove('Hi!'))
print(remove('Hi!!'))
print(remove('Hi!Hi!'))

def remove2(x):
	if x[-1] == '!':
		return x[:-1]

print(remove2('Hi!'))
print(remove2('Hi!!'))
print(remove2('Hi!Hi!'))

# problem 2
def array_diff(x, y):
	return [i for i in x if i not in y]
def array_diff1(x, y):
	arr = []
	for i in x:
		if i in y:
			pass
		else:
			arr.append(i)
	return arr

print(array_diff([1, 2], [2]))
print(array_diff([1, 2, 2, 2, 3], [2]))

print(array_diff1([1, 2], [2]))
print(array_diff1([1, 2, 2, 2, 3], [2]))

# problem 3
def find_longest(string):
    return max(len(x) for x in string.split())

def find_longest1(string):
	spl = string.split(" ")
	spl_len = len(spl)
	longest = 0
	for i in range(spl_len):
		if len(spl[i]) > longest:
			longest = len(spl[i])
	return longest

print(find_longest("The quick white fox jumped around the massive dog"))

print(find_longest1("The quick white fox jumped around the massive dog"))

# problem 4
def array(x):
	len_x = x.split(',')
	middle = 0
	if len(len_x) > 2:
		middle = x[2:-2]
	else:
		middle = None
	return middle

print(array(''))
print(array('1'))
print(array('1,3'))
print(array('1,2,3'))
print(array('1,2,3,4'))


# problem 5
stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5,
}

def fillable(a, b, c):
	if b in a and a[b] >= c:
		return True
	else:
		return False

def fillable1(a, b, c):
	return a.get(b, 0) >= c

print(fillable(stock, "football", 3))
print(fillable(stock, "leggos", 2))
print(fillable(stock, "action figure", 1))

print(fillable1(stock, "football", 3))
print (fillable1(stock, "leggos", 2))
print(fillable1(stock, "action figure", 1))

# problem 6
greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega'
)

def greek_comperator(a, b):
	if greek_alphabet.index(a) == greek_alphabet.index(b):
		return '==0'
	if greek_alphabet.index(a) > greek_alphabet.index(b):
		return '> 0'
	if greek_alphabet.index(a) < greek_alphabet.index(b):
		return '< 0'

greek_comperator1 = lambda a, b: greek_alphabet.index(a) - greek_alphabet.index(b)

print(greek_comperator('alpha', 'beta'))
print(greek_comperator('beta', 'alpha'))
print(greek_comperator('psi', 'psi'))

print(greek_comperator1('alpha', 'beta'))
print(greek_comperator1('beta', 'alpha'))
print(greek_comperator1('psi', 'psi'))
# problem 7
def IfChuckSaysSo():
	not True

def IfChuckSaysSo1():
	0

print(IfChuckSaysSo())
print(IfChuckSaysSo1())

# problem 8
def hex_to_dec(x):
	return int (x, 16)

print(hex_to_dec('1'))
print(hex_to_dec('a'))
print(hex_to_dec('10'))

# problem 9
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
	if dolphin:
		shark_speed = shark_speed / 2
	if pontoon_distance / you_speed > (pontoon_distance + shark_distance) / shark_speed:
		return 'Shark bait!'
	else:
		return 'Alive!'

print(shark(12, 50, 4, 8, True))
print(shark(7, 55, 4, 16, True))
print(shark(24, 0, 4, 8, True))

# problem 10
def shorten_to_date(x):
	arr = x.split(",")
	return arr[:-1]

print(shorten_to_date("Monday February 2, 8pm"))
print(shorten_to_date("Tuesday May 29, 8pm"))
print(shorten_to_date("Wed September 1, 3am"))
print(shorten_to_date("Friday May 2, 9am"))
print(shorten_to_date("Tuesday January 29, 10pm"))

# problem 11
def shortcut(s):
	VOWELS = ('a', 'e', 'i', 'o', 'u')
	return ''.join(x for x in s if x not in VOWELS)

print(shortcut('aeiou AEIOU is it working'))

def getRidOfVo(s):
	VOWELS = ('a', 'e', 'i', 'o', 'u')
	return ''.join(x for x in s if x.lower() not in VOWELS)
	
print(getRidOfVo('aeiou aeiou is it working'))

# problem 12
def returnArr(x, y):
	arr = []
	temp = 0
	if x < y:
		temp = x
		while temp <= y:
			arr.append(temp)
			temp += 1 
	elif x >= y:
		temp = y
		while temp <= x:
			arr.append(temp)
			temp += 1
	return arr

print(returnArr(1, 4))
print(returnArr(3, 9))

# problem 13
def shortlongshort(a, b):
	a_len = len(a)
	b_len = len(b)
	if a_len > b_len:
		return str(b + a + b)
	elif a_len < b_len:
		return str(a + b + a)

print(shortlongshort('1', '22'))
print(shortlongshort('22', '1'))