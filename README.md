# Egyptian ID Parser

This Python script allows you to parse and extract useful information from an Egyptian national ID number. The parser extracts the following details:
- Birth date
- Governorate of issue
- Gender
- Age in years, months, and days

## Features

- **Birth Date Extraction**: Extracts and formats the birth date from the ID number.
- **Governorate Identification**: Determines the governorate where the ID was issued.
- **Gender Identification**: Identifies the gender based on the unique serial number.
- **Age Calculation**: Calculates the person's age in years, months, and days.
- **Input Validation**: Ensures the ID is exactly 14 digits and numeric.
- **Error Handling**: Catches and reports invalid dates or century codes in the ID.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/HossamElbesh/Egyptian-ID-Parser.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Egyptian-ID-Parser
    ```

3. Run the script:

    ```bash
    python EgyptianIdParser.py
    ```
