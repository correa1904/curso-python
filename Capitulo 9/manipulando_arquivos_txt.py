

meu_arquivo = open('meu_texto.txt', 'a')

meu_arquivo.write('meu arquivo teste')

meu_arquivo.close()

with open('meu_texto.txt', 'a') as file:

    file.writelines(['\nLinha 1', '\nlinha 2', '\nTchau!'])