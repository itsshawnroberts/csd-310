# Shawn Roberts
# 07/02/2021
# Module 8
# 8.2 MySQL Setup

# git@github.com:itsshawnroberts/csd-310.git

# I'm connecting to my MySQL database.

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config) # connect to the pysports database 
cursor = db.cursor()
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()
    
print("\n  -- DISPLAYING TEAM RECORDS --")
# fetching the Team information from the db.    
for team in teams: 
    print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

players = cursor.fetchall()
# fetching the Player information from the db.
print ("\n  -- DISPLAYING PLAYER RECORDS --")

for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")