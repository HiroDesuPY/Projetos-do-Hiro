#contador de calorias por dia!

escolha = False
listacomida = {}
resposta = ['sim','não','nao']
resultadokcal = 0


def menos():    
    result = abs(kcal) + 2000 
    return result

while True:
    nome = input("O que você comeu? ").lower().strip()
    kcal = float(input("Quantos kcal: "))

    resultadokcal += kcal

    if nome in listacomida:
        listacomida[nome]["quantidade"] += 1
        listacomida[nome]["calorias"] += kcal
    else:
        listacomida[nome] = {"quantidade": 1, "calorias": kcal}



    if kcal < 0:
        kcal = menos()

    
    escolha_usu = input("Você quer sair? sim ou não? sim ou não?").lower().strip()


    if escolha_usu == 'sim':
        print("="*30)
        print("Obrigado por usar o software!")
        print("="*30)
        break



    elif escolha_usu not in resposta:
        print ('*'*30)
        print("Faça escolha certa!")
        escolha_usu = input("Você quer sair? sim ou não?").lower().strip()
        print ('='*30)


    elif escolha_usu == 'não' or escolha_usu == 'nao':
        continue





print ('='*30)
if resultadokcal > 2000:
    print (f"Você ultrapassou o limite! {resultadokcal:.2f} kcal")

else:
    print(f"Você não passou o limite! Parabéns :D!!!  {resultadokcal:.2f} kcal")

for nome, dados in listacomida.items():
     print(f"{nome}: {dados['quantidade']} vez(es) - {dados['calorias']:.2f} kcal")


print (listacomida)




    

            
        




        


    