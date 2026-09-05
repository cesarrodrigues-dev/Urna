# Cadastrei primeiro os candidatos

Candidato1 = {
    "Nome": "César",
    "Numero": 10,
    "Votos": 0
}

Candidato2 = {
    "Nome": "João",
    "Numero": 22,
    "Votos": 0
}

Candidato3 = {
    "Nome": "Maria",
    "Numero": 13,
    "Votos": 0
}

Continuar = "Sim"

while Continuar == "Sim":

    # Mensagem de abertura da tela dos candidatos
    print("====== Escolha seu candidato ======\n")

    print(f"Nome: {Candidato1['Nome']} - Numero: {Candidato1['Numero']}")
    print(f"Nome: {Candidato2['Nome']} - Numero: {Candidato2['Numero']}")
    print(f"Nome: {Candidato3['Nome']} - Numero: {Candidato3['Numero']}\n")

    # Solicitação - eleitor escolhe o número do candidato
    Voto = int(input("Digite o numero do seu candidato:\n"))

    if Voto == Candidato1["Numero"]:
        Candidato1["Votos"] += 1
        print("Seu voto foi computado com sucesso!")

    elif Voto == Candidato2["Numero"]:
        Candidato2["Votos"] += 1
        print("Seu voto foi computado com sucesso!")

    elif Voto == Candidato3["Numero"]:
        Candidato3["Votos"] += 1
        print("Seu voto foi computado com sucesso!")

    Continuar = input("Deseja continuar? Sim ou Não: ")


print("\n====== RESULTADO DA VOTAÇÃO ======")

print(f"{Candidato1['Nome']}: {Candidato1['Votos']} votos")
print(f"{Candidato2['Nome']}: {Candidato2['Votos']} votos")
print(f"{Candidato3['Nome']}: {Candidato3['Votos']} votos")


Vencedor = Candidato1

if Candidato2["Votos"] > Vencedor["Votos"]:
    Vencedor = Candidato2

if Candidato3["Votos"] > Vencedor["Votos"]:
    Vencedor = Candidato3

print(f"O vencedor é: {Vencedor['Nome']}")