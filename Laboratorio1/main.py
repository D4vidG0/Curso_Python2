import Trig as T
import menu
import logs

continuar = True
while continuar:
    print("\n*****************MENU PRINCIPAL*******************\n")
    print("1. Obtener seno de π \n")
    print("2. Obtener coseno de π \n")
    print("3. Obtener tangente de π \n")
    print("4. Salir \n")
    num = int(input("Eliga el numero de la opcion que desea: "))
    if num == 4:
      continuar = False
    elif num == 1: #Elige el seno de pi
       res = T.Trig() 
       res = res.sen() #convoca al metodo para calcular el seno
       print(f"El seno de π es: "+ str(res))
       logs.log_resultado("El seno de pi es: " + str(res)) 
       menu.volver_menu() #funcion para volver al menu

    elif num == 2: #Elige el cose de pi
       res = T.Trig() 
       res = res.cos() #convoca al metodo para calcular el coseno
       print(f"El coseno de π es: "+ str(res))
       logs.log_resultado("El coseno de pi es: " + str(res)) 
       menu.volver_menu() #funcion para volver al menu

    elif num == 3: #Elige la tangente de pi
        res = T.Trig() 
        res = res.tan() #convoca al metodo para calcular la tangente
        print(f"La tangente de π es:"+ str(res))
        logs.log_resultado("La tangente de pi es: " + str(res)) 
        menu.volver_menu() #funcion para volver al menu
        
