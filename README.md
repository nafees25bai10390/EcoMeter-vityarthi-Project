EcoMeter: Vehicle Emission Tracker

Project Overview
EcoMeter is a Python application that calculates vehicle CO2 emissions and tracks trip history.

Key Features
Emission Calculator: Support Car, SUV, Motorbike, and Bus.
Persistence: Automatically saves trip history to a local CSV file.
Impact Analysis: Converts CO2 mass into a "Trees Needed" metric.
Error Handling: Validates inputs to prevent crashes.

Technologies Used
Python 3.x
CSV Module (Data Storage)

How to Install & Run
1.Download: Clone the repository or download the folder.
2.Navigate: Open a terminal in the folder: `cd EcoMeter_Project`
3.Run: Execute the command: `python main.py`

Testing Instructions
Test Calculation: Select Option 1 -> Enter `suv`, `diesel`, `100` (Distance). Result should be ~22.0 kg CO2.
Test History: Select Option 2 -> Verify the trip appears in the table.
Test Validation:** Select Option 1 -> Enter `-50` as distance. Ensure it shows an error message.
