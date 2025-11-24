import csv
import os
from datetime import datetime
from config import CSV_FILENAME

def save_trip(vehicle, fuel, distance, co2, trees):
    """
    Saves the trip details to a CSV file.
    """
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [date_str, vehicle, fuel, distance, co2, trees]
    
    file_exists = os.path.isfile(CSV_FILENAME)
    
    try:
        with open(CSV_FILENAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(["Date", "Vehicle", "Fuel", "Distance_Km", "CO2_Kg", "Trees_Offset"])
            writer.writerow(row)
            return True, "Trip saved successfully!"
    except Exception as e:
        return False, f"Error saving to file: {e}"

def load_history():
    """
    Reads the CSV file and returns a list of past trips.
    """
    if not os.path.exists(CSV_FILENAME):
        return []

    history = []
    try:
        with open(CSV_FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                history.append(row)
    except Exception as e:
        print(f"Error loading history: {e}")
        return []
        
    return history