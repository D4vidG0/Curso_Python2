import requests
import menu
import os
import time

def randomjoke():
    urlrandom = "https://api.chucknorris.io/jokes/random"

    getResponse = requests.get(urlrandom)

    if getResponse.status_code == 200:
        data = getResponse.json()
        print("\nEste es el fabuloso chiste: \n")
        print(data["value"])
    else:
        print("\nError al realizar la solicitud.")


def getcategory():
    urlcat = "https://api.chucknorris.io/jokes/categories"
    getResponse = requests.get(urlcat)

    if getResponse.status_code == 200:
        data = getResponse.json()
        print('\n'.join(map(str, data)))
        print("\nEstas son las categorias disponibles \n")
    else:
        print("Error al realizar la solicitud.")

def catjoke(category):
    
     urlcatjoke = f"https://api.chucknorris.io/jokes/random?category={category}"
     
     getResponse = requests.get(urlcatjoke)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        print(f"\nEste es el chiste de la categoria {category}\n")
        print(data["value"])
     else:
        print("\nError al realizar la solicitud.")


if __name__ == "__main__":

    continuar = True
    while continuar:
        os.system('cls')
        print("\n*****************MENU PRINCIPAL*******************\n")
        print("1. Digite 1 para un chiste aleatorio de Chuck Norris\n")
        print("2. Digite 2 para obtener las categorias de los chistes \n")
        print("3. Digite 3 para Salir \n")
        num = input("Eliga el numero de la opcion que desea: ")

        if num == "3":
            continuar = False
        
        elif num == "1": 
            randomjoke()
            menu.volver_menu() #funcion para volver al menu

        elif num == "2":
            # print("Estas son las categorias de los chistes")
            getcategory()
            cat = str(input("Digite la categoria de la cual desea el chiste: "))
            catjoke(cat)
            menu.volver_menu()
        
        else:
            print("\nERROR OPCION NO VALIDA\n")
            time.sleep(2)

   