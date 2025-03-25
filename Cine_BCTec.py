def cadastro_filmes():
    filmes = [["Fuga das galinhas", "Comédia e aventura", 90, "As galinhas fogem de um galinheiro"]
              ,["Vingadores", "Ação e aventura", 120, "Os heróis mais fortes da terra"]]
    
    return filmes

def assentos(qtd):
    assentos = [True] * qtd
    return assentos

def dados_sessoes(filmes):
    sessoes = [[filmes[0], "24/03/2025", "18:00", 20, "Básica", assentos(20)],
               [filmes[1], "24/03/2025", "18:00", 25, "XD", assentos(20)],
               [filmes[0], "24/03/2025", "20:00", 30, "Super Confortável", assentos(15)],
               [filmes[1], "24/03/2025", "20:30", 40, "Luxo", assentos(10)]]
    return sessoes

def assentos_disponiveis(sessao):
    id = 1
    disponiveis = []
    for i in range(len(sessao[5])):
        if(sessao[5][i] == True):
            disponiveis.append(id)
        id += 1
    return disponiveis


def reservar_assento(sessao, id_assento):
    confirma_reserva = True
    if sessao[5][id_assento - 1]:
        sessao[5][id_assento-1] = False
        print(f"Assento {id_assento} foi reservado!")
    else:
        print(f"Assento {id_assento} reservado ou inválido, por favor selecione outro assento")
        confirma_reserva = False

    return confirma_reserva
def calcula_valor(sessao):
    sala = sessao[4]
    valor_calculado = sessao[3]
    
    if sala == "Básica":
        valor_calculado = valor_calculado
    elif sala == "XD":
        valor_calculado *= 1.1
    elif sala == "Super Confortável":
        valor_calculado *= 1.12
    elif sala == "Luxo":
        valor_calculado *= 1.15
    return valor_calculado

def brinde(sessao):
    brinde = ""
    if sessao[4] == "Básica":
        brinde = "Sem brinde"
    elif sessao[4] == "XD":
        brinde = "Bonequinho do BCTec"
    elif sessao[4] == "Super Confortável":
        brinde = "Bonequinho do BCTec, mais um combo de pipoca"
    elif sessao[4] == "Luxo":
        brinde = "Bonequinho doBCTec, mais umcombo de pipoca, refrigerante e chocolate"
    return brinde 

def comprovante_bilhete(sessao, assentos_reservados, quantidade, metodo_pagamento):
    lucro = calcula_valor(sessao) * quantidade
    brinde_selecionado = brinde(sessao)
    
    print("\n---------BILHETE--------- \n")
    print(f"Filme:  {sessao[0][0]}")
    print(f"Assento: {assentos_reservados}")
    print(f"Data: {sessao[1]}")
    print(f"{sessao[2]}")
    print(f"Valor total: R$ {lucro:.2f}")
    print(f"Forma de pagamento: {metodo_pagamento}")
    print(f"Brinde: {brinde_selecionado}")
    print("BOM FILME =)")
    
    
print("BEM VINDO AO Cine BCTec")

filmes = cadastro_filmes()   
sessoes = dados_sessoes(filmes)

continuar = "sim"

while(continuar == "sim"):
    assentos_reservados = []
    quantidade_de_ingressos = 0

    print("Sessões disponíveis no catálogo: ")
   
    for sessao in sessoes:
        print(f"{sessao[0][0]} - {sessao[1]} às {sessao[2]} - Sala: {sessao[4]}")
    sessao_id = -1
    sessao_id = int(input("Escolha uma sessão(1 - 4): "))
    
    while(sessao_id < 1 or sessao_id > 4):
        sessao_id = int(input("Por favor, escolha um número entre 1 e 4"))
    
    sessao_User = sessoes[sessao_id-1]
        
    print("ótimo! Agora escolha um assento disponível: ")
    
    
    pedido = "sim"
    
    while(pedido == "sim"):
        
        
        print(assentos_disponiveis(sessao_User))
        assento_definido = int(input("Escolha seu número de assento: "))
        
        if(reservar_assento(sessao_User, assento_definido)):
            quantidade_de_ingressos += 1
            assentos_reservados.append(assento_definido)
        pedido = input("Deseja continuar reservando assentos?(sim ou nao) ")   
        
    metodo_pagamento = input("Por favor, escolha a forma de pagamento(PIX, Dinheiro, Débito ou Crédito): ")
    
    comprovante_bilhete(sessao_User, assentos_reservados, quantidade_de_ingressos, metodo_pagamento )
    continuar = input("\nContinuar compra(sim ou não): ")