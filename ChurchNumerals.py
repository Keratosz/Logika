#! /usr/bin/python
# -*- coding: utf-8 -*-

zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
five = lambda f: lambda x: f(f(f(f(f(x)))))

# Definicja nastepnika
succ = (lambda n: lambda f: lambda x: f(n(f)(x)))
# Dodawanie dwóch liczebników Churcha n i m.
add = (lambda m: lambda n: lambda f: lambda x: n(f)(m(f)(x)))
# Mnożenie liczb n i m.
mult = (lambda m: lambda n: lambda f: lambda x: n(m(f))(x))
# Podnoszenie liczby m do potęgi n-tej
exp = lambda m: lambda n: lambda f: lambda x:((n)(m)) (f) (x)

# Instrukcja zamiany liczebnika Churcha na integer, pozwala zobaczyc wyniki dzialan.
def church_na_int(LChurcha): return LChurcha(lambda x:x+1)(0)
# Zamiana integera na liczebnnik Churcha
def int_na_church(x): 
        if (x==0): 
            return zero
        else:
            return succ(int_na_church(x-1))
    
#Przykłady
print "Jedynka za 3.. 2... ", church_na_int(one),
print "\nNastepnik dwójki: ", church_na_int(succ(two)),
print "\n2^2 = ", church_na_int((exp(two)(two))),
print "\n3+4 = ", church_na_int(add(int_na_church(4))(int_na_church(3)))
print "\n23*12= ", church_na_int(mult(int_na_church(23))(int_na_church(12)))
