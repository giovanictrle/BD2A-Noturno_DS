def vptrocados(vet):
    for x in range(20):

        if vet[x] >= 0 and vet[x] <= 10:
            vet[x]= 1
        elif vet [x] < 0:
                vet[x] = 0
        elif vet [x] > 10:
                vet[x] = 2
    return vet



vet = [0]*20
for x in range (20):
    vet[x] = int (input ("Digite um numero : "))
print (vet)
vptrocados(vet)
print (vet)
