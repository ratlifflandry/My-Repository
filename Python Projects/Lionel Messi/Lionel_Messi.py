from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Lionel_Messi Dataset
Lionel_Messi = Table.read_table('Lionel_Messi.csv')
print(Lionel_Messi)

#Renaming Competition Names
competition = make_array()

for i in range(0, len(Lionel_Messi.column('competition'))):

    if Lionel_Messi.column('competition')[i] == '2ª B - Grupo III':
        competition = np.append(competition, 'Spanish Third Division')
    elif Lionel_Messi.column('competition')[i] == 'CONCACAF Champions Cup':
        competition = np.append(competition, 'North America Champions Cup')
    elif Lionel_Messi.column('competition')[i] == 'Club World Cup':
        competition = np.append(competition, 'Club World Cup')
    elif Lionel_Messi.column('competition')[i] == 'Copa del Rey':
        competition = np.append(competition, 'Spanish Cup')
    elif Lionel_Messi.column('competition')[i] == 'LaLiga':
        competition = np.append(competition, 'Spanish League')
    elif Lionel_Messi.column('competition')[i] == 'Leagues Cup':
        competition = np.append(competition, 'MLS vs Liga MX Cup')
    elif Lionel_Messi.column('competition')[i] == 'Ligue 1':
        competition = np.append(competition, 'French League')
    elif Lionel_Messi.column('competition')[i] == 'MLS':
        competition = np.append(competition, 'Major League Soccer')
    elif Lionel_Messi.column('competition')[i] == 'MLS Cup Playoffs':
        competition = np.append(competition, 'Major League Soccer Playoffs')
    elif Lionel_Messi.column('competition')[i] == 'Supercopa':
        competition = np.append(competition, 'Spanish Super Cup')
    elif Lionel_Messi.column('competition')[i] == 'Trophée des Champions':
        competition = np.append(competition, 'French Super Cup')
    elif Lionel_Messi.column('competition')[i] == 'UEFA Champions League':
        competition = np.append(competition, 'Champions League')
    elif Lionel_Messi.column('competition')[i] == 'UEFA Super Cup':
        competition = np.append(competition, 'European Super Cup')

#Highest Scoring Game
game = make_array()

for i in range(0, len(Lionel_Messi.column('match_score'))):
    a = 0
    b = 0

    a = int(Lionel_Messi.column('match_score')[i].split(':')[0])
    b = int(Lionel_Messi.column('match_score')[i].split(':')[1])

    if a > b:
        game = np.append(game, 'Win')
    elif a == b:
        game = np.append(game, 'Draw')
    elif a < b:
        game = np.append(game, 'Loss')

Lionel_Messi = Lionel_Messi.drop('competition').with_column('competition', competition).with_column('game_result', game)
Lionel_Messi = Lionel_Messi.select('date', 'club', 'opponent', 'competition', 'venue', 'match_score', 'game_result', 'player_position', 'player_position', 'goal_minute', 'goal_type', 'assist_player', 'season', 'goal_decade', 'match_stage')

print(Lionel_Messi)
print(Lionel_Messi.num_rows)
print(Lionel_Messi.num_columns)
print(Lionel_Messi.labels)

#Number of Wins, Draws, Loss
Lionel_Messi.group('game_result').sort('count', descending = True).barh('game_result', 'count')
plt.xlabel('Count')
plt.ylabel('Game Result')
plt.title('Number of Wins, Draws, & Loss')
plt.show()

#Number of Goals Scored by Competition Bar Chart
Lionel_Messi.group('competition').sort('count', descending = True).barh('competition', 'count')
plt.xlabel('Count')
plt.ylabel('Competition')
plt.title('Number of Goals by Competition')
plt.show()

#Number of Goals Scored by Season Bar Chart
Lionel_Messi.group('season').sort('count', descending = True).barh('season', 'count')
plt.xlabel('Count')
plt.ylabel('Season')
plt.title('Number of Goals by Season')
plt.show()

#Number of Goals Scored by Club Bar Chart
Lionel_Messi.group('club').sort('count', descending = True).barh('club', 'count')
plt.xlabel('Count')
plt.ylabel('Club')
plt.title('Number of Goals Scored by Club')
plt.show()

