# Criando Dataframe e Filtrando apenas os que tem ODD maior que 0
    df = pd.DataFrame(jogo)
df = df[(df.Odds_H != 0)]
df.reset_index(inplace=True, drop=True)
df.index = df.index.set_names(['Nº'])
df = df.rename(index=lambda x: x + 1)
df

# Criando Tabela

df.to_excel("jogos_do_dia.xlsx")