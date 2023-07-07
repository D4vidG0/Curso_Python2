from datetime import datetime

def log_resultado(string):
    file = open("log.txt", "a") #Abre el archivo es modo append para agregar lineas
    now=datetime.today() #Agrega la hora
    fecha = now.strftime("%c")
    file.write(f"FECHA: {fecha}"+ string) #Escribe el string que es nuestro caso es el resultado de la operacion
    file.write("\n") #Puse este salto de linea para que los resultados no queden pegados
    file.close()



