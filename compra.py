import time

preço = int(input("Digite o valor do produto: \n\n"))

forma = int(input("De que forma você gostaria de pagar: \n[1] á vista\n\n[2] parcelado\n\n"))

print ("carregando...\n\n")
time.sleep(3)

if forma == 1:

    preço = preço - preço*10/100

    print ("Você ganhou um desconto de 10%!!!\n\n")
    time.sleep(1)
    print (f"O preço final é R${preço}\n\n")

else:

    print ("Você pode parcela em no máximo 15x\n\n")
    time.sleep(1)
    vezes = int(input("Em quantas vezes deseja: \n\n"))
    print ("carregando...\n\n")
    time.sleep(3)

    preço = preço/vezes

    print (f"O valor ficou em {vezes}x de R${preço} \n\n")