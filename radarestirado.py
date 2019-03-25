from lxml import etree
doc=etree.parse('radares.xml')

def listarprovincias(doc):
    lista=doc.xpath("//NOMBRE/text()")
    return lista

def cuentaradares(doc):
    cuenta=doc.xpath("//CARRETERA/DENOMINACION/text()")
    print("")
    print("Contamos con",len(cuenta),"radares en el total de todas las carreteras.")
    print("")

print("")
while True:
    print("1. Mostrar el nombre de las provincias de las que tenemos información sobre radares.")
    print("2. Mostrar la cantidad de radares de los que tenemos información.")
    print("3. Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.")
    print("4. Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.")
    print("5. Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.(Se puede obtener la URL de OpenStreetMap para ver donde está el radar).")
    print("0. Salir")
    opcion=int(input("Elija opción: "))

    if opcion==1:
        print("")
        for i in listarprovincias(doc):
            print("-",i)
        print("")
    elif opcion==2:
        cuentaradares(doc)
    elif opcion==0:
        print("Adios")
        break
    else:
        print("Error de opción")