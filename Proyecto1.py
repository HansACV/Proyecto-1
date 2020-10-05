

Sets=[]
palabras=['CREATE SET','LOAD INTO','FILES','USE SET','SELECT','WHERE','AND',
          'LIST ATTRIBUTES','MAX','MIN','SUM','COUNT','REPORT TO','SCRIPT','REPORT TOKENS']
tokens=[]

NombreSet=""



class Token:
    token=''
    des=''

    def __init__(self,a,b):
        self.token=a
        self.des=b

class Atributo:
    Tipo=""
    Nombre=""
    Valor=""
    def __init__(self,Tipo,Nombre,Valor):
        self.Tipo=Tipo
        self.Nombre=Nombre
        self.Valor=Valor

    def imprimir(self):
        print(self.Nombre+": "+self.Valor)





class Conjunto:
    Conjunto=[]

    def __init__(self):
        print()

    def agregarAtributos(self,listaAtributos):
        self.Conjunto.append(listaAtributos)

    def imprimir(self):
        for a in self.Conjunto:
            for b in a:
                b.imprimir()


class Set:
    ID=""
    Conjuntos=[]

    def __init__(self,ID):
        self.ID=ID
        print('El set '+self.ID+' a sido creado')

    def agregarConjunto(self,ListaConjuntos):
        self.Conjuntos.append(ListaConjuntos)

    def imprimir(self):
        for a in self.Conjuntos:
            a.imprimir()
            break









def CrearSeT(cadena):
    set = Set(cadena)
    Sets.append(set)
    tokens.append(Token(cadena, 'Identificador'))

def cargarEn(cadena):
    nombre=''
    for a in cadena:
        if a.isalpha():
            nombre=nombre+a
        elif a == ' ':
            break
    cadena2 = cadena.replace(nombre+' FILES ','')
    tokens.append(Token(nombre, 'Identificador'))
    tokens.append(Token('FILES', 'palabra reservada'))
    rutas = cadena2.split(', ')
    for a in rutas:
        tokens.append(Token(a, 'Identificador'))
        leerRuta(a,nombre)


def leerRuta(ruta,nombre):
    archivo = open(ruta,'r')
    lineas = archivo.readlines()
    texto=""
    for a in lineas:
        aux = []
        for b in a:
            texto=texto+b
            if b==">":
                leertexto(texto,nombre,aux)
                texto=""
    archivo.close()
    for a in Sets:
        if a.ID==nombre:
            a.imprimir()
            break

def leertexto(linea,nom,aux):
    estado=0
    nombre=''
    valor=''
    tipo=''
    for a in linea:
        if estado==0:
            if a=='(' or a==' ' or a=='<':
                estado=0
            elif a=='[':
                estado=1
            elif a=='=':
                estado=2
            elif a=='>':
                estado=0
                conjunto=Conjunto()
                conjunto.agregarAtributos(aux)
                for a in Sets:
                    if a.ID==nom:
                        a.agregarConjunto(conjunto)
                        break



        elif estado == 1:
            if a.isalpha() or a == '_':
                nombre=nombre+a
                estado=1
            elif a==']':
                estado=0
        elif estado==2:
            if a.isnumeric() or a=='.' or a=='-':
                valor=valor+a
                estado=2
                tipo='numerico'
            elif a.isalpha():
                valor=valor+a
                estado=2
                tipo='boolean'
            elif a==',':
                estado=0
                aux.append(Atributo(tipo, nombre, valor))
                print(tipo + " " + nombre + " " + valor)
                nombre=""
                tipo=""
                valor=""
            elif a=='"':
                estado=3
            elif a == ' ':
                estado=2
            else:
                estado = 0
                aux.append(Atributo(tipo, nombre, valor))
                print(tipo + " " + nombre + " " + valor)
                nombre = ""
                tipo = ""
                valor = ""
        elif estado==3:
            if a != '"':
                valor=valor+a
                estado=3
                tipo='cadena'
            elif a=='"':
                estado=0
                aux.append(Atributo(tipo, nombre, valor))
                print(tipo + " " + nombre + " " + valor)
                nombre = ""
                tipo = ""
                valor = ""









def leerCodigo(cadena):
    print(cadena)
    comando=''
    for a in cadena:
        if a.isalpha():
            comando=comando+a
        elif a == ' ':
            if comando in palabras:
                tokens.append(Token(comando,'palabra reservada'))
                break
            else:
                comando=comando+a
    com=comando.upper()
    cadena2 = cadena.replace(com + ' ', '')
    if com == 'CREATE SET':
        CrearSeT(cadena2)

    elif com == 'LOAD INTO':
        cargarEn(cadena2)

def main():
    ciclo=True
    while(ciclo):
        ingreso = input('Ingrese comando: ')
        if (ingreso == 'salir'):
            ciclo=False
        else:
            leerCodigo(ingreso)

main()