nome_missao = "Sem"
equipe = "Sem"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

dados_missao = [
    [25, 90, 85, 95, 88],
    [28, 82, 70, 92, 80],
    [32, 68, 55, 88, 72],
    [35, 52, 42, 84, 60],
    [38, 40, 30, 79, 48],
    [30, 65, 58, 86, 70]
]

def analisar_temperatura(valor):
    if valor < 18:
        return 1, "ATENÇÃO", "Temperatura abaixo do ideal"
    elif valor <= 30:
        return 0, "NORMAL", "Temperatura estável"
    elif valor <= 35:
        return 1, "ATENÇÃO", "Temperatura elevada"
    else:
        return 2, "CRÍTICO", "Risco de superaquecimento"

def analisar_comunicacao(valor):
    if valor < 30:
        return 2, "CRÍTICO", "Comunicação com a base em nível crítico"
    elif valor < 60:
        return 1, "ATENÇÃO", "Comunicação instável"
    else:
        return 0, "NORMAL", "Comunicação estável"

def analisar_bateria(valor):
    if valor < 20:
        return 2, "CRÍTICO", "Bateria em nível crítico"
    elif valor < 50:
        return 1, "ATENÇÃO", "Bateria abaixo do recomendado"
    else:
        return 0, "NORMAL", "Energia estável"

def analisar_oxigenio(valor):
    if valor < 80:
        return 2, "CRÍTICO", "Oxigênio em nível crítico"
    elif valor < 90:
        return 1, "ATENÇÃO", "Oxigênio abaixo do ideal"
    else:
        return 0, "NORMAL", "Oxigênio adequado"

def analisar_estabilidade(valor):
    if valor < 40:
        return 2, "CRÍTICO", "Estabilidade operacional crítica"
    elif valor < 70:
        return 1, "ATENÇÃO", "Estabilidade operacional reduzida"
    else:
        return 0, "NORMAL", "Estabilidade operacional adequada"

def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def recomendacao(risco):
    if risco <= 2:
        return "Manter operação normal e continuar monitoramento."
    elif risco <= 5:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

riscos = []
pontos_area = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)

print("Missão:", nome_missao)
print("Equipe:", equipe)
print("Quantidade de ciclos analisados:", len(dados_missao))

print("=" * 60)

for i in range(len(dados_missao)):

    temperatura = dados_missao[i][0]
    comunicacao = dados_missao[i][1]
    bateria = dados_missao[i][2]
    oxigenio = dados_missao[i][3]
    estabilidade = dados_missao[i][4]

    risco_temp, classe_temp, msg_temp = analisar_temperatura(temperatura)
    risco_com, classe_com, msg_com = analisar_comunicacao(comunicacao)
    risco_bat, classe_bat, msg_bat = analisar_bateria(bateria)
    risco_oxi, classe_oxi, msg_oxi = analisar_oxigenio(oxigenio)
    risco_est, classe_est, msg_est = analisar_estabilidade(estabilidade)

    risco_total = risco_temp + risco_com + risco_bat + risco_oxi + risco_est

    riscos.append(risco_total)

    pontos_area[0] += risco_temp
    pontos_area[1] += risco_com
    pontos_area[2] += risco_bat
    pontos_area[3] += risco_oxi
    pontos_area[4] += risco_est

    print("\nCICLO", i + 1)
    print("-" * 60)

    print("Temperatura:", temperatura, "°C |", classe_temp, "|", msg_temp)
    print("Comunicação:", comunicacao, "% |", classe_com, "|", msg_com)
    print("Bateria:", bateria, "% |", classe_bat, "|", msg_bat)
    print("Oxigênio:", oxigenio, "% |", classe_oxi, "|", msg_oxi)
    print("Estabilidade:", estabilidade, "% |", classe_est, "|", msg_est)

    print("\nPontuação de risco do ciclo:", risco_total)
    print("Classificação do ciclo:", classificar_ciclo(risco_total))
    print("Recomendação:", recomendacao(risco_total))

print("\n" + "=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

soma_temp = 0
soma_com = 0
soma_bat = 0
soma_oxi = 0
soma_est = 0

for ciclo in dados_missao:
    soma_temp += ciclo[0]
    soma_com += ciclo[1]
    soma_bat += ciclo[2]
    soma_oxi += ciclo[3]
    soma_est += ciclo[4]

media_temp = soma_temp / len(dados_missao)
media_com = soma_com / len(dados_missao)
media_bat = soma_bat / len(dados_missao)
media_oxi = soma_oxi / len(dados_missao)
media_est = soma_est / len(dados_missao)

maior_risco = max(riscos)
ciclo_critico = riscos.index(maior_risco) + 1

media_risco = sum(riscos) / len(riscos)

qtd_criticos = 0
for risco in riscos:
    if risco > 5:
        qtd_criticos += 1

print("Missão:", nome_missao)
print("Equipe:", equipe)

print("\nQuantidade de ciclos analisados:", len(dados_missao))

print("\nMédia de temperatura:", round(media_temp, 2), "°C")
print("Média de comunicação:", round(media_com, 2), "%")
print("Média de bateria:", round(media_bat, 2), "%")
print("Média de oxigênio:", round(media_oxi, 2), "%")
print("Média de estabilidade:", round(media_est, 2), "%")

print("\nCiclo mais crítico: Ciclo", ciclo_critico)
print("Maior pontuação de risco:", maior_risco)
print("Risco médio da missão:", round(media_risco, 2))
print("Quantidade de ciclos críticos:", qtd_criticos)

if riscos[len(riscos)-1] > riscos[0]:
    tendencia = "A missão apresentou tendência de piora."
elif riscos[len(riscos)-1] < riscos[0]:
    tendencia = "A missão apresentou tendência de melhora."
else:
    tendencia = "A missão permaneceu estável."

print("\nTendência da missão:")
print(tendencia)

print("\nPontuação acumulada por área:")

for i in range(len(areas_monitoradas)):
    print(areas_monitoradas[i] + ":", pontos_area[i], "pontos")

maior_area = max(pontos_area)
indice_area = pontos_area.index(maior_area)

print("\nÁrea mais afetada:")
print(areas_monitoradas[indice_area])

print("\nClassificação final da missão:")

if media_risco <= 2:
    classificacao_final = "MISSÃO ESTÁVEL"
elif media_risco <= 5:
    classificacao_final = "MISSÃO EM ATENÇÃO"
else:
    classificacao_final = "MISSÃO CRÍTICA"

print(classificacao_final)

print("\nConclusão:")

if classificacao_final == "MISSÃO ESTÁVEL":
    print("A missão manteve parâmetros seguros durante toda a operação.")
elif classificacao_final == "MISSÃO EM ATENÇÃO":
    print("A missão apresentou instabilidade relevante durante a operação. Apesar da recuperação parcial, alguns sistemas exigem monitoramento contínuo.")
else:
    print("A missão apresentou condições críticas e necessita de intervenção imediata para garantir a continuidade da operação.")