#Number of Goals Scored on an Opponent Bar Chart
Lionel_Messi.group('opponent').sort('count', descending = True).take([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).barh('opponent', 'count')
plt.xlabel('Count')
plt.ylabel('Opponent')
plt.title('Number of Goals Scored on an Opponent')
plt.show()

#Number of Goals by Minute Histogram
Lionel_Messi.hist('goal_minute', bins = 10)
plt.xlabel('Goal Minute')
plt.ylabel('Count')
plt.title('Number of Goals by Minute')
plt.show()

#Bell Curve of Goals by Minute
mean = np.mean(Lionel_Messi.column('goal_minute'))
std_dev = np.std(Lionel_Messi.column('goal_minute'))

def PDF(x):
    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean)/std_dev) ** 2)

x = np.linspace(0, 100, 1000)
y = PDF(x)

plt.plot(x, y, color='blue', label='Standard Normal PDF')
plt.xlabel('Goal Minute')
plt.ylabel('Density')
plt.title('Normal Distribution of Goals Scored by Minute')
plt.legend()
plt.show()

#Pie Chart of Proportion of Goals by Goal Type
goal_type = Lionel_Messi.num_rows

chest = Lionel_Messi.where('goal_type', are.equal_to('Chest')).num_rows
counter_attack = Lionel_Messi.where('goal_type', are.equal_to('Counter attack goal')).num_rows
deflected = Lionel_Messi.where('goal_type', are.equal_to('Deflected shot on goal')).num_rows
free_kick = Lionel_Messi.where('goal_type', are.equal_to('Direct free kick')).num_rows
header = Lionel_Messi.where('goal_type', are.equal_to('Header')).num_rows
left_foot = Lionel_Messi.where('goal_type', are.equal_to('Left-footed shot')).num_rows
long_distance = Lionel_Messi.where('goal_type', are.equal_to('Long distance kick')).num_rows
not_reported = Lionel_Messi.where('goal_type', are.equal_to('Not reported')).num_rows
penalty = Lionel_Messi.where('goal_type', are.equal_to('Penalty')).num_rows
penalty_rebound = Lionel_Messi.where('goal_type', are.equal_to('Penalty rebound')).num_rows
right_foot = Lionel_Messi.where('goal_type', are.equal_to('Right-footed shot')).num_rows
solo_run = Lionel_Messi.where('goal_type', are.equal_to('Solo run')).num_rows
tap_in = Lionel_Messi.where('goal_type', are.equal_to('Tap-in')).num_rows

Goals = Table().with_columns(
    'goal_type', make_array('Chest', 'Counter attack goal', 'Deflected shot on goal',
                            'Direct free kick', 'Header', 'Left-footed shot',
                            'Long distance kick', 'Not reported', 'Penalty',
                            'Penalty rebound', 'Right-footed shot', 'Solo run', 'Tap-in'),
    'percent', make_array(chest/goal_type * 100, counter_attack/goal_type * 100,
                          deflected/goal_type * 100, free_kick/goal_type * 100,
                          header/goal_type * 100, left_foot/goal_type * 100,
                          long_distance/goal_type * 100, not_reported/goal_type * 100,
                          penalty/goal_type * 100, penalty_rebound/goal_type * 100,
                          right_foot/goal_type * 100, solo_run/goal_type * 100,
                          tap_in/goal_type * 100)
)
Goals = Goals.sort('percent', descending = True).take([0, 1, 2, 3, 4, 5])

plt.pie(Goals.column('percent'), labels=Goals.column('goal_type'))
plt.title('Percentage of Goals by Goal Type')
plt.show()

#Number of Player Positions Bar Chart
Lionel_Messi.group('player_position').sort('count', descending = True).barh('player_position', 'count')
plt.xlabel('Count')
plt.ylabel('Player Position')
plt.title('Number of Goals Scored in Player Position')
plt.show()

#Number of Goals by Assist_Player Bar Chart
Lionel_Messi.where('assist_player', are.not_equal_to('Not Applicable')).group('assist_player').sort('count', descending = True).take([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).barh('assist_player', 'count')
plt.xlabel('Count')
plt.ylabel('Assist_Player')
plt.title('Number of Goals Scored by Assist_Player')
plt.show()