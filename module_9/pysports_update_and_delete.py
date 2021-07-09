# Shawn Roberts
# 07/09/2021
# Module 9
# Update & Deletes
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


def show_players(cursor, title):

# Showing the ressults of the inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("\n  -- {} --".format(title))
    
# Running threw the player data and to display the proper results. 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try: 
# Connect to the pysports database 
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()
# Adding a player.
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")
# adding the new player data.
    player_data = ("Smeagol", "Shire Folk", 1)
    cursor.execute(add_player, player_data)
# Adds the new player data to the database.
    db.commit()

    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")
# Updating player data
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    cursor.execute(update_player)


    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")
# Deleting a player.
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute(delete_player)
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Check user name and password")

    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist, Please try again")

    else:
        print(ERROR)
# User input to close th database.
finally:
    db.close()
