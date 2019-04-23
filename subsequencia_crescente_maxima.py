def subsequencia_crescente_maxima(arr):

    #Cria um dicionario para ir salvando as maiores subsequencias
    subsequencia = dict()
    for i in range(0, len(arr)):
        subsequencia[i] = []
    subsequencia[0] = [arr[0]]

    #Usando o método de memorização para acessar as melhores subsequencias ja conhecidas o algoritmo fica mais eficiente
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] >= arr[j] and (len(subsequencia[i]) < len(subsequencia[j]) + 1):
                subsequencia[i] = subsequencia[j]
        subsequencia[i] = subsequencia[i] + [arr[i]]
    maxima = subsequencia[0]
    
    for i in range(0, len(subsequencia)):
        if len(subsequencia[i]) > len(maxima):
            maxima = subsequencia[i]

    return maxima

#Testes
print()

arr = [10, 22, 9, 33, 21, 50, 41, 60] 
print("Array:", arr)
print("Subsequência Crescente Máxima:", subsequencia_crescente_maxima(arr))
print()

arr = [9, 1, 2, 8, 3, 4]
print("Array:", arr)
print("Subsequência Crescente Máxima:", subsequencia_crescente_maxima(arr))
print()

arr = [9, 5, 6, 3, 9, 6, 4, 7]
print("Array:", arr)
print("Subsequência Crescente Máxima:", subsequencia_crescente_maxima(arr))
print()

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print("Array:", arr)
print("Subsequência Crescente Máxima:", subsequencia_crescente_maxima(arr))
print()
