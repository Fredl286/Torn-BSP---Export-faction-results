import requests
import os
import csv
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
BSP_API_KEY = os.getenv("BSP_API_KEY")

def fetch_faction_members(faction_id):
    if not API_KEY:
        raise ValueError("API_KEY is not set in the .env file")
    
    url = f"https://api.torn.com/v2/faction/{faction_id}/members"
    params = {"key": API_KEY}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def post_battlestats(member_id):
    if not BSP_API_KEY:
        raise ValueError("BSP_API_KEY is not set in the .env file")
    
    url = f"http://www.lol-manager.com/api/battlestats/{BSP_API_KEY}/{member_id}/torn-bsp-faction-export"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get data for Member ID: {member_id}: {e}")
        return None

def process_and_save_data(faction_data, output_file="output.csv"):
    if not faction_data or "members" not in faction_data:
        print("No members found in the response.")
        return
    
    members = faction_data["members"]
    
    with open(output_file, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "name", "level", "TBS", "Score", "PredictionDate"]
        )
        writer.writeheader()
        
        for member in members:
            # Extract member details
            member_id = member.get("id")
            name = member.get("name")
            level = member.get("level")
            
            # Print progress
            print(f"Processing Member ID: {member_id}...")
            
            stats_response = post_battlestats(member_id)
            if stats_response:
                # Combine data from both calls into a single row
                row = {
                    "id": member_id,
                    "name": name,
                    "level": level,
                    "TBS": stats_response.get("TBS"),
                    "Score": stats_response.get("Score"),
                    "PredictionDate": stats_response.get("PredictionDate"),
                }
                writer.writerow(row)

if __name__ == "__main__":
    faction_id = input("Enter the faction ID: ")
    faction_data = fetch_faction_members(faction_id)
    
    if faction_data:
        print("Processing faction members and fetching BattleStats...")
        process_and_save_data(faction_data)
        print("Data saved to output.csv.")
