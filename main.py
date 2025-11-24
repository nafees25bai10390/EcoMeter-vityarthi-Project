import sys
from emissions_logic import calculate_emissions, get_impact_analysis
from history_manager import save_trip, load_history

def show_history():
    print("\n--- 📜 Trip History ---")
    trips = load_history()
    
    if not trips:
        print("No history found yet.")
    else:
        print(f"{'Date':<20} | {'Vehicle':<10} | {'CO2 (kg)':<10} | {'Trees Needed':<12}")
        print("-" * 65)
        for trip in trips:
            print(f"{trip['Date']:<20} | {trip['Vehicle']:<10} | {trip['CO2_Kg']:<10} | {trip['Trees_Offset']:<12}")
    input("\nPress Enter to return...")

def new_trip_workflow():
    print("\n--- 🚗 New Trip Calculation ---")
    print("Vehicle Types: small_car, suv, motorbike, bus")
    v_type = input("Enter Vehicle Type: ").lower().strip()
    
    print("Fuel Types: petrol, diesel, electric")
    f_type = input("Enter Fuel Type: ").lower().strip()
    
    try:
        dist_input = input("Enter Distance (km): ")
        dist = float(dist_input)
        if dist < 0:
             print("❌ Error: Distance cannot be negative.")
             return
    except ValueError:
        print("❌ Error: Distance must be a valid number.")
        return
    co2_result, error = calculate_emissions(v_type, f_type, dist)

    if error:
        print(f"❌ Error: {error}")
    else:
        trees = get_impact_analysis(co2_result)
        print(f"\n✅ RESULTS:")
        print(f"Total CO2 Emitted: {co2_result:.2f} kg")
        print(f"🌲 Environmental Impact: You need {trees} trees to offset this trip!")
        save_choice = input("\nSave this trip? (y/n): ").lower()
        if save_choice == 'y':
            success, msg = save_trip(v_type, f_type, dist, round(co2_result, 2), trees)
            print(msg)

def main_menu():
    while True:
        print("\n=== 🌍 EcoMeter: Carbon Tracker ===")
        print("1. Calculate New Trip")
        print("2. View History")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            new_trip_workflow()
        elif choice == '2':
            show_history()
        elif choice == '3':
            print("Goodbye! Stay Green. 🌱")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()