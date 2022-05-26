lista1 = [2, 3, 4, 5, 1]
lista2 = [2, 1, 4, 5, 3]
#      = [0, 1, 2, 3, 4]

tentativas = 0
tentativas2 = 0

if lista2 != lista1:
    lista2[4] = 5
    lista2[3] = 3
    lista2[1] = 4
    lista2[2] = 1
    tentativas = tentativas + 1

    lista1[4] = 5
    lista1[3] = 1
    lista1[2] = 3
    lista1[1] = 4
    tentativas2 = tentativas2 + 1
# [2, 4, 1, 3, 5]
# [0, 1, 2, 3, 4]

    lista2[2] = 3
    lista2[3] = 1
    tentativas = tentativas + 1

    lista1[2] = 1
    lista1[3] = 3
    tentativas2 = tentativas2 + 1

# [2, 4, 3, 1, 5] 
# [0, 1, 2, 3, 4]

    lista2[4] = 1
    lista2[3] = 5
    lista2[2] = 4
    lista2[1] = 3
    tentativas = tentativas + 1

    lista1[1] = 1
    lista1[2] = 4
    tentativas2 = tentativas2 + 1

# [2, 1, 4, 5, 3] 
# [0, 1, 2, 3, 4]

    lista1[3] = 5
    lista1[4] = 3
    tentativas2 = tentativas2 + 1


print(lista2, "\ntentativas", tentativas)
print(lista1, "\ntentativas", tentativas2)