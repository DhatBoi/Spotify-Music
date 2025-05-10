import pandas as pd
import sqlite3
#from sqlalchemy import create_engine

#extracts and read file from the file path with pandas 
def data_extraction(file_path):
    df = pd.read_csv(file_path)
    return df

#transforms and clean data(selects needed columns from the  data)
def data_transformation(df):
    df = df[['artist_name','genres','followers','track_name','album_name','release_date',
           'duration_ms','artist_popularity']]
    return df

#links selected data columns to database using sqlite3
def load_data(df, database_name):
    link = sqlite3.connect(database_name)
    df.to_sql('spotify music', con=link, if_exists='replace', index=False)
    print("Data loaded successfully....!")

#compiles various function parts and runs through a pipeline
def run_pipeline():
    data = data_extraction(r'C:/Users/stanl/Desktop/Projects/spotifydataset.csv')
    cleaned_data = data_transformation(data)
    load_data(cleaned_data, 'spotify music.db')

if __name__ == "__main__":
    run_pipeline()