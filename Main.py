import os
import shutil


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

def escribir_archivo():
    nombre = input("\n Cual es el archivo al que quieres añadir texto: ")
    try:
        if not os.path.isfile(nombre):
            print("**** No encontramos ese archivo ****")
        else:
            texto_escrito_nuevo = input("Dime que texto quieres añadir: ")
            with open(nombre, 'a', encoding='utf-8') as archivo:
                archivo.write(texto_escrito_nuevo + '\n')
            print(f"**** Has añadido texto en '{nombre}' ****")
    except Exception as e:
        print("|||| ERROR HAS ESCRITO DE FORMA INCORRECTA EL ACHIVO:", str(e), "||||")

def eliminar():
    nombre = input("\n Dime qué elemento quieres eliminar: ")
    try:
        if not os.path.exists(nombre):
            print("**** No encontramos ese elemento ****")
        elif os.path.isfile(nombre):
            os.remove(nombre)
            print(f"El archivo:  '{nombre}' ha sido eliminado.")
        elif os.path.isdir(nombre):
            confirmacion = input(f" La carpeta '{nombre}' contiene archivos. ¿Estas seguro de que la quieres eliminar?. Elije #SI# o #NO#")
            if confirmacion.lower() in ["SI","Si","si","sí","Sí","SÍ"]:
                shutil.rmtree(nombre)
                print(f"Has eliminado la carpeta '{nombre}' y todo su contenido.")
            else:
                print("No has eliminado nada has cancelado la operación. ")
        else:
            print("**** Ese elemento no es ni una carpeta ni un archivo ****")
    except Exception as e:
        print("|||| ERROR NO SE HA ELIMINADO CORRECTAMENTE EL ELEMENTO: ", str(e),"||||")
def info():
    nombre = input("\n Te mostraré la información del archivo o carpeta: ")
    try:
        if not os.path.exists(nombre):
            print("**** No encontramos ese archivo o carpeta, inténtalo de nuevo. ||||")
        else:
            peso = os.path.exists(nombre)
            from datetime import datetime
            timestamp = os.path.getmtime(nombre)
            ultima_modificacion = datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S')
            tipo = "~CARPETA~" if os. path.isdir(nombre) else "~ARCHIVO~"
            print(f"\n La información del archivo '{nombre}' es: ")
            print(f"\n Fecha de la última modificación: '{ultima_modificacion}'")
            print(f"\n El tipo de archivo es: '{tipo}'")
            print(f"\n El tamaño del archivo es '{peso}' Bytes")
    except Exception as e:
        print("|||| ERROR AL MOSTRAR LA INFORMACIÓN DEL ARCHIVO: ",str(e), "||||")
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
            escribir_archivo() #Escribir archivo
        elif opcion == "5":
            eliminar() #Eliminar elemento
        elif opcion == "6":
            info() #Mostrar info
        elif info() == "7":
            print("*** Regresa cuando quieras ***")
            break
        else:
            print("|||| Selecciona una opción valida del 1 al 7 ||||")

if __name__ == '__main__':
    main()