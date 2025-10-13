# MPO_Proyecto2
Segundo Proyecto de evaluación continua de MPO (Python) 1ºGS de DAM
##Proyecto 2: Gestor de Archivos en Consola
Objetivo del proyecto¶
Desarrollar una aplicación de consola en Python que permita gestionar archivos y carpetas del sistema de forma sencilla. El usuario podrá listar contenido, crear o eliminar carpetas y archivos, escribir dentro de ellos y visualizar información básica.

Requisitos funcionales mínimos¶
Tu aplicación deberá permitir al usuario interactuar mediante un menú principal que se repita hasta que decida salir.

MENÚ PRINCIPAL¶
Listar contenido del directorio actual
Crear un nuevo directorio
Crear un archivo de texto
Escribir texto en un archivo existente
Eliminar un archivo o directorio
Mostrar información del archivo
Salir
Detalles de funcionamiento¶
El programa debe mostrar la ruta actual en todo momento.
Al listar el contenido, deberá indicar si cada elemento es archivo o carpeta.
Al crear un archivo de texto, deberá permitir introducir un nombre y escribir contenido inicial (usando open() y write()).
La opción de escribir texto deberá abrir un archivo existente y añadir nuevo contenido al final.
Al mostrar información, deberá indicar tamaño, fecha de modificación y tipo (archivo o carpeta).
El programa debe gestionar errores comunes, tales como:
Intentar acceder o escribir en un archivo que no existe.

Intentar eliminar un archivo o carpeta inexistente.

Intentar crear un archivo o carpeta con un nombre ya existente.
Problemas de permisos o rutas incorrectas.
En todos estos casos, el programa no debe cerrarse, sino mostrar un mensaje de error amigable para el usuario.
Contenidos del módulo que se aplican¶
Entrada/salida de datos por consola.
Manejo de archivos de texto (open(), read(), write(), append(), close()).
Uso del módulo os para manipular el sistema de archivos:

os.listdir(), os.getcwd(), os.mkdir(), os.remove(), os.rmdir(), os.path.

Control de flujo (if, elif, else).
Bucles (while, for).
Funciones con parámetros y valores de retorno.
