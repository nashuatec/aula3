
    
nome =input('Digite seu nome : ')
sobrenome = input('Digite seu sobrenome filhote: ')
print('olá', nome , sobrenome, 'seja bem vindo vamos fazer umas contas')
print("**************************************************************")
numero1 = float(input("Digite o primeiro valor : "))
numero2 = float(input("digite o segundo valor :"))
resultado = (numero1 + numero2)
print(nome, 'O Resultado da sua conta é ' , resultado)
print("****************************************************************")
print("legal agora vamos calcular sua media final")
nota1 = float(input("Digite a primeira nota mano : "))
nota2 = float(input("Digite a segunda nota mano: " ))
nota3 = float(input("Digite a terceira nota mano : "  ))

resultado_final = (nota1 + nota2 + nota3)/3 
print(f"certo" , nome, "o resultado final ehh " , resultado_final)
print("*****************************************************************")
input("Agora para finalizar vamos calcular a area de um retangulo, APERTE ENTER PARA CONTINUAR")
largura = float(input("digite a largura do rentanglu : "))
altura = float(input("digite a altura do retanglu : "))
area = (largura * altura)
print("Prontinho a area desta retanglu imaginal ehh ", area,  "m2")
