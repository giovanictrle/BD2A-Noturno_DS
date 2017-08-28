"""Diego Alcantara  RA 1700531
Giovani Carneiro RA 1700709
Gabriel Alex     RA 1700781  
Liber Ferraz     RA 1700235"""

def exe_1 ():
    vt = []
    i=0
    while i <30:
        n=int(input("Digite o valor o número desejado: "))
        vt.insert(i,n)
        i+=1
    print(vt)
    qtd = len(vt)
    i=0
    while i < qtd:
        if(vt[i]<0):
           vt[i]=0
        else:
           vt[i]=1
        i+=1
    print(vt)
exe_1()
    
