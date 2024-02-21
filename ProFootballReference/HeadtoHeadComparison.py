# haven't tested whether it works due to "too many requests" server error. 

import pandas as pd
import matplotlib.pyplot as plt

def getplayerstats(player_name):
    playerstats = {'yards': 0, 'touchdowns': 0, 'interceptions': 0}
    for year in range(0, 24):
        url = f'https://www.pro-football-reference.com/years/20{year:02d}/passing.htm'
        tables = pd.read_html(url)
        passing_stats_df = tables[0]

        playeryearstats = passing_stats_df[passing_stats_df['Player'].str.contains(player_name, case=False)]
        if not playeryearstats.empty:
            playerstats['yards'] += int(playeryearstats['Yds'].iloc[0])
            playerstats['touchdowns'] += int(playeryearstats['TD'].iloc[0])
            playerstats['interceptions'] += int(playeryearstats['Int'].iloc[0])  # iloc hooray

    return playerstats

def headtohead(player1name, player2name):
    player1stats = getplayerstats(player1name)
    player2stats = getplayerstats(player2name)

    fig, ax = plt.subplots(figsize=(10, 6))

    bar_width = 0.35
    index = range(3)
    labels = ['Yards', 'Touchdowns', 'Interceptions']

    player1_values = [player1stats['yards'], player1stats['touchdowns'], player1stats['interceptions']]
    player2_values = [player2stats['yards'], player2stats['touchdowns'], player2stats['interceptions']]

    bar1 = ax.bar(index, player1_values, bar_width, label=player1name)
    bar2 = ax.bar([i + bar_width for i in index], player2_values, bar_width, label=player2name)

    ax.set_xlabel('Statistic')
    ax.set_ylabel('Count')
    ax.set_title(f'Head-to-Head Stats: {player1name} vs {player2name}')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate('{}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(bar1)
    autolabel(bar2)

    plt.tight_layout()
    plt.show()

player1name = input("Enter the name of Player 1: ").strip()
player2name = input("Enter the name of Player 2: ").strip()

headtohead(player1name, player2name)
