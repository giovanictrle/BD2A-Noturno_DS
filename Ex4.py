import os
texto = input('Informe um texto:')

#Criar arquivo no diretório corrente
cwd = os.path.abspath('Ex4.txt')
arq = open(cwd,'w')
arq.writelines(texto)
arq.close()

#Criar arquivo no diretório corrente
cwd2 = os.path.abspath('Ex4_copia.txt')
arq2 = open(cwd2,'w')

#Abre o arquivo criado com o texto e popula o segundo arquivo com o texto
arq = open(cwd,'r')
for linha in arq:
    arq2.writelines(linha)
arq2.close()

print('Fim do Processo')




