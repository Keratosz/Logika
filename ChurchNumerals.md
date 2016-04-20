# Liczebniki Churcha
Liczebniki Churcha są sposobem reprezentacji liczb naturalnych w rachunku lambda, stworzonymi przez twórcę ssamego rachunku.
Definicja poszczególnych liczb naturalnych w rachunku lambda opiera się na definicji zera i tworzeniu kolejnych jego następników.
Funkcja bierze kolejny argument x i zwraca jego n-tą kompozycję. Jako język przykładowych implementacji pod przykładami wybrałem Pyton.

## Reprezentacja w rachunku lambda

Liczba | Reprezentacja w rachunku lambda 
--- | --- 
0 | λf.λx.x
1 | λf.λx.f(x)
2 | λf.λx.f( f(x) )
5 | λf.λx.f( f( f( f( f(x) ) ) ) )
n | λf.λx.f^n(x)
n+1 | λf.λx.f(nf(x))

```python
zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
five = lambda f: lambda x: f(f(f(f(f(x)))))
```
---
## Podstawowe operacje na liczbach w rachunku lambda
Dodawanie w rachunku lambda to po prostu m-te złożenie od n-tego złożenia dla liczb m i n, oprócz poniższego zapisu w tabeli można je także zdefiniować
jak m wykonań funkcji następnika na liczbie n. Podobnie mnożenie ktore może być po prostu dodawaniem liczby m do liczby m n razy.

Zapis tradycyjny | Nazwa operacji | Zapis w rachunku lambda
--- | --- | ---
n+1 | nastepnik | λn.λf.λx.f (n f (x) )
n + m | dodawanie | λm.λn.λf.λx.m f (nf x)
n * m | mnożenie | λm.λn.λf.m (n f)
m^n | potęgowanie |λn.λf.λx.(n m) f x

```python
# Definicja nastepnika
succ = (lambda n: lambda f: lambda x: f(n(f)(x)))
# Dodawanie dwóch liczebników Churcha n i m.
add = (lambda m: lambda n: lambda f: lambda x: n(f)(m(f)(x)))
# Mnożenie liczb n i m.
mult = (lambda m: lambda n: lambda f: lambda x: n(m(f))(x))
# Podnoszenie liczby m do potęgi n-tej
exp = lambda m: lambda n: lambda f: lambda x:((n)(m)) (f) (x)
```
