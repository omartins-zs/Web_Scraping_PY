
# Faz um for com o Link do Site e Adiciona na URL o Id de cada Jogo
for link in tqdm(id_jogos, total=len(id_jogos)):
    wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/match-summary')
    
    # Pegando as Informacoes Básicas do Jogo
    try:
        Date = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__startTime').text.split(' ')[0]
        Time = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__startTime').text.split(' ')[1]
        Country = wd_Chrome.find_element(By.CSS_SELECTOR,'span.tournamentHeader__country').text.split(':')[0]
        League = wd_Chrome.find_element(By.CSS_SELECTOR,'span.tournamentHeader__country')
        League = League.find_element(By.CSS_SELECTOR,'a').text
        Home = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__home')
        Home = Home.find_element(By.CSS_SELECTOR,'div.participant__participantName').text
        Away = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__away')
        Away = Away.find_element(By.CSS_SELECTOR,'div.participant__participantName').text
        
        # Match Odds
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/1x2-odds/full-time')
        time.sleep(2)
        celulas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
        
        Odds_H = 0
        Odds_D = 0
        Odds_A = 0
        
        if 'title="bet365"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if ((bookie == 'bet365') & (Odds_H == 0)) | ((bookie == 'Betfair') & (Odds_H == 0)):
                    Odds_H = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text
                    Odds_D = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text 
                    Odds_A = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text
                else:
                    pass
        else:
            for celula in celulas:
                Odds_H = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text
                Odds_D = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text 
                Odds_A = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text

    except:
        pass

    print(Date,Time,Country,League,Home,Away,Odds_H,Odds_D,Odds_A) 

    jogo['Date'].append(Date)
    jogo['Time'].append(Time)
    jogo['Country'].append(Country)
    jogo['League'].append(League)
    jogo['Home'].append(Home)
    jogo['Away'].append(Away)
    jogo['Odds_H'].append(Odds_H)
    jogo['Odds_D'].append(Odds_D)
    jogo['Odds_A'].append(Odds_A)
