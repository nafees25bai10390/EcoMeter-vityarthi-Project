PROJECT REPORT

EcoMeter: Vehicle Emission Tracker

A Project Report Submitted by:

Nafees Khan

Registration Number: 25BAI10390

I created this project as part of my coursework for:

Python Essentials

1. Introduction

Climate change is one of the most pressing challenges of our time, driven largely by carbon dioxide (CO2) emissions from transportation. "EcoMeter" is a Python-based software application designed to help individuals track and understand their personal carbon footprint. By inputting simple travel details, users can calculate the environmental impact of their daily commutes and visualize this impact in tangible terms, such as the number of trees required to offset their emissions.

2. Problem Statement

While many people are aware of global warming, they often lack the tools to quantify their specific contribution to it. Most commuters do not know how much CO2 their specific vehicle emits per kilometer. Without this data, it is difficult to make informed decisions about travel habits. There is a need for a simple, accessible, and persistent tool that allows users to log their trips and monitor their cumulative environmental impact over time.

3. Functional Requirements

The system implements the following three major functional modules as required by the project guidelines:

3.1 Emission Calculation Engine:
The core module takes user inputs (Vehicle Type, Fuel Type, Distance) and processes them using specific emission factors (e.g., Diesel SUV = 220g/km) to output the total CO2 in kilograms.

3.2 History & Persistence (CRUD):
The system allows users to "Save" their trips. This data is written to a persistent CSV file (trip_history.csv), allowing users to view their travel history even after restarting the application.

3.3 Impact Analysis (Reporting):
Beyond raw numbers, the system analyzes the result and converts the CO2 mass into a "Trees Offset" metric, providing a meaningful environmental context to the user.

4. Non-Functional Requirements

The project adheres to the following quality attributes:

4.1 Usability:
The application features a clear, menu-driven Command Line Interface (CLI) that guides the user step-by-step, ensuring ease of use.

4.2 Reliability:
Data persistence is guaranteed through File I/O operations. If the application closes, the user's history is not lost.

4.3 Error Handling:
The system implements robust validation (try-except blocks) to handle invalid inputs (e.g., negative distances or non-numeric characters) without crashing.

4.4 Maintainability:
The code follows a modular architecture. Configuration data (emission factors) is stored in a separate file (config.py), making it easy to update vehicle statistics without rewriting the logic.

5. System Architecture

The project follows a Modular Design pattern to ensure separation of concerns.

Presentation Layer (main.py): Handles user input and displays results.

Logic Layer (emissions_logic.py): Contains the algorithms for calculation.

Data Layer (history_manager.py): Manages reading and writing to the CSV storage.

Configuration (config.py): Stores static constants and emission factors.

6. Design Decisions & Rationale

Why Python? Selected for its strong data handling capabilities, readability, and vast standard library support.

Why CSV over SQL? For a single-user desktop application, a CSV file offers portability and human-readability (can be opened in Excel) without the overhead of installing a local database server like MySQL or PostgreSQL.

The "Trees" Metric: Raw CO2 numbers are abstract to the average user. Converting them to "Trees Needed" adds a psychological "Gamification" element, making the data more actionable.

7. Implementation Details

The project is built using Python 3.x. It utilizes the csv library for data management and the datetime library for logging timestamps.

Key Code Snippet (Logic Module):

def calculate_emissions(vehicle_type, fuel_type, distance_km):
    # Retrieve factor from config dictionary
    grams_per_km = EMISSION_FACTORS[vehicle_type][fuel_type]
    
    # Calculate total grams
    total_grams = grams_per_km * float(distance_km)
    
    # Convert to Kilograms for final output
    return total_grams / 1000.0

8. Testing Approach

8.1 Test Case 1: High Emission Scenario

Input: Vehicle = SUV, Fuel = Diesel, Distance = 100km

Expected Output: ~22.0 kg CO2

Actual Result: Pass

8.2 Test Case 2: Zero Emission Scenario

Input: Vehicle = Small Car, Fuel = Electric, Distance = 50km

Expected Output: 0.0 kg CO2

Actual Result: Pass

8.3 Test Case 3: Data Check

Action: Save a trip, close the application, and restart it.

Expected Output: The saved trip appears in the History table.

Actual Result: Pass

9. Challenges Faced

Module Import Errors: During development, I faced ImportError issues because the file structure was split into multiple modules (calculator vs emissions_logic). This was resolved by standardizing the filenames and ensuring the import statements in main.py matched the file locations exactly.

File Handling Logic: Handling the first-run scenario where trip_history.csv did not exist caused a crash. This was solved by adding a check to create the file header automatically if the file is missing.

10. Learnings & Key Takeaways

Modular Programming: Learned how to structure a Python project into modular components (Logic, Data, UI) rather than writing a single monolithic script.

File I/O: Gained practical experience with reading and writing CSV files for persistent data storage.

Input Validation: Understood the importance of sanitizing user inputs to prevent runtime errors.

11. Future Enhancements

Graphical User Interface (GUI): Implement a frontend using Tkinter or CustomTkinter for a more modern user experience.

Visualization: Integrate matplotlib to generate graphs showing emission trends over the last month.

Cloud Sync: Move the storage from a local CSV to a cloud database (Firebase) to allow access from multiple devices.
