project_name = "Football Data Explorer"

print("=" * 35)
print(project_name)
print("=" * 35)

print("Welcome to the Football Data Explorer!")
print("Our goal is to analyse football statistics.")

players = ["Cristiano Ronaldo", "Lionel Messi", " Neymar Jr."]

player_stats = {
    "Cristiano Ronaldo": 99,
    "Lionel Messi": 86,
    "Neymar Jr.": 71
}

print("\nPlayers in our database:")

for player in players:
    print(player)

print("\nGoals Scored:")

for player, goals in player_stats.items():
    print(f"{player}: {goals} goals")