import pandas as pd
import matplotlib.pyplot as plt

def playerperformance(playername):
    playerdata = []
    for year in range(0, 24):
        url = f'https://www.pro-football-reference.com/years/20{year:02d}/passing.htm'
        tables = pd.read_html(url)
        passingstatsdf = tables[0]

        playerstats = passingstatsdf[passingstatsdf['Player'].str.contains(playername, case=False)]
        if not playerstats.empty:
            yards = playerstats['Yds'].iloc[0]
            touchdowns = playerstats['TD'].iloc[0]
            interceptions = playerstats['Int'].iloc[0]
            playerdata.append({'Year': 2000 + year, 'Yards': yards, 'Touchdowns': touchdowns, 'Interceptions': interceptions})

    if not playerdata:
        print(f"No data found for player '{playername}'")
    else:
        players = pd.DataFrame(playerdata)
        players = players.sort_values(by='Year')  # creates a better graph? idk.
        plt.figure(figsize=(10, 6))
        plt.plot(players['Year'], players['Yards'], label='Yards')
        plt.plot(players['Year'], players['Touchdowns'], label='Touchdowns')
        plt.plot(players['Year'], players['Interceptions'], label='Interceptions')
        plt.title(f'Performance of {playername} over Time')
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

playername = input("Enter the name of the player to analyze: ").strip()
playerperformance(playername)
