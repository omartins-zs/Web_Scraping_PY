
# Pegando o ID dos Jogos
id_jogos = []
jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--scheduled')

for i in jogos:
    id_jogos.append(i.get_attribute("id"))

# Exemplo de ID de um jogo: 'g_1_Gb7buXVt'    
# Retira os 4 primeiros caracteres que são padrao "g_1_"
id_jogos = [i[4:] for i in id_jogos]

jogo = {'Date':[],'Time':[],'Country':[],'League':[],'Home':[],'Away':[],'Odds_H':[],'Odds_D':[],'Odds_A':[]}

# Imprimi todos os id dos Jogos
