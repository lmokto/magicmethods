
'''

http://jolthgs.wordpress.com/2013/04/20/metodos-especiales-avanzados-de-las-clases-en-python/

__cmp__(self, other):
Es un método que se invoca cuando realizamos operaciones de comparación con una instancias de una clase y busca emular la funcionalidad de la función interna cmp(). La función interna cmp(x,y), retorna 1 si x>y, retorna -1 si x<y, y retorna 0 si x==y. Hay reglas que definen cuándo se consideran iguales dos tipos de datos incorporados; por ejemplo, los diccionarios son iguales cuando tienen todas las mismas claves y valores, y las cadenas son iguales cuando tienen la misma longitud y contienen la misma secuencia de caracteres. Para instancias de clases, podemos definir el método __cmp__ y programar la lógica de la comparación nosotros mismos, y entonces puede usar == para comparar instancias de sus clases y Python invocará a su método especial __cmp__ por usted.

'''

class Clientes:
    def __init__(self, dict=None):
        self.data = {}
    if dict is not None:
        self.update(dict)
    def update(self, dict=None):
        self.data.update(dict)
    def __len__(self):
        return len(self.data)
    def __cmp__(self, dict):
        return cmp(self.data, dict)

c = Clientes({'nombre':'Jorge', 'apellidos':'Toro', 'nit':'100244235', 'cargo':'aseador', 'telefono':None})
len(c)
#5
d = {1:'uno', 2:'dos', 3:'tres'}
len(d)
#3
cmp('124', '33')
#-1
d == c
#False
c > d
#True
c < d
#False
cmp(c, d)
#1
b = Clientes({'nombre':'Jorge', 'apellidos':'Toro', 'nit':'100244235', 'cargo':'aseador', 'telefono':None})
cmp(c, b)
#0
f = {1:'uno', 2:'dos', 3:'tres', 4:'cuatro', 5:'cinco'}
cmp(c,f)
#1
h = {'nombre':'Jorge', 'apellidos':'Toro', 'nit':'100244235', 'cargo':'aseador', 'telefono':None}
cmp(c,h)
#0
j = {'nombre':'Ferz', 'apellidos':'Benitez', 'nit':934034, 'cargo':None, 'telefono':None}
cmp(c,j)
#1
v = {'n':'Jorge', 'a':'Toro', 'n':'100244235', 'c':'aseador', 't':None}
cmp(c,v)
#1


'''Qué pasa si no tenemos definido el método especial __cmp__ y realizamos comparaciones con los operadores de "comparación".'''

class Clientes1:
    def __init__(self, dict=None):
        self.data = {}
    if dict is not None:
        self.update(dict)
    def update(self, dict=None):
        self.data.update(dict)
    def __len__(self):
        return len(self.data)

c = Clientes1({'nombre':'Jorge', 'apellidos':'Toro', 'nit':'100244235', 'cargo':'aseador', 'telefono':None})
len(c)
#5
d = {1:'uno', 2:'dos', 3:'tres'}
len(d)
#3
d == c # Esto siempre es False.
#False
c == {'nombre':'Jorge', 'apellidos':'Toro', 'nit':'100244235', 'cargo':'aseador', 'telefono':None}
#False
d > c # Esto debe ser False!!.
#True
len(d) > len(c)
#False
c > d # Esto debe ser True!!.
#False
