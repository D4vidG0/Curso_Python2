import requests
import menu
import os
import time

def getheroe(): #obtiene el nombre de todos los heroes de dota2
    urlheroe = "https://api.opendota.com/api/heroes"

    getResponse = requests.get(urlheroe)

    if getResponse.status_code == 200:
        data = getResponse.json()
        for item in data:
            print(item["localized_name"])
    else:
        print("\nError al realizar la solicitud.")


def getheroespeed(): #obtiene la velocidad de movimiento al principio del juego para cada heroe
    
     urlspeed = f"https://api.opendota.com/api/heroStats"
     
     getResponse = requests.get(urlspeed)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        for item in data:
            print("Name: "+ item["localized_name"]) 
            print("Move speed: ", end=" ")
            print(item["move_speed"]) 
            print("\n")
     else:
        print("\nError al realizar la solicitud.")

def getheroeroles(): #obtiene los roles de cada heroe del juego
    
     urlroles = f"https://api.opendota.com/api/heroStats"
     
     getResponse = requests.get(urlroles)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        for item in data:
            print("Name: "+ item["localized_name"]) 
            print("Role: ", end=" ")
            print(item["roles"])#
            print("\n")
     else:
        print("\nError al realizar la solicitud.")

def getheroestr(): #obtiene la fuerza con la que empieza cada heroe del juego
     
     urlstr = f"https://api.opendota.com/api/heroStats"
     
     getResponse = requests.get(urlstr)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        for item in data:
            print("Name: "+ item["localized_name"]) 
            print("Base strength: ", end=" ")
            print(item["base_str"])
            print("\n")
     else:
        print("\nError al realizar la solicitud.")

def getheroeagi(): #obtiene la agilidad con la que empieza cada heroe del juego
     
     urlagi = f"https://api.opendota.com/api/heroStats"
     
     getResponse = requests.get(urlagi)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        for item in data:
            print("Name: "+ item["localized_name"]) 
            print("Base agility: ", end=" ")
            print(item["base_agi"])
            print("\n")
     else:
        print("\nError al realizar la solicitud.")

def getheroeint(): #obtiene la inteligencia con la que empieza cada heroe del juego
     
     urlint = f"https://api.opendota.com/api/heroStats"
     
     getResponse = requests.get(urlint)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        for item in data:
            print("Name: "+ item["localized_name"]) 
            print("Base inteligence: ", end=" ")
            print(item["base_int"])
            print("\n")
     else:
        print("\nError al realizar la solicitud.")

def getcountryplayers(): #obtiene el pais donde se juega el juego y la cantidad de jugadores que hay en ese pais
    
     urlcountry = f"https://api.opendota.com/api/distributions"
     
     getResponse = requests.get(urlcountry)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        x =data["country_mmr"]["rows"]
        for item in x: 
            print("Pais: " + item["common"]) 
            print("N° de jugadores: "+ " "+ str(item["count"]))
            print("\n")
     else:
        print("\nError al realizar la solicitud.")


def getcountrymmr(): #obtiene el pais y el mmr promedio de cada pais
    
     urlmmr = f"https://api.opendota.com/api/distributions"
     
     getResponse = requests.get(urlmmr)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        x =data["country_mmr"]["rows"]
        for item in x: 
            print("Pais: " + item["common"]) 
            print("MMR promedio: "+ " "+ str(item["avg"]))
            print("\n")
     else:
        print("\nError al realizar la solicitud.")

if __name__ == "__main__":
    
     continuar = True
     while continuar:
        os.system('cls')
        print("\n**************************MENU PRINCIPAL******************************\n")
        print("\n****************PROGRAMA PARA VER DATOS DEL JUEGO DOTA 2***************\n")
        print("1. Digite 1 para ver el nombre de todos los heroes del juego\n")
        print("2. Digite 2 para ver la velocidad de movimiento con la que empiezan todos los heroes\n")
        print("3. Digite 3 para ver el rol que los heroes pueden tomar durante el juego\n")
        print("4. Digite 4 para ver la fuerza base con la que empiezan los heroes\n")
        print("5. Digite 5 para para ver la agilidad base con la que empiezan los heroes\n")
        print("6. Digite 6 para ver la base inteligencia base con la que empiezan los heroes\n")
        print("7. Digite 7 para ver la cantidad de jugadores que hay en cada pais\n")
        print("8. Digite 8 para ver el MMR promedio que hay en cada pais\n")
        print("9. Digite 9 para Salir \n")
        num = input("Eliga el numero de la opcion que desea: ")

        if num == "9":
            os.system('cls')
            print("\nSaliendo del programa... \n")
            time.sleep(2)
            continuar = False
        
        elif num == "1":
            os.system('cls')
            print("\nNombres de los heroes: \n") 
            getheroe()
            menu.volver_menu() #funcion para volver al menu
     
        elif num == "2":
            os.system('cls')
            getheroespeed()
            menu.volver_menu()     
     
        elif num == "3":
            os.system('cls')
            getheroeroles()
            menu.volver_menu()  
     
        elif num == "4":
         os.system('cls')
         getheroestr()
         menu.volver_menu()  

        elif num == "5":
         os.system('cls')
         getheroeagi()
         menu.volver_menu()  

        elif num == "6":
         os.system('cls')
         getheroeint()
         menu.volver_menu()  

        elif num == "7":
         os.system('cls')
         getcountryplayers()
         menu.volver_menu()  

        elif num == "8":
         os.system('cls')
         getcountrymmr() 
         menu.volver_menu()  
        
        else:
            os.system('cls')
            print("\nERROR OPCION NO VALIDA\n")
            time.sleep(2)


#Functions for endpoints

    # getheroe()
    # getheroespeed()
    # getheroeroles()
    # getheroestr()
    # getheroeagi()
    # getheroeint()
    #getteam()
    # getcountryplayers()
    # getcountrymmr()        

#Possible graphics

#country vs average mmr
#country vs number of players
#heroe vs move speed
#heroe vs str
#Heroe vs int
#Heroe vs agi
