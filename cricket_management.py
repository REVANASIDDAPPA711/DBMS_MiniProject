import pymysql
from pymysql import Error
# Create a connection to the database
def create_connection():
  try:
    connection = pymysql.connect(
      host='localhost',
      user='root',
      password='sreenivas@12',
      database='cricket_db'
    )
    if connection.open:
       print("Connected to MySQL database")
       return connection
  except pymysql.MySQLError as err:
    print(f"Error: {err}")
  return None
# Create tables
def create_tables(connection):
  if connection is None:
    print("No connection to MySQL database. Tables not created.")
    return
  cursor = connection.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS teams (
      id INT AUTO_INCREMENT,
      name VARCHAR(255),
      captain VARCHAR(255),
      coach VARCHAR(255),
      PRIMARY KEY (id)
    )
 """)
 cursor.execute("""
   CREATE TABLE IF NOT EXISTS players (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    team_id INT,
    role VARCHAR(255),
    PRIMARY KEY (id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
   )
""")
cursor.execute("""
  CREATE TABLE IF NOT EXISTS matches (
  id INT AUTO_INCREMENT,
  team1_id INT,
  team2_id INT,
  date DATE,
  result VARCHAR(255),
  PRIMARY KEY (id),
  FOREIGN KEY (team1_id) REFERENCES teams(id),
  FOREIGN KEY (team2_id) REFERENCES teams(id)
 )
 """)
 connection.commit()
 cursor.close()
# Add a team
def add_team(name, captain, coach):
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      query = "INSERT INTO teams (name, captain, coach) VALUES (%s, %s, %s)"
      values = (name, captain, coach)
      cursor.execute(query, values)
      connection.commit()
      cursor.close()
      print("Team added successfully!")
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
# Add a player
def add_player(name, team_id, role):
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      query = "INSERT INTO players (name, team_id, role) VALUES (%s, %s, %s)"
      values = (name, team_id, role)
      cursor.execute(query, values)
      connection.commit()
      cursor.close()
      print("Player added successfully!")
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
# Add a match
def add_match(team1_id, team2_id, date, result):
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      query = "INSERT INTO matches (team1_id, team2_id, date, result) VALUES (%s,%s, %s, %s)"
      values = (team1_id, team2_id, date, result)
      cursor.execute(query, values)
      connection.commit()
      cursor.close()
      print("Match added successfully!")
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
# Update a team
def update_team(team_id, name=None, captain=None, coach=None):
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      update_query = "UPDATE teams SET "
      updates = []
      values = []
      if name:
        updates.append("name = %s")
        values.append(name)
      if captain:
        updates.append("captain = %s")
        values.append(captain)
      if coach:
        updates.append("coach = %s")
        values.append(coach)
      update_query += ", ".join(updates) + " WHERE id = %s"
      values.append(team_id)
      cursor.execute(update_query, tuple(values))
      connection.commit()
      cursor.close()
      print("Team updated successfully!")
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
# Update a player
def update_player(player_id, name=None, team_id=None, role=None):
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      update_query = "UPDATE players SET "
      updates = []
      values = []
      if name:
        updates.append("name = %s")
        values.append(name)
      if team_id:
        updates.append("team_id = %s")
        values.append(team_id)
      if role:
        updates.append("role = %s")
        values.append(role)
      update_query += ", ".join(updates) + " WHERE id = %s"
      values.append(player_id)
      cursor.execute(update_query, tuple(values))
      connection.commit()
      cursor.close()
      print("Player updated successfully!")
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
# Update a match
def update_match(match_id, team1_id=None, team2_id=None, date=None, result=None):
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      update_query = "UPDATE matches SET "
      updates = []
      values = []
      if team1_id:
        updates.append("team1_id = %s")
        values.append(team1_id)
      if team2_id:
        updates.append("team2_id = %s")
        values.append(team2_id)
      if date:
        updates.append("date = %s")
        values.append(date)
      if result:
        updates.append("result = %s")
        values.append(result)
      update_query += ", ".join(updates) + " WHERE id = %s"
      values.append(match_id)
      cursor.execute(update_query, tuple(values))
      connection.commit()
      cursor.close()
      print("Match updated successfully!")
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
# Delete a team
def delete_team(team_id):
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      cursor.execute("DELETE FROM teams WHERE id = %s", (team_id,))
      connection.commit()
      cursor.close()
      print("Team deleted successfully!")
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
# Delete a player
def delete_player(player_id):
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      cursor.execute("DELETE FROM players WHERE id = %s", (player_id,))
      connection.commit()
      cursor.close()
      print("Player deleted successfully!")
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
# Delete a match
def delete_match(match_id):
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      cursor.execute("DELETE FROM matches WHERE id = %s", (match_id,))
      connection.commit()
      cursor.close()
      print("Match deleted successfully!")
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
#Get Teams
def get_teams():
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      query = "SELECT * FROM teams"
      cursor.execute(query)
      result = cursor.fetchall()
      cursor.close()
      return result
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
  return []
# Get players
def get_players():
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      query = "SELECT * FROM players"
      cursor.execute(query)
      result = cursor.fetchall()
      cursor.close()
      return result
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
  return []
# Get matches
def get_matches():
  connection = create_connection()
  if connection:
    try:
      cursor = connection.cursor()
      query = "SELECT * FROM matches"
      cursor.execute(query)
      result = cursor.fetchall()
      cursor.close()
      return result
    except pymysql.MySQLError as err:
      print(f"Error: {err}")
    finally:
      connection.close()
  return []
# Main function
def main():
  connection = create_connection()
  if connection:
    create_tables(connection)
    connection.close()
  while True:
    print("\nCricket Database Menu:")
    print("1. Add a team")
    print("2. Add a player")
    print("3. Add a match")
    print("4. Update a team")
    print("5. Update a player")
    print("6. Update a match")
    print("7. Delete a team")
    print("8. Delete a player")
    print("9. Delete a match")
    print("10. View all teams")
    print("11. View all players")
    print("12. View all matches")
    print("13. Exit")
    choice = input("Enter your choice (1-13): ")
    if choice == '1':
      name = input("Enter team name: ")
      captain = input("Enter captain's name: ")
      coach = input("Enter coach's name: ")
      add_team(name, captain, coach)
    elif choice == '2':
      name = input("Enter player's name: ")
      team_id = int(input("Enter team ID: "))
      role = input("Enter player's role: ")
      add_player(name, team_id, role)
    elif choice == '3':
      team1_id = int(input("Enter first team ID: "))
      team2_id = int(input("Enter second team ID: "))
      date = input("Enter match date (YYYY-MM-DD): ")
      result = input("Enter match result: ")
      add_match(team1_id, team2_id, date, result)
    elif choice == '4':
      team_id = int(input("Enter team ID to update: "))
      name = input("Enter new team name (leave empty to skip): ")
      captain = input("Enter new captain's name (leave empty to skip): ")
      coach = input("Enter new coach's name (leave empty to skip): ")
      update_team(team_id, name or None, captain or None, coach or None)
    elif choice == '5':
      player_id = int(input("Enter player ID to update: "))
      name = input("Enter new player's name (leave empty to skip): ")
      team_id = input("Enter new team ID (leave empty to skip): ")
      role = input("Enter new role (leave empty to skip): ")
      update_player(player_id, name or None, int(team_id) if team_id else None, role orNone)
    elif choice == '6':
      match_id = int(input("Enter match ID to update: "))
      team1_id = input("Enter new first team ID (leave empty to skip): ")
      team2_id = input("Enter new second team ID (leave empty to skip): ")
      date = input("Enter new match date (leave empty to skip): ")
      result = input("Enter new match result (leave empty to skip): ")
      update_match(match_id, int(team1_id) if team1_id else None, int(team2_id) if
      team2_id else None, date or None, result or None)
    elif choice == '7':
      team_id = int(input("Enter team ID to delete: "))
      delete_team(team_id)
    elif choice == '8':
      player_id = int(input("Enter player ID to delete: "))
      delete_player(player_id)
    elif choice == '9':
      match_id = int(input("Enter match ID to delete: "))
      delete_match(match_id)
    elif choice == '10':
      teams = get_teams()
      if teams:
        print("\nTeams:")
        for team in teams:
          print(f"ID: {team[0]}, Name: {team[1]}, Captain: {team[2]}, Coach: {team[3]}")
      else:
        print("No teams found.")
    elif choice == '11':
      players = get_players()
      if players:
        print("\nPlayers:")
        for player in players:
          print(f"ID: {player[0]}, Name: {player[1]}, Team ID: {player[2]}, Role:{player[3]}")
      else:
        print("No players found.")
    elif choice == '12':
      matches = get_matches()
      if matches:
        print("\nMatches:")
        for match in matches:
          print(f"ID: {match[0]}, Team 1 ID: {match[1]}, Team 2 ID: {match[2]}, Date:{match[3]}, Result: {match[4]}")
      else:
        print("No matches found.")
    elif choice == '13':
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 13.")
# Run the main function
if __name__ == "__main__":
  main()
