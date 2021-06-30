from pomegranate import *

#Definição da probabilidade inicial
inicio =  DiscreteDistribution({
    "sol": 0.9,
    "chuva": 0.1
})
#Definição das transições
transicoes = ConditionalProbabilityTable([
    ["sol", "sol", 0.9],
    ["sol", "chuva", 0.1],
    ["chuva", "sol", 0.8],
    ["chuva", "chuva", 0.2]
], [inicio])

#Instancia do Cadeia de Markov
modelo_Markov = MarkovChain([inicio, transicoes])

#Amostras pela função do pomegranate
amostras = modelo_Markov.sample(100)
#Quantidade de amostras geradas
quantidade_de_amostras = len(amostras)
#Variaveis para guardar quantidade de momentos
# chuva após chuva
# sol após chuva
# sol após sol
# chuva após sol
chuva_chuva = 0
chuva_sol = 0
sol_sol = 0
sol_chuva = 0 


print("=====================================================================================")
print("==============================Imprimindo 100 amostras================================")
print("=====================================================================================")
print(amostras)
print("=====================================================================================")
print("=========================Imprimindo quantidade de momentos===========================")
print("=====================================================================================")
#Loop que verifica as ocorrencias dos momentos
for i in range(quantidade_de_amostras):
    if(i+1 != quantidade_de_amostras):
        if amostras[i] == "chuva" and amostras[i+1] == "chuva":
            chuva_chuva = chuva_chuva + 1 
        elif amostras[i] == "chuva" and amostras[i+1] == "sol":
            chuva_sol = chuva_sol + 1
        elif amostras[i] == "sol" and amostras[i+1] == "sol":
            sol_sol = sol_sol + 1
        elif amostras[i] == "sol" and amostras[i+1] == "chuva":
            sol_chuva = sol_chuva + 1
print(f'Quantidade de momentos em que tivemos chuva seguido de chuva: {chuva_chuva}')
print(f'Quantidade de momentos em que tivemos sol após chuva : {chuva_sol}')
print(f'Quantidade de momentos em que tivemos sol após sol: {sol_sol}')
print(f'Quantidade de momentos em que tivemos chuva após sol: {sol_chuva}')
print("=====================================================================================")
print("================Imprimindo Porcentagem de ocorrencia dos momentos====================")
print("=====================================================================================")
print(f'Porcentagem de momentos em que tivemos chuva seguido de chuva: {(chuva_chuva/quantidade_de_amostras)*100} %')
print(f'Porcentagem de momentos em que tivemos sol após chuva : {(chuva_sol/quantidade_de_amostras)*100} %')
print(f'Porcentagem de momentos em que tivemos sol após sol: {(sol_sol/quantidade_de_amostras)*100} %')
print(f'Porcentagem de momentos em que tivemos chuva após sol: {(sol_chuva/quantidade_de_amostras)*100} %')
print("=====================================================================================")
