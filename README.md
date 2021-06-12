# Database Modeling for Sparkify

### Background 
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
I have been assigned to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. My role is to create a database schema and ETL pipeline for this analysis. The database and ETL pipeline will be tested by running queries submitted by the analytics team from Sparkify and compare your results with their expected results.

### Project Description
An ETL pipeline will be built using python. The fact and dimension tables will be created for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and Sql.

### Datasets
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. 
The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

### Schema
The star database schema will be used for this project. There is one fact table and four dimension tables with enables Sparkify to conduct simplified queries and allow for fast aggregrations. 
Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong

songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
Dimension Tables
users - users in the app

user_id, first_name, last_name, gender, level
songs - songs in music database

song_id, title, artist_id, year, duration
artists - artists in music database

artist_id, name, location, latitude, longitude
time - timestamps of records in songplays broken down into specific units

start_time, hour, day, week, month, year, weekday

### Project Files
sql_queries.py - contains sql queries for dropping and creating fact and dimension tables. Also, contains insertion query template.

create_tables.py - contains code for setting up database. Running this file creates sparkifydb and also creates the fact and dimension tables.

etl.ipynb - a jupyter notebook to analyse dataset before loading.

etl.py - read and process song_data and log_data

test.ipynb - a notebook to connect to postgres db and validate the data loaded.

### Environment
Python 3.6 or above

PostgresSQL 9.5 or above

psycopg2 - PostgreSQL database adapter for Python