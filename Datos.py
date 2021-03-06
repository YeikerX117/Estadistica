#Herramientas matematicas para la ciencia de datos

#Integrantes: Jose Luis Quintero 20181020061
#             Yeimer Serrano Navarro 20181020060

from matplotlib import pyplot as plt 
import pandas as pd
import numpy as np
import statistics as st

# Función para retornar a valor Literal
def clasificar(valor):
    if valor == 1:
        print('D')
    elif valor == 2:
        print('C')
    elif valor == 3:
        print('B')
    elif valor == 4:
        print('A')
    elif valor == 5:
        print('A+')
    else:
        print('NR')
    print('')
    del valor
    
#Importacion del archivo csv
data = pd.read_csv("Pruebas_ICFES_2011-2016.csv")

#Sustituciones a los valores del dataframe 
data.replace({"NR": 0, "Nr": 0, "nan":0, "NaN":0, "A+":5,"A":4, "B":3, "C":2, "D":1}, inplace = True)
data = data.fillna(value = 0)

# Contar los colegios de la misma categoria por municipio
notMun = pd.DataFrame(columns=['Municipio', 'A+', 'A', 'B', 'C', 'D','NR']) # DataFrame con la informacion
mun = data.iloc[0, 0] # Guarda el municipio que se compara
aa, a, b, c, d, nr = 0, 0, 0, 0, 0, 0 # Contadores de los tipos de pruebas
for indice_fila, fila in data.iterrows(): 
    if (fila["MUNICIPIO"] == mun):
        if fila["AÑO 2019"] == 5:
            aa = aa + 1
        elif fila["AÑO 2019"] == 4:
            a = a + 1
        elif fila["AÑO 2019"] == 3:
            b = b + 1
        elif fila["AÑO 2019"] == 2:
            c = c + 1
        elif fila["AÑO 2019"] == 1:
            d = d + 1
        else:
            nr = nr + 1
    else:
        notMun.loc[len(notMun.index)+1]=[data.loc[indice_fila-1,"MUNICIPIO"],aa,a,b,c,d, nr] # Guardar las pruebas
        aa, a, b, c, d, nr = 0, 0, 0, 0, 0, 0 # Reinicia los contadores
        if fila["AÑO 2019"] == 5:
            aa = aa + 1
        elif fila["AÑO 2019"] == 4:
            a = a + 1
        elif fila["AÑO 2019"] == 3:
            b = b + 1
        elif fila["AÑO 2019"] == 2:
            c = c + 1
        elif fila["AÑO 2019"] == 1:
            d = d + 1
        else:
            nr = nr + 1
        mun = data.iloc[indice_fila, 0] # Pasa al siguiente municipio
    if indice_fila == len(data)-1:
        notMun.loc[len(notMun.index)+1]=[data.loc[indice_fila-1,"MUNICIPIO"],aa,a,b,c,d, nr]

#Colores para el pie
colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E", "#FF5D47", "#FA928E"]

#Asignacion de datos e impresion del pie
plt.pie(notMun['C'], labels = notMun['Municipio'], shadow = False, colors=colors,
        startangle = 90, autopct = '%1.1f%%')
plt.axis("equal")
plt.title('Instituciones educativas con puntaje C por municipio para el año 2019')
plt.tight_layout()
plt.show()

#Figura que compara la grafica de dos años 
fig, ax = plt.subplots()
ax.plot(data["INSTITUCION EDUCATIVA"], data["AÑO 2019"], label = '2019')
ax.plot(data["INSTITUCION EDUCATIVA"], data["AÑO 2018"], label = '2018')
ax.set_xlabel('Colegios')
ax.set_ylabel('Puntajes')
ax.set_title("Puntajes 2018-2019 de todas las instituciones educativas")
ax.set_yticklabels(['','NR','D','C','B','A','A+'])
ax.legend()
plt.show()

#Mostrando los datos de dos años en graficas distintas
plt.figure(figsize = (15, 5))
plt.subplot(131)
plt.plot(data["INSTITUCION EDUCATIVA"], data["AÑO 2017"], color = 'green')
plt.title('Puntajes año 2017 de todas las instituciones')
plt.yticks(np.arange(6), labels = ('NR','D','C','B','A','A+'))

plt.subplot(132)
plt.plot(data["INSTITUCION EDUCATIVA"], data["AÑO 2018"], color = 'red')
plt.title('Puntajes año 2018 de todas las instituciones')
plt.yticks(np.arange(6),labels = ('NR','D','C','B','A','A+'))
plt.show()


#Figura que muestra la cantidad de colegios que hay por calificación 
fig, ax = plt.subplots()
x = np.arange(12) # la cantidad de municipios
ancho = 0.15  # tamaño de las barras
# Seteo de cada barra
ax.bar(x - ancho/.33, np.array(notMun['A+']), ancho, color = '#5DD2BC', label='A+')
ax.bar(x - ancho/.5, np.array(notMun['A']), ancho, color = '#CC6B27', label='A')
ax.bar(x - ancho, np.array(notMun['B']), ancho, color = '#706A99', label='B')
ax.bar(x, np.array(notMun['C']), ancho, color = '#4B93FF', label='C')
ax.bar(x + ancho, np.array(notMun['D']), ancho, color = '#FFB217', label='D')
ax.bar(x + ancho/.5, np.array(notMun['NR']), ancho, color = '#A1373D', label='No reporta')
# Titulos, leyenda y rejilla
ax.set_ylabel('Número de colegios')
ax.set_xlabel('Municipio')
ax.set_title('Calificación de los colegios en los departamentos de Risaralda año 2019')
ax.set_xticks(x)
ax.set_xticklabels(notMun['Municipio'])
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
ax.legend()
fig.tight_layout()
plt.show()
del x, ancho, a, aa, b, c, d, fila, indice_fila, mun, nr

#Calculo de medias
print("Media 2019")
clasificar(round(st.mean(data["AÑO 2019"])))

print("Media 2014")
clasificar(round(st.mean(data["AÑO 2014"])))
print('')

#Calculo de mediana
print("Mediana 2019")
clasificar(round(st.median(data["AÑO 2019"])))

print("Mediana 2018")
clasificar(round(st.median(data["AÑO 2018"])))
print('')

#mediana datos agrupados
print("Mediana datos agrupados")
clasificar(round(st.median_grouped(data["AÑO 2019"])))
print('')

#varianza
print("Varianza de datos 2019")
clasificar(round(st.variance(data["AÑO 2019"])))

print("Varianza de datos 2014")
clasificar(round(st.variance(data["AÑO 2014"])))
