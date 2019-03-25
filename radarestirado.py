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

def mostrarcarre(doc):
    provincia=input("Introduzca una provincia: ")
    listacarre=doc.xpath("/RAIZ/PROVINCIA[NOMBRE='%s']/CARRETERA/DENOMINACION/text()"%(provincia))
    print("")
    print("Contamos con", len(listacarre),"radares en %s." %(provincia))
    print("Los nombres de sus carreteras son: ")
    print("")
    return list(set(listacarre))

def mostrarprovi(doc,carretera):
    listaprovi=doc.xpath("//CARRETERA[DENOMINACION='%s']/../NOMBRE/text()"%(carretera))
    print("")
    print("La carretera %s pasa por: " %(carretera))
    print("")
    return listaprovi

def contarad(doc,carretera):
    cuentarad=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/SENTIDO/text()"%(carretera))
    print("Cuenta con",len(cuentarad),"radares.")
    print("")

def ejer5(doc,carretera):
    listalati=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_INICIAL/LATITUD/text()"%(carretera))
    listalongi=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_INICIAL/LONGITUD/text()"%(carretera))
    for i in range(len(listalati)):
        print("http://www.openstreetmap.org/#map=20/%s/%s" %(listalati[i],listalongi[i]))
        
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
    elif opcion==3:
        for i in mostrarcarre(doc):
            print("-",i)
        print("")
    elif opcion==4:
        carretera=input("Introduzca una carretera: ")
        for i in mostrarprovi(doc,carretera):
            print("-",i)
        print("")
        contarad(doc,carretera)
    elif opcion==5:
        carretera=input("Introduzca una carretera: ")
        print("")
        contarad(doc,carretera)
        print("Sus coordenadas son las siguientes: ")
        print("")
        ejer5(doc,carretera)
        print("")
    elif opcion==0:
        print("Adios")
        break
    else:
        print("Error de opción")