#  Hospital Database Management System

A robust, pure Python command-line application designed to automate hospital workflows. This system efficiently tracks patient data, manages doctor assignments, handles room allocations, and computes automated discharge financial billing.

##  Key Features

*   **Patient Record Registry**: Built using optimized Python dictionary lookups for instant patient history retrieval.
*   **Dynamic Room Allocation**: Manages available room inventories and links them to specific patient tracks.
*   **Staff Tracking**: Maintains active rosters for specialized attending doctors.
*   **Automated Billing Engine**: Processes room rent, days stayed, and medical variables to generate crash-free financial checkout summaries.

##  Tech Stack & Concepts Applied

*   **Language**: Python 3
*   **Data Structures**: Nested Dictionaries, Lists, and Tuples.
*   **Core Concepts**: Data validation, automated type casting, error/boundary handling, and algorithmic status updates.

##  How It Works (Sample Flow)

1. **Registration**: The system registers a unique Patient ID (e.g., `P101`).
2. **Allocation**: Assigns a room index and an attending doctor.
3. **Checkout**: Converts text-based terminal inputs into processed integers to calculate total discharge dues without type crashes.

## 💻 Getting Started

### Prerequisites
1. Make sure you have Python 3 installed on your desktop.
2. Also tabulate needs to be pip installed in ur Computer.

### Execution
1. Clone this repository or download the source code file.
2. Open the project directory inside **VS Code** or **PyCharm**.
3. Run the script via your terminal:
   ```bash
   python main.py
   ```

##  Bug Fix Log & Safeguards Implemented

This project applies high-utility programming logic to solve common runtime vulnerabilities:
*   **KeyError Avoidance**: Implemented dictionary structural checks (`if key in dict`) to prevent crashes when searching for non-existent Patient IDs.
*   **Input Type Casting**: Wrapped terminal inputs in explicit `int()` casts to eliminate string-multiplication failures during billing calculations.
*   **IndexError Bounds Checking**: Added length boundary constraints (`0 <= index < len(list)`) to block invalid room or doctor selection slips.
