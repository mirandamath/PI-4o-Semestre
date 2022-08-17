#IMportando Modulo em Python
import conversaoFeetToMeters #tambem podemos "fazer from conversaoFeetToMeters import FeetToMeter" para importar funcoes especificas

#Nao Precisa colocar o tipo antes da variavel (tipagem dinamica)
option = None

while option != "3":
    option = input("Qual sua opção de conversão ?\n1 - Pés para Metros\n2 - Metros para Pés\n3 - Sair\n")
    if option == "1":
        value = input("Qual valor deseja converter ?\n")
        res = conversaoFeetToMeters.FeetToMeter(float(value))
        print("Resultado: " + str(res) + " metros\n")
    elif option == "2":
        value = input("Qual valor deseja converter ?\n")
        res = conversaoFeetToMeters.MeterToFeet(float(value))
        print("Resultado: " + str(res) + " pés")
    elif option == "3":
        print("Tchau !")
    else:
        print("Escolha invalida!")
