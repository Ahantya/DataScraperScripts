import pandas as pd
import plotly.express as px

allplayers = dict()
allplayerinfo = dict()

for year in range(0, 24):
    url = f'https://www.pro-football-reference.com/years/20{year:02d}/passing.htm'
    tables = pd.read_html(url)
    passing_stats_df = tables[0]

    players = passing_stats_df['Player']
    yards = passing_stats_df['Yds']
    ptd = passing_stats_df['TD']
    inter = passing_stats_df['Int']

    teams = list(zip(players, yards, ptd, inter))

    for team in teams[:10]:
        if (int(team[1]) > 4000 and int(team[2]) > 35 and int(team[3]) < 9):
            info = {'yards': team[1], 'TDs': team[2], 'interceptions': team[3]}
            player = team[0].replace('*', '').replace('+', '').strip()

            if player in allplayerinfo:
                if (info['yards'] > allplayerinfo[player]['yards']) and \
                        (info['TDs'] > allplayerinfo[player]['TDs']) and \
                        (info['interceptions'] < allplayerinfo[player]['interceptions']):
                    allplayerinfo[player] = info
            else:
                allplayerinfo[player] = info

            allplayers[player] = allplayers.get(player, 0) + 1

sortedplayers = sorted(allplayers.items())


players_data = pd.DataFrame(sortedplayers, columns=['Player', 'Count'])
players_data = players_data.sort_values(by='Count', ascending=False).head(10)


fig = px.bar(players_data, x='Player', y='Count', color='Player', title='Top Players with Most Appearances')
fig.update_xaxes(tickangle=45)
fig.update_layout(xaxis_title='Player', yaxis_title='Number of Appearances')
fig.show()
