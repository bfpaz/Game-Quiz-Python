
lista = []

def ler_perguntas():
    arq = open("perguntas.txt", "r")
    arquivo = arq.read()
    arquivo = arquivo.split('\n')
    #print(arquivo)
    for x in arquivo:
        #print(x)
        lista.append(x.split(";"))
    #print(lista)

def iniciar_jogo():
    respostas_certas = 0
    for x in range(0, len(lista)):
        perguntas = {
            f'Q{x+1}.': {
                'pergunta': lista[x][0],
                'respostas': {
                    'a': lista[x][1],
                    'b': lista[x][2],
                    'c': lista[x][3],
                    'd': lista[x][4],
                    'e': lista[x][5]},
                'resposta_certa': lista[x][6]
            },
        }
        for pk, pv in perguntas.items():
            print(f'{pk}: {pv["pergunta"]}')
            for rk, rv in pv['respostas'].items():
                print(f'{rk}) {rv}')
            print()
            resp_user = input("Sua resposta: ")
            if resp_user.lower() == pv['resposta_certa']:
                print("RESPOSTA CERTA!")
                respostas_certas += 1
            else:
                print("VOCÊ ERROU!")
            print()
    qtd_perguntas = len(lista)
    aproveitamento = respostas_certas / qtd_perguntas * 100
    print(f"VOCÊ ACERTOU {respostas_certas} PERGUNTAS E TEVE {aproveitamento}% DE APROVEIRAMENTO.")

ler_perguntas()
iniciar_jogo()
