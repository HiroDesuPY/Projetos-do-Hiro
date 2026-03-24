#lista de produtos:

def atualizando_lista(produto,valor):
    global lista
    lista[produto] = valor
    return lista

lista = {}

while True:
    prod = input("Qual o nome do produto?")
    val = float(input("Qual o valor do produto?"))

    if prod in lista:
        print(f"O produto {prod} já está dentro da lista")
        print(lista)
        escolha_usu = input("Deseja atualizar o valor do produto? (sim/não)").lower().strip()

        if escolha_usu[0] == "s":
            atualizando_lista(prod,val)
            continue

        if escolha_usu[0] == "n":
            print("Valor mantindo")
            print("\n" + "="*20)


        else:
            print('*'*30)
            escolha_usu = input("Faça escolha certa!").lower().strip()

    if prod not in lista:
        lista[prod] = val
        print(f"O produto {prod} foi adicionado à lista com o valor de R${val:.2f}")
        print(lista)

    escolha_usu = input("Deseja continuar? (sim/não)").lower().strip()

    
    if escolha_usu[0] == "s":
        continue

    if escolha_usu[0] == "n":
        break

    else:
        print('*'*30)
        
        escolha_usu = input("Faça escolha certa! ").lower().strip()




print('Lista atualizada:', lista)









