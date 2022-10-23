import matplotlib.pyplot as plt  #importação da biblioteca

progressao = 0# valor inicial da progressão geometrica ()
razao = 0.5# razão da progressao geometrica
voltas = 5 # contador de "meias voltas" define o número de linhas da espiral

x = []
y = []

#ambas as listas iniciam com o valor inicial da progressão

# colagem dos valores iniciais independente do ponto de partida da progressão
x.append(progressao)
x.append(progressao) # o eixo x deve ter o primeiro valor duplicado
y.append(progressao)

if (progressao == 0): # caso o valor inicial da progressao for 0 devemos somar 2
    progressao += razao
else:
    progressao = (progressao*razao)*-1 # com o valor inicial diferente de zero podemos iniciar a inversão
y.append(progressao)

#após os valores iniciais colados podemos iniciar a repetição

for c in range(0, voltas + 1):
    x.append(progressao)
    x.append(progressao)
    y.append(progressao)
    progressao = (progressao *razao)*-1
    y.append(progressao)

plt.plot(x,y)
plt.show()

print(x,y)

