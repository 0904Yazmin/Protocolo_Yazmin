#Yazmin Reyes Barquera   5M10
from io import open
archivo=open ("Protocolo1.txt", "w+")
a="seguir"
ancho =0
pos=0
rep=0
resp = "si"
i = 1
sub = 1
regla_an=""
newL=[]
listas=[]

def menu():
    print( "             _______________  MENÚ  ___________________")
    print("\n    Elige la accion que quieres hacer para tu protocolo:")
    print("1   Ver el protocolo.")
    print("2   Añadir una instrucción.")
    print("3   Modificar una instrucción de una posición especifica.")
    print("4   Insertar lista anidada a la instrucción.") 
    print("""5.   Salir del programa.
    _______________________________________________________________""")

def crearArchivo():
    archivo=open ("Protocolo1.txt", "w")
    archivo.close

def Añadir():
    archivo=open("Protocolo1","a+")
    archivo.write(str(rep)+".   " + regla +"\n")
    archivo.close



print("                                Creador de protocolos.")
print("------------------------------------------------------------------------------------------")
print("En este programa usted podrá crear un protocolo para una determinada situación \n" )

nombre = input("Escribe el nombre del protocolo a crear:   ")

archivo.write(""" Editor de protocolos  \n"""+
                    "Nombre del protocolo creado:  " + nombre + "\n" )
crearArchivo()
regla = input("Ingresa la instrucción "+ str(i) + ":       ")

archivo.write(str(i)+".   " + regla +"\n")
listas.append(regla)


while resp=="si":
    print("\n\n")
    crearArchivo()
    ancho=len(listas)
    for rep in range(ancho):
        cadena=listas[rep]
        Añadir()
    
    menu()
    op =int (input("Escoge una opción:        "))

    if op == 1:
        print("_________________________")
        print("Tu lista de instrucciones es: ")
        for rep in range(ancho):
            print(str(rep+1)+".   "  + listas[rep])
            
    elif op == 2:
        print("_________________________")
        regla = input("Ingresa la instrucción "+ str(rep+2) + ":       ")
        listas.append(regla)
        archivo.write(str(rep +2)+".   " + regla +"\n")
        
    elif op == 3:
        print("_________________________")
        pos=int(input("Ingrese la posición en que quiere que se encuentre su nueva instrucción:     " ))
        regla=input("Ingresa la nueva instrucción que desea añadir:     ")
        if pos == 1:
            listas.pop(0)
            listas.insert(0,regla)
        else:
            listas.pop(pos-1)
            listas.insert(pos-1,regla)
            
    elif op == 4:
        print("__________ Lista anidada_______________")
        regla_an = input("Ingresa la instrucción "+ str(rep+1)+ "." + str(sub) + ":       ")
        newL.append(regla_an)
        archivo.write("      "+ str(rep +1)+"." + str(sub) + ": "+ regla_an +"\n")
        sub = sub +1
        
    elif op == 5:
        print("-------Su archivo de protocolo se ha guardado con el nombre de 'Protocolo1.txt'")
        print("-------Gracias por usar este programa, ten un buen dia :D ")
        archivo.close()
        break
    else:
        print("Opción no valida, ingresa otra.")
    resp = str(input("\n" + "¿Desea hacer otra acción?   si / no:  " ))
    if resp== "no":
        print("-------Su archivo de protocolo se ha guardado con el nombre de 'Protocolo1.txt'")
        print("-------Gracias por usar este programa, ten un buen dia :D ")
        archivo.close()



