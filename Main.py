import os

def mostrar_menu():
    print("\n===== MENÚ DE GESTIÓN DE ARCHIVOS =====")
    print("El directorio actual es: ", os.getcwd())
    print("1. Contenido del directorio actual")
    print("2. Creación de nuevo directorio")
    print("3. Creación de nuevo archivo de texto")
    print("4. Añadir texto a un archivo existente")
    print("5. Eliminar un archivo o directorio")
    print("6. Mostrar los detalles del archivo")
    print("7. Salir")

def listar_contenido():
    print("\n Este directorio contiene: ")
    try:
        elementos = os.listdir()
        if not elementos:
            print("El directorio no contieene nada (Directorio Vacío)")
        else:
            for elemento in elementos:
                if os.path.isdir(elemento):
                    print(f"*Carpeta* {elemento}")
                elif os.path.isfile(elemento):
                    print(f"*Archivo* {elemento}")
                else:
                    print(f"*Otro/s* {elemento}")
    except Exception as e:
        print("|||| ERROR ||||", str(e))

def crear_directorio():
    nombre = input("\n Pon el nombre con el que quieras llamar a tu nuevo directorio: ")
    try:
        if os.path.exists(nombre):
            print("Ese nombre ya está usado.")
        else:
            os.mkdir(nombre)
            print(f"El directorio '{nombre}' ha sido creado.")
    except Exception as e:
        print("|||| ERROR AL CREAR EL DIRECTORIO ||||", str(e))

def crear_archivo():
    nombre = input("\n Introduce el nombre del archivo con la extensión .txt "
                   "\n Ejemplo Prueba.txt : ")
    try:
        if os.path.exists(nombre):
            print("**** Con ese nombre ya hay un archivo ****")
        else:
            contenido = input("Adelante empieza a rellenar el archivo con texto: ")
            with open(nombre, "w", encoding='utf-8') as archivo:
                archivo.write(contenido + '\n')
            print((f" El archivo '{nombre}' ha sido creado. "))
    except Exception as e:
        print("|||| ERROR AL CREAR EL ARCHIVO ||||")

def main():
    while True:
        mostrar_menu()
        opcion = input("Pon el número de una de las opciones: ")

        if opcion == "1":
            listar_contenido() #Listar contenido
        elif opcion == "2":
            crear_directorio() #Crear directorio
        elif opcion == "3":
            crear_archivo() #Crear archivo
        elif opcion == "4":
            pass #Escribir archivo
        elif opcion == "5":
            pass #Eliminar elemento
        elif opcion == "6":
            pass #Mostrar info
        elif opcion == "7":
            print("*** Regresa cuando quieras ***")
            break
        else:
            print("|||| Selecciona una opción valida del 1 al 7 ||||")

if __name__ == '__main__':
    main()