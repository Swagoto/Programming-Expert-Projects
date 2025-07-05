Steps and Actions
1. **Number of Teams**
    *Dis*:"Enter the number of teams in the tournament: "
    *input*: number_of_teams = int 
    *Constraints*: Must be bigger than 2

2. **Name of Teams**
    *Dis*: "Enter the name for team #1...#n: " for teams
    *input*: team(n)_name = str (n is nth team)
    *Constraints*: Have at least 2 character and at most 2 words.

3. **Game Played by Each Team**
    *Dis*: "Enter the number of games played by each team: "
    *input*: n_games = int
    *Constraints*: n_games =>number_of_teams

4. **Number of wins for each teams**
    *Dis*: "Enter the number of wins Team {team(n)_name} had: "
    *input*: team(n)_wins = int
    *Constraints*: team(n)_wins <= n_games

4. **Makes a descending order series based on team wins**
5. **Register the match with the first and the last member of the series and delete those names**
    *Output*: {max win least} vs {least win team}

6. **Repeat Step 5**
