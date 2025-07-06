#Step 1: Getting the number of teams
while True:
    try:
        number_of_teams = int(input("Enter the number of teams in the tournament: "))
        if number_of_teams<2:
            print("The minimum number of teams is 2, try again.")
        else:
            break
    except ValueError:
        print("Please try again with a valid integer value.")

#Step 2:Naming the teams
team_names = []
for i in range(number_of_teams):
    while True:
        name = input(f"Enter the name for team #{i+1}: ")
        name_characters = len(name.replace(" ", ""))
        name_words = name.split()
        if name_characters<2:
            print("Team names must have at least 2 characters, try again.")
        elif len(name_words)>2:
            print("Team names may have at most 2 words, try again.")
        else:
            team_names.append(name)
            break


#Step 3: Number of games
while True:
    try:
        n_games = int(input("Enter the number of games played by each team: "))
        if(n_games <number_of_teams):
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        else:
            break
    except ValueError:
        print("Please try again with a valid integer value.")

# Step 4: Number of Wins
team_wins = {}
for team in team_names:
    while True:
        try:
            n_wins = int(input(f"Enter the number of wins Team {team} had: "))
            if n_wins>n_games:
                print(f"The maximum number of wins is {str(n_games)}, try again.")
            elif n_wins<0:
                print("The minimum number of wins is 0, try again.")
            else:
                team_wins[team] = n_wins
                break

        except ValueError:
            print("Please try again with a valid integer value.")

#Step 5: Sort by wins
sorted_teams =[team for team,_ in sorted(team_wins.items(), key = lambda item: item[1])]


#Step 6 & 7: Generate
print("Generating the games to be played in the first round of the tournament...")
while len(sorted_teams)!=0:
    home = sorted_teams.pop(0)
    away = sorted_teams.pop(-1)
    print(f"Home: {home} VS Away: {away}")