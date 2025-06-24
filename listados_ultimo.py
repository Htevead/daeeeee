juegos={
    1:{
        "nombre": "Minecraft",
        "precio": 30000,
        "code": "HBlo3345",
    },
    
    2:{
        "nombre": "Gta v",
        "precio": 15000,
        "code": "LKbh6784",
    },
}

def agregar_juego(dic):
    ultima=list(dic.keys())[-1]
    nombre=input("\nIngrese el nombre del juego: ")
    precio=int(input("\nIngrese el precio del juego: "))
    while True:
        code=input("\nIngrese el codigo del juego: ")
        if valida_code(code):
            dic[ultima+1]={
                    "nombre":nombre,
                    "precio":precio,
                    "code":code
                }
            print("Codigo ingresado con exito")
            break
        else:
            print("\nCodigo invalido, el codigo debe tener 2 mayusculas, 2 minusculas, 4 numeros")




def valida_code(clave):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for palabra in clave:
        if palabra.isupper():
            Mayuscula+=1
        if palabra.islower():
            Minuscula+=1
        if palabra.isdigit():
            Numero+=1
    if Mayuscula==2 and Minuscula==2 and Numero==4 :
        print("\nEl codigo está bien escrito")
        return True
    else:
        print("El codigo está mal escrito")
        return False

def mostrar_juegos(dic):
    for key,value in dic.items():
        print(key, value)
    
def act_juegos(dict):
    mostrar_juegos(dict)
    act=int(input("\nSeleccione el juego que desea actulizar: "))
    while True:
        print('''
                1.- Nombre
                2.- Precio
                3.- Code
                4.- Salir''')
        dato=int(input("\n¿Que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre: ")
                dict[act]["nombre"]=n
            case 2:
                n=input("ingrese el nuevo precio: ")
                dict[act]["precio"]=n
            case 3:
                n=input("ingrese el nuevo codigo: ")
                dict[act]["code"]=n
                if valida_code(n):
                    dict[act]["code"]=n
                else:
                    print("\nel paramatro del codigo no es correcto\n")
                    print('''
                    el codigo debe tener, 2 mayuscula, 2 minuscula, 
                    4 numeros''')
            case 4:
                break
            case _:
                    print("Opcion invalida")

def borrar_juego(dict):
    mostrar_juegos(dict)
    borrar=int(input("\nSeleccione el juego a borrar"))
    if borrar in dict:
        del dict[borrar]
    else:
        print("El juego no existe")


while True:
    try:
        print('''
            1.- Agregar juego
            2.- Mostrar juegos
            3.- Actualizar juego
            4.- Borrar juego
            5.- Salir
            ''')
        op=int(input("\nSeleccione una opción: "))
        match op:
            case 1:
                agregar_juego(juegos)
            case 2:
                mostrar_juegos(juegos)
            case 3:
                act_juegos(juegos)
            case 4:
                borrar_juego(juegos)
            case 5:
                break
            case _:
                print("\nOpción invalida\n")

    except Exception:
        print("\nAlgo ha salido mal, intente nuevamente\n")