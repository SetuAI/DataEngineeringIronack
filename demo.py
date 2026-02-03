import requests
import csv
from datetime import datetime
import sys

# Configuration Constants
API_URL = "https://api.open-meteo.com/v1/forecast"
FILENAME = "madrid_weather.csv"

def fetch_weather_data():
    """Step 2: Fetch data with error handling."""
    params = {
        "latitude": 40.4168,
        "longitude": -3.7038,
        "hourly": "temperature_2m,precipitation,wind_speed_10m",
        "forecast_days": 7
    }
    
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        # Raise an exception for 4xx or 5xx status codes
        response.raise_for_status() 
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: {e}")
        return None

def process_data(raw_json):
    """Step 3: Transform JSON arrays into a List of Dictionaries."""
    if not raw_json or "hourly" not in raw_json:
        return []

    hourly = raw_json["hourly"]
    ingestion_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    # The 'Hardcore' way: Using zip() to combine parallel arrays
    # This aligns timestamps with their specific temp/precip/wind values
    processed_records = [
        {
            "timestamp": t,
            "temperature_c": temp,
            "precipitation_mm": precip,
            "wind_speed_kmh": wind,
            "ingestion_time": ingestion_time
        }
        for t, temp, precip, wind in zip(
            hourly["time"], 
            hourly["temperature_2m"], 
            hourly["precipitation"], 
            hourly["wind_speed_10m"]
        )
    ]
    return processed_records

def save_to_csv(data, filename):
    """Step 4 & 5: Save to disk with error handling."""
    if not data:
        print("⚠️ No data available to save.")
        return

    try:
        keys = data[0].keys()
        with open(filename, 'w', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        print(f"✅ Success! Data saved to {filename}")
        
    except IOError as e:
        print(f"❌ File Error: Could not write to file. {e}")

def main():
    print("🚀 Starting Weather Ingestion Pipeline...")
    
    # 1. Extraction
    raw_data = fetch_weather_data()
    
    # 2. Transformation
    clean_data = process_data(raw_data)
    
    # 3. Loading
    save_to_csv(clean_data, FILENAME)

if __name__ == "__main__":
    main()