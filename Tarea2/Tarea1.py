import requests
import pandas as pd


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
        df = pd.DataFrame(data)
        # data2 = df["localized_name"] + df["move_speed"] Esta era la funcion original
        # for item in data:
        #     print("Name: "+ item["localized_name"]) 
        #     print("Move speed: ", end=" ")
        #     print(item["move_speed"]) 
        #     print("\n")
        # print(df)
        heroe_mas_veloz = df.loc[df["move_speed"].idxmax(), "localized_name"]
        print("El heroe con mayor velocidad al principio del juego es: ", heroe_mas_veloz) #esta fue la modificacion para obtener los datos
     else:
        print("\nError al realizar la solicitud.")

def getheroestr(): #obtiene la fuerza con la que empieza cada heroe del juego
     
     urlstr = f"https://api.opendota.com/api/heroStats"
     
     getResponse = requests.get(urlstr)

     
     if getResponse.status_code == 200:
        data = getResponse.json()
        df = pd.DataFrame(data)
        # for item in data:
        #     print("Name: "+ item["localized_name"])   Esta era ka funcion original
        #     print("Base strength: ", end=" ")
        #     print(item["base_str"])
        #     print("\n")
        heroe_mas_fuerte = df.loc[df["base_str"].idxmax(), "localized_name"]
        print("El heroe con mayor fuerza al principio del juego es: ", heroe_mas_fuerte) #modificacion para la Tarea 2
     else:
        print("\nError al realizar la solicitud.")

def getheroeagi(): #obtiene la agilidad con la que empieza cada heroe del juego
     
     urlagi = f"https://api.opendota.com/api/heroStats"
     
     getResponse = requests.get(urlagi)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        df = pd.DataFrame(data)
        # for item in data:
        #     print("Name: "+ item["localized_name"])      Esta era ka funcion original
        #     print("Base agility: ", end=" ")
        #     print(item["base_agi"])
        #     print("\n")
        heroe_mas_agil = df.loc[df["base_agi"].idxmax(), "localized_name"]
        print("El heroe con mayor agilidad al principio del juego es: ", heroe_mas_agil) #Modificacion para datos de Tarea 2
     else:
        print("\nError al realizar la solicitud.")

def getheroeint(): #obtiene la inteligencia con la que empieza cada heroe del juego
     
     urlint = f"https://api.opendota.com/api/heroStats"
     
     getResponse = requests.get(urlint)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        df = pd.DataFrame(data)
        # for item in data:
        #     print("Name: "+ item["localized_name"]) Esta era la funcion original
        #     print("Base inteligence: ", end=" ")
        #     print(item["base_int"])
        #     print("\n")
        heroe_mas_int = df.loc[df["base_int"].idxmax(), "localized_name"]
        print("El heroe con mayor inteligencia al principio del juego es: ", heroe_mas_int) # Modificacion para datos de Tarea 2
     else:
        print("\nError al realizar la solicitud.")

def getcountryplayers(): #obtiene el pais donde se juega el juego y la cantidad de jugadores que hay en ese pais
    
     urlcountry = f"https://api.opendota.com/api/distributions"
     
     getResponse = requests.get(urlcountry)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        x =data["country_mmr"]["rows"]
        df = pd.DataFrame(x)
        # for item in x: 
        #     print("Pais: " + item["common"]) 
        #     print("N° de jugadores: "+ " "+ str(item["count"])) Esta era la funcion original
        #     print("\n")
        pais_mas_jugadores = df.loc[df["count"].idxmax(), "common"]
        print("Pais con mayor cantidad de jugadores: ", pais_mas_jugadores) # Modificacion para datos de Tarea 2
        pais_menos_jugadores = df.loc[df["count"].idxmin(), "common"]
        print("Pais con menor cantidad de jugadores: ", pais_menos_jugadores)
     else:
        print("\nError al realizar la solicitud.")


def getcountrymmr(): #obtiene el pais y el mmr promedio de cada pais
    
     urlmmr = f"https://api.opendota.com/api/distributions"
     
     getResponse = requests.get(urlmmr)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        x =data["country_mmr"]["rows"]
        df = pd.DataFrame(x)
        # for item in x: 
        #     print("Pais: " + item["common"]) 
        #     print("MMR promedio: "+ " "+ str(item["avg"])) Esta era la funcion original
        #     print("\n")
        # print(df['avg'].dtype)
        pais_mas_nivel = df.loc[df["avg"].astype(int).idxmax(), "common"]
        # print(type(pais_mas_nivel))
        print("Pais con mejores jugadores: ", pais_mas_nivel)
        mmr_promedio = df["avg"].astype(float).mean()
        print("Nivel de MMR promedio mundial:","{:.2f}".format(mmr_promedio)) # Modificacion para datos de Tarea 2
        cantidad_jugadores = df["count"].astype(float).sum()
        print("Cantidad de jugadores a nivel mundial:", "{:,}".format(cantidad_jugadores))
     else:
        print("\nError al realizar la solicitud.")

def country_cr(): # Funcion nueva para obtener los datos de Costa Rica
    
     urlcountry = f"https://api.opendota.com/api/distributions"
     
     getResponse = requests.get(urlcountry)
     
     if getResponse.status_code == 200:
        data = getResponse.json()
        x =data["country_mmr"]["rows"]
        df = pd.DataFrame(x)
      #   print(df)
        i= df[df["common"] == "Costa Rica"]
        country = i["common"].values[0]
        players = i["count"].values[0]
        average = i["avg"].values[0]
        print("Pais: ", country) 
        print("Cantidad de jugadores: ", players)
        print("Nivel de MMR promedio: ", average) 
      
#Estos son los datos que me parecieron interesantes

#Pais con mas MMR
#Pais con mayor cantidad de usuarios
#Heroe mas veloz del juego
#Cantidad total de jugadores

#country vs average mmr
#country vs number of players
#heroe vs move speed
#heroe vs str
#Heroe vs int
#Heroe vs agi
