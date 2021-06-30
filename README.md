# Modelo de Markov
Execução do modelo de Markov em situaçãoes meteorológicas fictícias.

### Saída da execução
* Quantidades de momentos meterológicos;
* Porcentagem de ocorrência desses momentos.

```OBS.: As probabilidades aqui encontradas são apenas fictícias para a possível execução do modelo.```
## Definição da suposição de Markov
O modelo de Markov é utilizado para realizar predições de eventos em um futuro. Portanto, sendo X um evento qualquer, X<sub>t</sub> é determinado como o evento atual e X<sub>t+1</sub> é determinado com o próximo evento. Sendo assim, a definição da suposição de Markov é uma suposição de que o estado atual depende somente de um número fixo e finito de estados anteriores. Um exemplo é a utilização de dados de ontem e de hoje para prever o clima de amanhã. Contudo, de acordo com o crescimento de dados anteriores a serem utilizados, o esforço computacional aumenta. Por conseguinte, a suposição de Markov limita esses dados anteriores para que a gerência desses dados seja mais fácil e o esforço computacional seja reduzido.

## Definição da cadeia de Markov
A cadeia de Markov é definida da seguinte maneira:
* A ocorrência do evento X<sub>t+1</sub> será com base na probabilidade do evento X<sub>t</sub>.
Em palavras mais técnicas, a cadeia de Markov é uma sequência de variáveis aleatórias em que a distribuição de cada variável segue a suposição de Markov.

## Definição de transição
Transição é a especificação das distribuições de probabilidade do evento X<sub>t+1</sub> com base nos valores possíveis do evento X<sub>t</sub> .  

## Requisitos para a execução do modelo
Para a execução deste modelo é necessário a instalação do pacote pomegranate.

```pip3 install pomegranate ```

## Execução do modelo
Para executar este modelo execute o arquivo `markov.py`

```python3 markov.py```
