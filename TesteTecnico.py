from random import randint

def ehPrimo(num):
    
    if num > 1:
        return all(num % i for i in range(2, num))
    else:
        return False

def primeiroDesafio(lista):
    print ("Primeiro Desafio")
    
    procurar = input("Digite o numero que deseja achar :")
    
    if int(procurar) in lista :
        print ('O numero %s esta na lista' %(int(procurar)))
    else :
        print ('O numero %s nao esta na lista' %(int(procurar)))
            
        
primeiroDesafio(sorted([randint(0, 300) for x in range(300)])) 

def segundoDesafio(lista1, lista2):
    
    print ("Segundo Desafio")
    
    intersec = set(lista2).intersection(lista1)
    
    print(intersec)


segundoDesafio([randint(0, 5000000) for x in range(500)],  [randint(0, 5000000) for x in range(50000)])

def terceiroDesafio():
    
    print("Terceiro desafio")
    num = input("Digite o numero desejado")
    num = int(num)
    i = 2
    
    while i <= num:
        if(ehPrimo(i)):
            print (i)
        i+= 1

terceiroDesafio()

def quartoDesafio():
    print("Quarto Desafio")
    
    palavra = input("Digite a palavra desejada: ")
    soma = 0;
    
    for char in palavra:
        if char.isupper():
            soma += ord(char) - 38
        else :
            soma+= ord(char) - 96    
    
    if ehPrimo(soma):
        print("%s eh uma palavra prima" %(palavra))
    else :
        print("%s nao eh uma palavra prima" %(palavra))

   

quartoDesafio()