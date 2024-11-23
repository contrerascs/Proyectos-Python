import pandas as pd
#Leer 1 archivo csv de un website
df_premier_league = pd.read_csv('https://www.football-data.co.uk/mmz4281/2324/E0.csv')
print(df_premier_league)

#Cambiar nombre a columnas
df_premier_league.rename(columns={'Date':'date',
                                 'HomeTeam':'equipo_local',
                                 'AwayTeam':'equipo_visitante',
                                 'FTHG':'goales_locales',
                                 'FTAG':'goles_visitantes'}, inplace=True)

print(df_premier_league)