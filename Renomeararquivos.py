import os
pasta = str(input('Informe o caminho da pasta: ')+'\\')
print(pasta)
teste = 1
for contagem in range(teste):
        for caminho in os.listdir(pasta):
            try:
                        contagem = contagem + 1
                        nomeantigo = pasta + caminho
                        nomeatual = pasta  +str(contagem)+"-"+ caminho
                        os.rename(nomeantigo,nomeatual)
                        print(os.listdir(pasta))
            except:
                print('Ocorreu um Erro na execução')

