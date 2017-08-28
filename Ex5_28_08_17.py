import os

#Cria o arquivo no diretório 
cwd = os.path.abspath('Ex5.txt') 
arq = open(cwd,'w')

#Escrevendo no arquivo
#\n pular linha
texto = []
texto.append('ACME Inc.           Uso do espaço em disco pelos usuários\n')
texto.append('---------------------------------------------------------\n')
texto.append('Nr.    Usuário          Espaço utilizado         % do uso\n')
texto.append('\n')
texto.append('1      alexandre            434,99 MB              16,85%\n')
texto.append('2      anderson            1187,99 MB              46,02%\n')
texto.append('3      antonio              117,73 MB               4,56%\n')
texto.append('4      carlos                87,03 MB               3,37%\n')
texto.append('5      cesar                  0,94 MB               0,04%\n')
texto.append('6      rosemary             752,88 MB              29,16%\n')
texto.append('Espaço total ocupado: 2581,57 MB\n')
texto.append('Espaço médio ocupado: 430,26 MB\n')
arq.writelines(texto)
arq.close()
