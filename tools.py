from helpers import read_json

def show_batting_stats():
    data = read_json("players.json")

    print("\nTop Batting Performers")
    for player in data["batting"]:
        print(player["player"], "-", player["team"], "-", player["runs"], "runs")


def show_bowling_stats():
    data = read_json("players.json")

    print("\nTop Bowling Performers")
    for player in data["bowling"]:
        print(player["player"], "-", player["team"], "-", player["wickets"], "wickets")


def show_matches():
    matches = read_json("matches.json")

    print("\nRecent Matches")
    for match in matches:
        print(match["match"], "->", match["result"])
