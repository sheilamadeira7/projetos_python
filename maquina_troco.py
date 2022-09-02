# Programa - Máquina de Troco
# Troco com o menor número possível de notas e moedas

from decimal import Decimal

compra = Decimal(input("Informe o valor da compra: R$ "))
dinheiro = Decimal(input("Informe o valor pago: R$ "))
troco = Decimal(dinheiro - compra)
print("O valor do troco é: R$ ", +troco)

Lista = ["200", "100", "50", "20", "10", "5", "2", "1", "0.50", "0.25", "0.10", "0.05", "0.01"]
for valor in Lista:

    calculo = int(troco / Decimal(valor))
    troco = troco - (calculo*Decimal(valor))
    print("Troco no valor de: R$"+valor, ", quantidade = ",calculo)

