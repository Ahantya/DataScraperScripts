import requests

# work in progress, all it does is get champion name for last 20 matches, but i no longer feel motivated to be working on this for now at least (2/29/24 11:50 PM)

def getSummonerInfo(summonerName, apiKey):
    apiUrl = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?apiKey={apiKey}"
    resp = requests.get(apiUrl)
    playerInfo = resp.json()
    playerID = playerInfo['accountId']
    playerPuuid = playerInfo['puuid']
    return playerID, playerPuuid

def getRecentMatches(playerPuuid, apiKey, count=20):
    apiUrl = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{playerPuuid}/ids?start=0&count={count}&apiKey={apiKey}"
    resp = requests.get(apiUrl)
    matches = resp.json()
    return matches

def getChampionName(matchID, playerPuuid, apiKey):
    apiUrl = f"https://americas.api.riotgames.com/lol/match/v5/matches/{matchID}?apiKey={apiKey}"
    resp = requests.get(apiUrl)
    matchData = resp.json()
    participants = matchData['metadata']['participants']
    playerIndex = participants.index(playerPuuid)
    championName = matchData['info']['participants'][playerIndex]['championName']
    return championName

def main():
    apiKey = "" # get your own!
    summonerName = "" # you can do your own name!!

    playerID, playerPuuid = getSummonerInfo(summonerName, apiKey)
    matches = getRecentMatches(playerPuuid, apiKey)
    for matchID in matches:
        championName = getChampionName(matchID, playerPuuid, apiKey)
        print(championName)

if __name__ == "__main__":
    main()
