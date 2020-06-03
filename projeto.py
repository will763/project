
import matplotlib.pyplot as plt

# variáveis

paises=('Brasil','Argentina','Chile','Uruguai','Colombia')
mortes = (11163,3073,1838,630,2332)
indice =(0,1,2,3,4)
anos = (2010,2011,2012,2013,2014,2015)
mpa = (9429, 9822, 10295,10513,10631, 11163)

#Gráfico de colunas

plt.bar(indice,mortes)
plt.xticks(indice,paises)
plt.ylabel("Número de Mortes")
plt.title("Mortes por suicídio 2015")
plt.show()

#Gráfico de linha

plt.plot(anos,mpa)
plt.title('Mortes por suicídio')
plt.ylabel('Mortes')
plt.xlabel("Linha do tempo")
plt.show()

#Gráfico de setores

plt.pie(mortes,labels= paises, autopct='%1.f%%')
plt.title("Frequência de mortes por suicídio 2015")
plt.show()