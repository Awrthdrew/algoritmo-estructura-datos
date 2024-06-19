
a= 9
b= 12
c= 18
d= c ** b
raicesp= (-b+((b**2)-(4*a*c))**0.5)/(2*a)
raicesn= (-b-((b**2)-(4*a*c))**0.5)/(2*a)

"""Suma"""  
print(a + b + c)

#Multiplicación 
print(a * b * c)

"""El resto de la división de A y B"""
print(a/b)

#A elevado a B
print(a ** b)

"""La raíz cuadrática de C"""
print(c ** 0.5) 

#El valor de la hipotenusa de un triángulo rectángulo formado pelos catetos A y B
print((a ** 2 + b ** 2) ** 0.5)

"""Siendo A, B y C coeficientes de la Fórmula Cuadrática o Resolvente (Baskara) SUMANDO"""
print(raicesp)

#Siendo A, B y C coeficientes de la Fórmula Cuadrática o Resolvente (Baskara) RESTANDO
print(raicesn)

"""Considerando A la altura de la pared de tu dormitorio, B la profundidad de un
ropero que quieres comprar. ¿Cuál es la altura máxima de este ropero?
Imagina que va a ser montado tirado en el suelo y que cuando lo levantes no
podrá golpear el techo."""

print( (a ** 2 + b ** 2) ** 0.5) #Es esto? O se desarrolla de otra manera?
