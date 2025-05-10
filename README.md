# Spotify Data Pipeline

This Python script (`Spotify pipeline.py`) automates the process of extracting, transforming, and loading Spotify data into a SQLite database.

## Description

The script performs the following actions:

1.  **Data Extraction:** Reads data from a CSV file using the `pandas` library.
2.  **Data Transformation:** Selects and cleans specific columns from the extracted data.
3.  **Data Loading:** Creates a SQLite database and loads the transformed data into a table.

## Dependencies

* Python 3.x
* pandas
* sqlite3 (This comes with Python, but you need SQLite to interact with the created database file)

## Setup

1.  Ensure Python 3.x is installed on your system.
2.  Install the pandas library:
    ```bash
    pip install pandas
    ```
3.  Place the input CSV data file in the location specified in the script or modify the `file_path` variable.

## Usage

1.  Run the script:
    ```bash
    python Spotify pipeline.py
    ```

This will execute the pipeline, creating a SQLite database (`spotify music.db`) in the same directory and loading the processed data into it.

## File

* `Spotify pipeline.py`: The main Python script containing the data pipeline logic.
