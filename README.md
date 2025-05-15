# HSN Code Validation Agent

## Overview

This project is a web-based intelligent agent designed to validate Harmonized System Nomenclature (HSN) codes using a master Excel dataset. It follows a modular architecture inspired by Google's conceptual Agent Developer Kit (ADK), applying clear separation between intents, entities, fulfillment logic, and data access.

## Features

- Accepts user input for HSN code validation
- Validates code format (numeric and correct length)
- Checks existence in the official master list
- Detects hierarchy of parent codes (e.g., chapter, heading, subheading)
- Provides detailed and human-readable feedback
- Reloads master data dynamically if updated
- Simple web interface for user interaction

## Folder Structure

```
HSNValidationAgent/
├── agent/
│   ├── intents.py          # Defines validation intent
│   └── entities.py         # Defines HSNCode entity
├── data/
│   └── loader.py           # Loads and caches Excel data
├── validation/
│   └── code_validator.py   # Core validation logic
├── web_app/
│   ├── app.py              # Flask web app
│   └── templates/
│       └── index.html      # HTML interface
├── HSN_SAC.xlsx            # Provided HSN master data file
├── requirements.txt        # Dependencies list
└── README.md               # Project documentation
```

## How It Works

### Agent Components

- **Intent**: `ValidateCode` is the action the agent takes when a user submits an HSN code.
- **Entity**: `HSNCode` is the piece of information extracted from the user's input.
- **Fulfillment**: A Python class (`HSNValidator`) evaluates the code and returns meaningful feedback.
- **Data Store**: The master Excel sheet is read and transformed into a dictionary for efficient lookup.

### Validation Rules

1. **Format Validation**
   - The code must be all numeric.
   - Its length should be between 2 and 8 digits.

2. **Existence Check**
   - The code must be listed in the HSN master dataset.

3. **Hierarchical Validation (Optional)**
   - For 4, 6, or 8-digit codes, their parent categories (e.g., 2 or 4 digits) should also exist.

### Edge Case Handling

- Blank or non-numeric inputs return an error.
- Unknown codes give a “not found” message.
- Hierarchical gaps raise a warning.

## Setup Instructions

1. **Install Python** (version 3.8 or higher)

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Web Application**

```bash
python web_app/app.py
```

4. **Access in Browser**

Open [http://localhost:5000](http://localhost:5000)

## Updating the Data

To update the master dataset:

- Replace `HSN_SAC.xlsx` with a new version.
- The app automatically reloads the data on the next request.

## Credits and Design Notes

- Inspired by Google's ADK conceptual model for agent architecture.
- Modular, readable, and scalable codebase for ease of maintenance.
- Designed with practical business use cases in mind for trade and invoicing.

## License

This project is open for educational and demonstration purposes. Adapt freely with proper citation.