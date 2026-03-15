#Aprendendo path lib
from pathlib import Path
from shutil import rmtree

#para em um caminho relativo, ou seja, a pasta onde o arquivo está localizado
caminho = Path()
print(caminho.absolute())



#pasta absoluta - todo o caminho do arquivo
caminho2 = Path(__file__)
print(caminho2.absolute())


#pasta mãe
print(caminho2.parent)

#gerando um caminho

caminho3 = caminho2.parent / 'teste' / 'teste2' / 'teste3'
print(caminho3)


#home no disco local c
bundaArquivo = Path.home() / 'Desktop' / 'teste.txt'

bundaArquivo.touch() #cria o arquivo teste.txt
bundaArquivo.write_text('bunda') #escreve no arquivo teste.txt
print ('Conteúdo do arquivo teste.txt: ', bundaArquivo.read_text()) #lê o conteúdo do arquivo teste.txt

print(Path.home() / 'Desktop' / 'teste.txt')

#para apagar o arquivo
bundaArquivo.unlink()


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#abrindo o arquivo teste.txt com multiplas linhas

caminho_arquivo = Path.home() / 'Desktop' / 'bundinha.txt'
with caminho_arquivo.open('w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.write('linha 3\n')

print (caminho_arquivo.read_text())

caminho_arquivo.unlink()

#-----------------------------------------------------------------------------------------------------

#criando pasta

hiropasta = Path.home() / 'Desktop' / 'hiropasta' 
hiropasta.mkdir(exist_ok=True) #cria a pasta hiropasta
subhiro = hiropasta / 'subhiro'
subhiro.mkdir(exist_ok=True) #cria a pasta subhiro dentro da pasta hiropasta

textohiro = subhiro / 'textohiro.txt'
textohiro.touch() #cria o arquivo textohiro.txt dentro da pasta subhiro
with textohiro.open('w') as arquivo:
    arquivo.write('Olá, este é o arquivo textohiro.txt!\n') #escreve no arquivo textohiro.txt
    arquivo.write('cala a boca, hiropasta é vida!\n')

print (textohiro.read_text()) #lê o conteúdo do arquivo textohiro.txt

rmtree(hiropasta) #apaga a pasta hiropasta e todo o seu conteúdo