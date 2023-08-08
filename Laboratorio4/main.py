import pandas as pd
import matplotlib.pyplot as plt

# Funcion para leer el archivo csv
data = pd.read_csv("ventas.csv")

#Linea para convertirlo en dataframe
df = pd.DataFrame(data)

#Linea de codigo para agregar las ganancias
df["Ganacia"] = df["Ventas"] - df["Gastos"]

print(df)


# #Crear la gráfica de lineas
plt.plot(df["Mes"], df["Ventas"], label="Ventas", color='m')
plt.plot(df["Mes"], df["Gastos"], label="Gastos", color='c')
plt.xlabel("Mes", fontsize="20")
plt.ylabel("Cantidades",fontsize="20")
plt.title("Evolucion Mensual", fontsize="30")
plt.legend(fontsize="20")
plt.show()
