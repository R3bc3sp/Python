# ‐*‐ coding: utf‐8 ‐*‐

import datetime as dt

def abrir_log(nombre):
    archivo = open(nombre, "a")
    fecha = str(dt.datetime.now())
    mensaje = fecha + ": Iniciando registro de errores"
    archivo.write(mensaje)
    return archivo

def guardar_log(archivo, mensaje):
    

abrir_log("log.txt")