import sqlite3
import os
import json

data_path = os.path.join(os.getcwd(), "film1.db")
connect = sqlite3.connect(data_path)
cursor = connect.cursor()

def select_data(conn):
	cursor = connect.cursor()
	cursor.execute("SELECT * FROM film")
	rows = cursor.fetchall()

	list_of_table =[]
	for i in rows:
		list_of_table.append(list(i))
	return list_of_table

# Ex 1 Write script to find the names of movies which name starts with “B”

selected_data = select_data(connect)
films = []

for film_list in selected_data:
	if str(film_list[1])[0] == "B":
		films.append(film_list[1])
print(f"Movies which title starts with 'B' are:\n{films}.")

# Ex 2 Write a python code to find the movie which duration is the largest from film table

duration_list = []
for film_list in selected_data:
	duration_list.append(film_list[5])
	duration_list.sort()
largest_dur = duration_list[-1]

for film_list in selected_data:
	if film_list[5] == largest_dur:
		the_largest_film = film_list[1]
print(f"The largest film in the table is '{the_largest_film}'.")

# Ex 3 Write a python code to write the data from film table into a json file

with open("json_datbase.json", "w") as jsonfile:
	json.dump(selected_data, jsonfile, indent=4)

# Ex 4 extra** write script which finds all the movies from film table which release date is above 2010 
# and rate is between 3 and 5 , after that writes them in a new table called filtered_film

create_ = """ CREATE TABLE IF NOT EXISTS filtered_film_ (
                                        id integer PRIMARY KEY,
                                        title text,
                                        description text,
                                        release_year integer,
                                        rate real,
                                        length integer,
                                        special_features text
                                    ); """


cursor.execute(create_)
connect.commit()

def add_film(values):
	add_ = """INSERT OR IGNORE INTO filtered_film_(id, title, description, release_year, rate, length, special_features)
 	                    VALUES(?,?,?,?,?,?,?);
	                    """
	cursor.execute(add_, values)
	connect.commit()

for film_list in selected_data:
	if float(film_list[4]) >= 3 and float(film_list[4]) <= 5 and film_list[3] > 2010:
		add_film(tuple(film_list))