import math

str1 = "ало, привет, как дела"

a = "".join(x.upper() for x in str1.split(",")) # Генерирует результаты
print(type(a))
print(a)

line = "1,2,3,4,5"

b = "".join(map((lambda x: x * 2), line.split(","))) # Генерирует результаты
print(type(b))
print(b)

###

aa = [x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]] # Вложенное включение
print(aa)

bb = list(map(lambda x: x * 2, map(abs, (-1 , -2, 3, 4)))) # Вложенное отображение
print(bb)

cc = list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4)))
print(cc)

dd = list(map(math.sqrt, (x ** 2 for x in range(4)))) # Вложенные комбинации
print(dd)

###
stringg = "aa bb c dd j"
aaa = "".join(x for x in stringg.split() if len(x) > 1)
print(aaa)

bbb = "".join(filter(lambda x: len(x) > 1, stringg.split()))
print(bbb)

ccc = "".join(x.upper() for x in stringg.split() if len(x) > 1)
print(ccc)

ddd = "".join(map(str.upper, filter(lambda x: len(x) > 1, stringg.split()))) # Нужно фиксануть)
print(ddd)

###

n = "".join(x.upper() for x in stringg.split() if len(x) > 1) # Эквивалент
print(n)

res = "" # Эквивалент
for x in stringg.split():
	if len(x) > 1:
		res += x.upper()
print(res)

###

gg = (x * 4 for x in "spam")
print(list(gg))

def fourchar(line):
	for char in line:
		yield char * 4

ggg = fourchar("spam")
print(list(ggg))

gggg = (x * 4 for x in "spam")

I = iter(gggg)
print(next(I))
print(next(I))
print(next(I))
print(next(I))

###
chars = "ssss f gg y rrr"
l = "".join((x.upper() for x in chars.split() if len(x) > 2)) # Эквивалент
print(l)


def l_func(line): # Эквивалент
	for char in line.split():
		if len(char) > 2:
			yield char.upper()
lll = "".join(l_func(chars))
print(lll)

###

GG = (x ** 2 for x in range(10)) # Итератором генератора является сам генератор. GG cодержит метод __next__

a = iter(GG) is GG
print(a)

# Но можно создать ручуню итерацию
t1 = iter(GG)
print(next(t1))
print(next(t1))
t2 = iter(GG) # Второй итератор находится в той же самой позиции!
print(next(t2))
print(next(t2))
print(next(t2))
print(list(t1)) # Собираем все оставшиеся элементы

t3 = iter(x ** 2 for x in range(10)) # Новый генератор, чтобы начать заново
print(list(t3))

###
# Но есть объекты, которые поддерживают множество итераций
# Например списки

L = [1, 2 , 3, 4]
def funcc(list):
	for i in L:
		yield i
mmg = funcc(L)
print(list(mmg))
h1, h2 = iter(funcc(L)), iter(funcc(L))
print(next(h1))
print(next(h1))
print(next(h2))
print(next(h2))

###

# Расширение from yield
# from генератор

def booth(NN):
	for i in range(NN):
		yield i

print(list(booth(5)))

def boooth(NNN):
	yield from range(NNN)
print(list(boooth(5)))

def footh(h):
	for i in (x ** 2 for x in range(h)):
		yield i
print(list(footh(5)))

def foooth(h):
	yield from (x ** 2 for x in range(h)) # Вернуть x из генератора значение
print(list(foooth(5)))













