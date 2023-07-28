def volver_menu():
    cont =True
    while cont:
          print()
          num1 = input("Digite Salir para regresar al menu principal: ") #este nos sirve para regresar al menu principal
          if num1 == "Salir" or num1 == "salir":
             cont = False
          else:
              print("\nERROR OPCION NO VALIDA. FAVOR DIGITAR SALIR")