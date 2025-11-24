# EcoMeter: Vehicle Emission Tracker

## Project Overview
EcoMeter is a modular Python application that calculates the carbon footprint of daily vehicle travel. It tracks history and visualizes the impact in terms of "trees required to offset emissions," helping users make eco-friendly decisions.

## Features
- **Emission Calculator:** Supports Small Cars, SUVs, Motorbikes, and Buses.
- **Impact Analysis:** Converts CO2 mass into tree equivalents.
- **History Tracking:** Saves all trips to a CSV file (`trip_history.csv`) for future reference.

## How to Run
1. Ensure Python 3.x is installed.
2. Open a terminal in the project folder.
3. Run the command: `python main.py`
4. Follow the on-screen menu to calculate emissions or view history.

## Technologies Used
- **Python 3.x**: Core logic.
- **CSV Module**: Data persistence.
- **Modular Architecture**: Separate logic, config, and storage layers.