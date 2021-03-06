# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
songplay_id SERIAL PRIMARY KEY,
start_time TIMESTAMP NOT NULL,
user_id INT,
song_id VARCHAR, 
artist_id VARCHAR, 
session_id INT,
location VARCHAR(25), 
user_agent INT
);
""")


user_table_create = ("""CREATE TABLE IF NOT EXISTS users(
user_id INT PRIMARY KEY, 
first_name VARCHAR NOT NULL, 
last_name VARCHAR NOT NULL, 
gender CHAR(1),
level VARCHAR);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
song_id VARCHAR PRIMARY KEY, 
title VARCHAR NOT NULL, 
artist_id VARCHAR, 
year INT, 
duration float);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
artist_id VARCHAR PRIMARY KEY, 
name VARCHAR NOT NULL,
location VARCHAR, 
latitude DECIMAL(8,6),
longitude DECIMAL(9,6));
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
start_time TIMESTAMP PRIMARY KEY,
hour INTEGER NOT NULL CHECK (hour >= 0),
day INTEGER NOT NULL CHECK (day >= 0),
week INTEGER NOT NULL CHECK (week >= 0),
month INTEGER NOT NULL CHECK (month >= 0),
year INTEGER NOT NULL CHECK (year >= 0),
weekday VARCHAR NOT NULL);
""")



# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays
        (
            start_time,
            user_id,
            level,
            song_id,
            artist_id,
            session_id,
            location,
            user_agent
        )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) 
    DO NOTHING;
""")

user_table_insert = (""" INSERT INTO users
        (
        user_id,
        first_name,
        last_name,
        gender, 
        level
        )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE 
        SET level=EXCLUDED.level;
""")

song_table_insert = ("""INSERT INTO songs
        (
        song_id,
        title,
        artist_id,
        year,
        duration        
        )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists
        (
            artist_id,
            name,
            location,
            latitude,
            longitude
        )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO NOTHING;
""")


time_table_insert = (""" INSERT INTO time 
        (
            start_time,
            hour,
            day,
            week,
            month,
            year,
            weekday
        )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time)
    DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT
        songs.song_id AS song_id,
        songs.artist_id AS artist_id
    FROM
        songs JOIN artists
        ON songs.artist_id=artists.artist_id
    WHERE
        songs.title = %s AND 
        artists.name = %s AND 
        songs.duration = %s  
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop,songplay_table_drop]