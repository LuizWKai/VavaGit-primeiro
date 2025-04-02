import random

while True:
    print("Bem vindo ao sorteio de agentes do Valorant!")

    agente1 = "Viper"
    agente2 = "Sova"
    agente3 = "Breach"
    agente4 = "Brimstone"
    agente5 = "Omen"
    agente6 = "Phoenix"
    agente7 = "Jett"
    agente8 = "Raze"
    agente9 = "Reyna"
    agente10 = "Sage"
    agente11 = "Cypher"
    agente12 = "Killjoy"
    agente13 = "Skye"
    agente14 = "Yoru"
    agente15 = "Astra"
    agente16 = "Iso"
    agente17 = "KAY/O"
    agente18 = "Chamber"
    agente19 = "Neon"
    agente20 = "Deadlock"
    agente21 = "Harbor"
    agente22 = "Gekko"
    agente23 = "Tejo"
    agente24 = "Clove"
    agente25 = "Fade"

    Smolk = [agente1, agente4, agente5, agente15, agente21, agente24]
    Duelista = [agente6, agente7, agente8, agente9, agente14, agente16, agente19]
    Iniciador = [agente2, agente3, agente13, agente17, agente22, agente25, agente23]
    Sentinela = [agente10, agente11, agente12, agente18, agente20]
    agente = [agente1, agente2, agente3, agente4, agente5, agente6, agente7, agente8, agente9, agente10, agente11, agente12, agente13,
            agente14, agente15, agente16, agente17, agente18, agente19, agente20, agente21, agente22, agente23, agente24, agente25]


    Smolk1 = random.choice(Smolk)
    Smolk.remove(Smolk1)
    agente.remove(Smolk1)  # Remove o agente escolhido da lista de agentes

    Duelista1 = random.choice(Duelista)
    Duelista.remove(Duelista1)
    agente.remove(Duelista1)  # Remove o agente escolhido da lista de agentes

    Iniciador1 = random.choice(Iniciador)
    Iniciador.remove(Iniciador1)
    agente.remove(Iniciador1)  # Remove o agente escolhido da lista de agentes

    Sentinela1 = random.choice(Sentinela)
    Sentinela.remove(Sentinela1)
    agente.remove(Sentinela1)  # Remove o agente escolhido da lista de agentes

    Agente1 = random.choice(agente)
    agente.remove(Agente1)  # Remove o agente escolhido da lista de agentes

    print()

    Pickados = [Agente1, Iniciador1, Sentinela1, Smolk1, Duelista1]

    quantidade = int(input("Quantas pessoas vão jogar? "))

    while quantidade > 5:
        print("Tu ta de sacanagem, né?")
        quantidade = int(input("Quantas pessoas vão jogar poha? "))

    pessoas = []
    i = 1
    while i <= quantidade:
        pessoa = input(f"Nome do jogador {i}: ")
        pessoas.append(pessoa)
        i += 1

    print()

    i = 1
    j = 1
    while j <= quantidade:
        for i in range(len(pessoas)):
            print(f"{pessoas[i]} vai jogar de {Pickados[i]}")
            i += 1
            j += 1

    print()
