# Shawn Roberts
# 07/09/2021
# Module 9
# Basic Table Joins
# My Github: git@github.com:itsshawnroberts/csd-310.git

# I'm connecting to My SQL database.
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
} 
# Here I am connecting to the "pysports" database
db = mysql.connector.connect(**config)
cursor = db.cursor()
# Running the inner join query
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()

print("\n  -- DISPLAYING PLAYER RECORDS --")
    
# Running threw the player data and to display the proper results. 
for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
# User input to close th database.
input("\nPress any key to continue... ")

db.close()