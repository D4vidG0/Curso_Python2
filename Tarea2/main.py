import Tarea1 
import requests
import pandas as pd
import matplotlib.pyplot as plt
import menu
import os
import time

def plot_top_10_countries(): #Grafica los 10 paises donde mas se juega el juego
    
     urlcountry = f"https://api.opendota.com/api/distributions"
     
     getResponse = requests.get(urlcountry)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        x =data["country_mmr"]["rows"]
        df = pd.DataFrame(x)
        y = df.sort_values(by=['count'], ascending=False).head(10)
        # print(y)
        c = ['purple', 'yellow', 'black', 'blue', 'orange', 'cyan', 'pink','brown','grey','olive']
        plt.bar(y["common"], y["count"],color=c)
        plt.xlabel("Paises", fontsize="10")
        plt.ylabel("Numero de jugadores",fontsize="10")
        plt.title("Top 10 de paises con mas jugadores", fontsize="20")
        plt.show()    
     else:
        print("\nError al realizar la solicitud.")

def plot_top_5_best(): #grafica los 5 mejores paises a nivel mundial del juego 
    
     urlcountry = f"https://api.opendota.com/api/distributions"
     
     getResponse = requests.get(urlcountry)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        x =data["country_mmr"]["rows"]
        df = pd.DataFrame(x)
        y = df.sort_values(by=['avg'], ascending=False).head(5)
        plt.pie(y["avg"], labels = y["common"], autopct = '%1.1f%%')
        plt.legend(loc="upper right",fontsize="8")
        plt.title("Top 5 de paises con mejores jugadores", fontsize="20")
        plt.show()    
     else:
        print("\nError al realizar la solicitud.")

def plot_top_10_str(): #Grafica los 10 heroes con mas atributo de fuerza
    
     urlstr = f"https://api.opendota.com/api/heroStats"
     
     getResponse = requests.get(urlstr)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        df = pd.DataFrame(data)
        y = df.sort_values(by=['base_str'], ascending=False).head(10)
        c = ['purple', 'yellow', 'black', 'blue', 'orange', 'cyan', 'pink','brown','grey','olive']
        plt.barh(y["localized_name"], y["base_str"],color=c)
        plt.title("Top 10 de los heroes con mayor atributo de fuerza", fontsize="20")
        plt.xlabel("Heroes", fontsize="10")
        plt.ylabel("Fuerza base (con la que empieza cada heroe)",fontsize="10")
        plt.show()    
     else:
        print("\nError al realizar la solicitud.")

if __name__ == "__main__":
    
    continuar = True
    while continuar:
      os.system('cls')
      print("\n**************************MENU PRINCIPAL******************************\n")
      print("\n****************PROGRAMA PARA VER DATOS DEL JUEGO DOTA 2***************\n")
      print("1. Digite 1 para ver datos interesantes del juego\n")
      print("2. Digite 2 para ver los datos de Costa Rica\n")
      print("3. Digite 3 para ver el grafico de Top 10 de paises con mas jugadores\n")
      print("4. Digite 4 para ver el grafico de Top 5 de Paises con mejores jugadores\n")
      print("5. Digite 5 para ver el grafico de Top 10 de heroes con mayor fuerza\n")
      print("6. Digite 6 para Salir \n")
      num = input("Eliga el numero de la opcion que desea: ")

      if num == "6":
            os.system('cls')
            print("\nSaliendo del programa... \n")
            time.sleep(2)
            continuar = False
        
      elif num == "1":
            os.system('cls')
            print("\nNombres de los heroes: \n") 
            Tarea1.getheroespeed()
            Tarea1.getheroestr()
            Tarea1.getheroeagi()
            Tarea1.getheroeint()
            Tarea1.getcountryplayers()
            Tarea1.getcountrymmr()
            menu.volver_menu() #funcion para volver al menu
     
      elif num == "2":
            os.system('cls')
            Tarea1.country_cr()
            menu.volver_menu()

      elif num == "3":
            os.system('cls')
            plot_top_10_countries()
            menu.volver_menu()  

      elif num == "4":
            os.system('cls')
            plot_top_5_best()
            menu.volver_menu()  
     
      elif num == "5":
         os.system('cls')
         plot_top_10_str()
         menu.volver_menu()  

      else:
            os.system('cls')
            print("\nERROR OPCION NO VALIDA\n")
            time.sleep(2) 
    