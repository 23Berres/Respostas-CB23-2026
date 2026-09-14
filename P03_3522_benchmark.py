import AP_03_ordenacao as ord
import random as rd
import time as tm
import sys

sys.setrecursionlimit(10002)

def caso_medio(beta = "Quantidade de elementos da lista"):
    """Retorna uma lista aleatória a ser ordenada.
    
    
    Ao ser chamada com o parâmetro quantidadede elementos N da lista, 
    a função retorna uma lista com N elementos (podendo repetir).
    O elementos estão entre 0 e 10.000."""


    return rd.choices(range(10001),k=beta)

def pior_caso(beta = "Quantidade de elementos da lista"):
    """Retorna a pior lista a ser ordenada.
    
    Uma lista regressiva com N elementos, de um em um.
    Os elementos estão entre N e 0"""
    return list(range(beta,-1,-1))

def pior_caso_merge(beta):
    """Gera o verdadeiro pior caso para o Merge Sort."""
    def separar(lista):
        if len(lista) <= 1:
            return lista
        esquerda = lista[0::2]
        direita = lista[1::2]
        return separar(esquerda) + separar(direita)
    lista_ordenada = list(range(beta))
    return separar(lista_ordenada)

funcoes = {"1": ord.selection_sort,
           "2": ord.divide_and_conquer_sort,
           "3": ord.quick_sort}


k = 50


selection_s = {"100":[0,0,0,0],
                  "500":[0,0,0,0],
                  "1000":[0,0,0,0],
                  "5000":[0,0,0,0],}
                  
merge_s = {"100":[0,0,0,0],
                  "500":[0,0,0,0],
                  "1000":[0,0,0,0],
                  "5000":[0,0,0,0],}

quick_s = {"100":[0,0,0,0],
                  "500":[0,0,0,0],
                  "1000":[0,0,0,0],
                  "5000":[0,0,0,0],} 

betas = [100,500,1000,5000]
algoritmos = [selection_s, merge_s, quick_s]

for i in range(1,4):
    funcao = funcoes[f"{i}"]
    internacional = algoritmos[i-1]
    for beta in betas:
        for j in range(2):
            if j ==0:
                for algo in range(k):

                    lista = caso_medio(beta)
                    tempo_inicial = tm.perf_counter()
                    funcao(lista)
                    tempo_final = tm.perf_counter()

                    tempo_modular = tempo_final-tempo_inicial
                    internacional[f"{beta}"][0] += tempo_modular
                internacional[f"{beta}"][1] = f"{(internacional[f'{beta}'][0]/k):.6f}"
            else:
                if i != 2:
                    for algo in range(k):

                        lista = pior_caso(beta)
                        tempo_inicial = tm.perf_counter()
                        funcao(lista)
                        tempo_final = tm.perf_counter()

                        tempo_modular = tempo_final-tempo_inicial
                        internacional[f"{beta}"][2] += tempo_modular
                    internacional[f"{beta}"][3] = f"{(internacional[f'{beta}'][2]/k):.6f}"
                else:
                    for algo in range(k):

                        lista = pior_caso_merge(beta)
                        tempo_inicial = tm.perf_counter()
                        funcao(lista)
                        tempo_final = tm.perf_counter()

                        tempo_modular = tempo_final-tempo_inicial
                        internacional[f"{beta}"][2] += tempo_modular
                    internacional[f"{beta}"][3] = f"{(internacional[f'{beta}'][2]/k):.6f}"

selection = {"Algoritmo": ["Selection Sort","Selection Sort","Selection Sort","Selection Sort","Selection Sort","Selection Sort","Selection Sort","Selection Sort"],
         "N": [100,500,1000,5000,100,500,1000,5000],
         "Cenário": ["caso médio","caso médio","caso médio","caso médio","pior caso","pior caso","pior caso","pior caso"],
         "Tempo Médio (s)":[selection_s["100"][1],selection_s["500"][1],selection_s["1000"][1],selection_s["5000"][1],
                            selection_s["100"][3],selection_s["500"][3],selection_s["1000"][3],selection_s["5000"][3]]}

merge = {"Algoritmo": ["Merge Sort","Merge Sort","Merge Sort","Merge Sort","Merge Sort","Merge Sort","Merge Sort","Merge Sort"],
         "N": [100,500,1000,5000,100,500,1000,5000],
         "Cenário": ["caso médio","caso médio","caso médio","caso médio","pior caso","pior caso","pior caso","pior caso"],
         "Tempo Médio (s)":[merge_s["100"][1],merge_s["500"][1],merge_s["1000"][1],merge_s["5000"][1],
                            merge_s["100"][3],merge_s["500"][3],merge_s["1000"][3],merge_s["5000"][3]]}

quick = {"Algoritmo": ["Quick Sort","Quick Sort","Quick Sort","Quick Sort","Quick Sort","Quick Sort","Quick Sort","Quick Sort"],
         "N": [100,500,1000,5000,100,500,1000,5000],
         "Cenário": ["caso médio","caso médio","caso médio","caso médio","pior caso","pior caso","pior caso","pior caso"],
         "Tempo Médio (s)":[quick_s["100"][1],quick_s["500"][1],quick_s["1000"][1],quick_s["5000"][1],
                            quick_s["100"][3],quick_s["500"][3],quick_s["1000"][3],quick_s["5000"][3]]}

print(f"{'Resultado das análises':^22}\n---------------------------------------------------------")
print(f"{'Algoritmo':<15} | {'N':<6} | {'Cenário':<12} | {'Tempo Médio (s)':>15}")
print("-" * 57)

dicionarios = [selection, merge, quick]

for dic in dicionarios:
    for i in range(len(dic["Algoritmo"])):
        algo = dic["Algoritmo"][i]
        n = dic["N"][i]
        cenario = dic["Cenário"][i]
        tempo = dic["Tempo Médio (s)"][i]
        
        print(f"{algo:<15} | {str(n):<6} | {cenario:<12} | {tempo:>15}")