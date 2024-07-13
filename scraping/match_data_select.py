# This script fetches NRL (National Rugby League) match data for the year 2024
# and saves it to a JSON file named "nrl_data_2024_round_6.json" in the "./data/test"
# directory.


# Imports

from utilities.get_nrl_data import get_nrl_data
import json
import sys
import os
sys.path.append('..')
#import ENVIRONMENT_VARIABLES as EV

#Initial conditions
# Select the year and the subset of rounds (1 to 27) to scrape 
select_year = 2024
select_rounds = 6

#set location to print to
data_directory = "../NRL-Data/Data/Testing"
# Before opening the file, ensure the directory exists
try:
    os.makedirs(data_directory, exist_ok=True)
    print(f"Directory '{os.path.abspath(data_directory)}' created successfully.")
except Exception as e:
    print(f"Failed to create directory '{os.path.abspath(data_directory)}'. Error: {e}")

years = [select_year]
if __name__ == "__main__":
    match_json_datas = []  # List to store JSON data for matches
    for year in years:
        year_json_data = []  # List to store JSON data for a particular year
        for round_nu in range(1, select_rounds + 1):  # Loop through 25 rounds
            try:
                # Attempt to fetch NRL data for a specific round and year
                match_json = get_nrl_data(round_nu, year)
                # Append fetched JSON to year's data list
                year_json_data.append(match_json)
            except Exception as ex:
                print(f"Error: {ex}")
        # Store year's data in a dictionary
        year_data = {
            f"{year}": year_json_data
        }
        # Append year's data to the main list
        match_json_datas.append(year_data)

    # Create overall data dictionary
    overall_data = {
        "NRL": match_json_datas
    }
    # Convert overall data to JSON format with indentation for better
    # readability
    overall_data_json = json.dumps(overall_data, indent=4)

    # # Write JSON data to a file
    
    with open(f"{data_directory}/nrl_data_{select_year}_round_{select_rounds}.json", "w") as file:
       file.write(overall_data_json)
    
