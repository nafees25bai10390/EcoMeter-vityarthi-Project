from config import EMISSION_FACTORS, TREE_ABSORPTION_KG

def calculate_emissions(vehicle_type, fuel_type, distance_km):
    """
    Calculates total CO2 emissions.
    """
    if vehicle_type not in EMISSION_FACTORS:
        return None, "Invalid Vehicle Type."
    
    if fuel_type not in EMISSION_FACTORS[vehicle_type]:
        return None, f"Invalid Fuel Type for {vehicle_type}."

    grams_per_km = EMISSION_FACTORS[vehicle_type][fuel_type]
    total_grams = grams_per_km * float(distance_km)
    total_kg = total_grams / 1000.0

    return total_kg, None

def get_impact_analysis(co2_kg):
    if co2_kg <= 0:
        return 0
    trees_needed = co2_kg / TREE_ABSORPTION_KG
    return round(trees_needed, 2)