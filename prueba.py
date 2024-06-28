prueba=[]

def Registro():
    RUT=int(input("Repite tu RUT: "))
    Nombre=input("Nombre: ")
    Documento=input("Documento Entregado (carnet o pase): ")
    numnote=int(input("Numero de Notebook entregado: "))
    if numnote>20 or numnote<=0:
        print("Solo hay 20 Notebooks")
        return

    regis={'RUT':RUT,
           'Nombre':Nombre,
           'Documento':Documento,
           'Numero de Note':numnote}

    prueba.append(regis)

    print("Registro Creado Correctamente!!!")

    with open ('registro.txt','w+') as file:
        file.write (f"RUT:{RUT}, Nombre:{Nombre}, Documento:{Documento}, Num de Note:{numnote}")

def Menu():
    print("Aplicacion para Notebooks")
    while True:

        print("1) Registro")
        print("2) Devolver")
        print("3) Modificar")
        print("4) Imprimir Lista de Notebooks Prestados")
        print("5) Terminar Clase")
        opcion=int(input("Selecciona una Opcion >>> "))

        if opcion==1:
            RegistroDeRut()
            Registro()

        elif opcion==2:
            Devolver()

        elif opcion==3:
            Modificar()

        elif opcion==4:
            Imprimir()

        elif opcion==5:
            Terminar()
            exit() 

        else:
            print("Seleccione una opcion disponible")


def Modificar():
    print("")


def Imprimir():
    print("Lista de Notebooks Prestados")
    with open('registro.txt','r') as file:
     lines=file.readlines()


    for i, line in enumerate(lines,start=1):
     RUT,Nombre,Documento,numnote=line.strip().split(",")
    
    with open ("Pablo Saldaña BIY1101-008D.txt",'w+') as file:
        file.write

        print(f"Pedido:{i}")
        print(f"RUT:{RUT}")
        print(f"Nombre:{Nombre}")
        print(f"Documento:{Documento}")
        print(f"Num. de Notebook:{numnote}")
        print("")



def Terminar():
    print("Clase Terminada")
    exit()

def Devolver():
    print("Devolver Notebook")
    


def RegistroDeRut():
    RUT2=int(input("Escribe tu RUT: "))

Menu()