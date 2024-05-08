import mysql.connector
import pandas as pd
import numpy as np


host = "127.0.0.1"
user = "root"
password = "admin"
database = "task2"
table_name = "moviess"
csv_file_path = "netflix_titles_nov_2019.csv"

conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()

try:
    df = pd.read_csv(csv_file_path)

    
    df = df.where(pd.notna(df), None)

    
    df = df.fillna('') 

    df['date_added'] = pd.to_datetime(df['date_added']).dt.strftime('%Y-%m-%d')

   
    for index, row in df.iterrows():
       
        duration = row['duration']
        duration_value = None
        duration_unit = None
        if isinstance(duration, str):
            duration_parts = duration.split()
            if len(duration_parts) == 2:
                duration_value = int(duration_parts[0])
                duration_unit = duration_parts[1]

        try:
            cursor.execute(
                f"INSERT INTO {table_name} (show_id, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    row['show_id'], row['title'], row['director'], row['cast'], row['country'], row['date_added'],
                    row['release_year'], row['rating'], duration_value, row['listed_in'], row['description'], row['type']
                )
            )
        except Exception as e:
            print(f"Error inserting row {index + 1}: {e}")
            print("Row data:", row)

    conn.commit()
    print("CSV data uploaded successfully to MySQL.")

except Exception as e:
    print("Error:", e)
    conn.rollback()

finally:

    cursor.close()
    conn.close()
